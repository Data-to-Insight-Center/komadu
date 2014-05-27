/*
#
# Copyright 2014 The Trustees of Indiana University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or areed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -----------------------------------------------------------------
#
# Project:		Komadu Provenance Client
# File:			Notification.java
# Description:	API for sending notifications to Komadu Provenance Server, 
#				through Messaging Bus.  
#
# -----------------------------------------------------------------
# 
*/
package edu.indiana.d2i.komadu.client.messaging;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Calendar;
import java.util.UUID;

import org.apache.xmlbeans.XmlException;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;
import com.rabbitmq.client.ShutdownSignalException;


import edu.indiana.d2i.komadu.messaging.MessagingQueue.QueueBind;
import edu.indiana.d2i.komadu.messaging.KomaduOperations;
import edu.indiana.d2i.komadu.messaging.MessagingOperationTypes;
import edu.indiana.d2i.komadu.messaging.MessageConfig;
import edu.indiana.d2i.komadu.messaging.MessagingQueue;
import edu.indiana.d2i.komadu.messaging.Receiver;
import edu.indiana.d2i.komadu.messaging.Sender;


/**
 * @author Quan Zhou (quzhou@indiana.edu)
 *
 */
public class Query {
	private Sender sender;
	private Receiver receiver;
	private MessageConfig msgconf;
	private File schemaFile;
	
	/**
	 * 
	 * @param msgconf
	 */
	public Query(MessageConfig msgconf, String msgconfPath){
		try {
			this.msgconf=msgconf;
			this.sender=new Sender(msgconf,MessagingOperationTypes.SEND_QUERY_REQUEST);
			String schemaPath=PropertyReader.getInstance(msgconfPath).getProperty("komadu.query.schema");
			this.schemaFile=new File(schemaPath);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	/**
	 * Send Query to Komadu Server through Message Bus.
	 * @param Query
	 * @throws XmlException
	 */
	public String sendQueryRequest(XmlObject query) throws XmlException{
		
		try{
			if(!Validation.validate(query,schemaFile)){
				throw new XmlException("Fail to Send Message: Invalid Query Format");
			}else{
				String ResponseRoutingKey=UUID.randomUUID().toString();
				try {
					//Bind response exchange-queue-routingkey before send request.
					new MessagingQueue().new QueueBind(this.msgconf, this.msgconf.getQueryResponseExchangeName(), this.msgconf.getQueryResponseQueueName(), ResponseRoutingKey);
					//send message
					this.sender.sendMessage(ResponseRoutingKey+"#"+query.xmlText(new XmlOptions().setSavePrettyPrint()));
					return ResponseRoutingKey;
				} catch (ShutdownSignalException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}catch (XmlException e){
			e.printStackTrace();
		}
		return null;
	}
	/**
	 * Send Query to Komadu Server through Message Bus.
	 * @param Query
	 */
	public String sendQueryRequest(String query){
		//Validate Query Format
    	try {
			if(!Validation.validate(query,schemaFile)){
				throw new XmlException("Fail to Send Message: Invalid Query Format");
			}else{
				String ResponseRoutingKey=UUID.randomUUID().toString();
				try {
					//Bind response exchange-queue-routingkey before send request.
					new MessagingQueue().new QueueBind(this.msgconf, this.msgconf.getQueryResponseExchangeName(), this.msgconf.getQueryResponseQueueName(), ResponseRoutingKey);
					//send message
					this.sender.sendMessage(ResponseRoutingKey+"#"+query);
					return ResponseRoutingKey;
				} catch (ShutdownSignalException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		} catch (XmlException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	/**
	 * Send Query to Komadu Server through Message Bus.
	 * @param QueryFile
	 * @throws IOException
	 */
	public String sendQueryRequest(File QueryFile) throws IOException{
		
		try {
	    	XmlObject query=XmlObject.Factory.parse(QueryFile);
			//Validate Query Format
	    	if(!Validation.validate(query,schemaFile)){
				throw new XmlException("Fail to Send Message: Invalid Query Format");
			}else{
				String ResponseRoutingKey=UUID.randomUUID().toString();
				try {
					//Bind response exchange-queue-routingkey before send request.
					new MessagingQueue().new QueueBind(this.msgconf, this.msgconf.getQueryResponseExchangeName(), this.msgconf.getQueryResponseQueueName(), ResponseRoutingKey);
					//send message
					this.sender.sendMessage(ResponseRoutingKey+"#"+query.xmlText(new XmlOptions().setSavePrettyPrint()));
					return ResponseRoutingKey;
				} catch (ShutdownSignalException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} 
			}
		} catch (XmlException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	/**
	 * Receive Query Response from Komadu Server via Message Bus.
	 * @param QueryFile
	 * @throws IOException
	 */
	public String receiveQueryResponse(String ResponseRoutingKey) throws IOException{
		
		try {
			this.msgconf.setQueryResponseRoutingKey(ResponseRoutingKey);
			this.receiver=new Receiver(this.msgconf,MessagingOperationTypes.RECEIVE_QUERY_RESPONSE);
			String QueryResponse=this.receiver.getMessage();
			this.receiver.closeConnection();
			//Unbind after receiving message
			new MessagingQueue().new QueueUnBind(this.msgconf, this.msgconf.getQueryResponseExchangeName(), this.msgconf.getQueryResponseQueueName(), ResponseRoutingKey);
			return QueryResponse;
			
		} catch (ShutdownSignalException e) {
			e.printStackTrace();
				
			this.receiver.abortChannel();
			this.receiver.abortConnection();
			
			boolean reconnected=false;
			int retry_count=0;
			while(!reconnected){
				if(retry_count>3){
					return null;
				}
				retry_count++;
				reconnected=false;
				try {
					this.receiver.createConnection();
					this.receiver.createChannel();
					reconnected=true;
				} catch (IOException e1) {
					reconnected=false;
					e1.printStackTrace();
				}
				//break the while loop when reconnected
				if(reconnected){
					try {
						this.receiver.formatChannel();
						break;
					} catch (IOException e1) {
						reconnected=false;
						this.receiver.closeChannel();
						this.receiver.closeConnection();
					}
					
				}
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	/**
	 * Close Messaging Channel
	 */
	public void closeChannel(){
		this.sender.closeChannel();
		this.receiver.closeChannel();
	}
	/**
	 * Close Messaging Channel and Close Message Bus Connection
	 */
	public void closeConnection(){
		this.sender.closeConnection();
		this.receiver.closeConnection();
	}

	public String query(String Query){
		String queryResponse=new String();
		try {
			String responseRoutingKey=this.sendQueryRequest(Query);
			queryResponse= this.receiveQueryResponse(responseRoutingKey);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return queryResponse; 
	}
	
	public String query(XmlObject Query){
		String queryResponse=new String();
		try {
			String responseRoutingKey=this.sendQueryRequest(Query);
			queryResponse= this.receiveQueryResponse(responseRoutingKey);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return queryResponse; 
	}
	
	public String query(File QueryFile){
		String queryResponse=new String();
		try {
			String responseRoutingKey=this.sendQueryRequest(QueryFile);
			queryResponse= this.receiveQueryResponse(responseRoutingKey);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return queryResponse; 
	}
	
	public static void main(String[] args) {
		if(args.length!=2){
			System.out.println("Query:\nargs[0]: Message Configuration File.\nargs[1]: Query in XML file format.");
			System.out.println("Please check the parameters.");
			return;
		}
		String MessageConfigPath=args[0];
		String pathToQueryFile=args[1];
		long startTime = System.currentTimeMillis();
		MessageConfig msgconf=new MessageConfig(MessageConfigPath);
		Query query=new Query(msgconf, MessageConfigPath);
		String queryResult=query.query(new File(pathToQueryFile));
		query.closeConnection();
		
		System.out.println("Query Result:\n"+queryResult);

		long endTime = System.currentTimeMillis();
		System.out.println("Total Execution Time: "+(endTime-startTime));
		
	}

}
