/*
#
# Copyright 2007 The Trustees of Indiana University
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
# Project:		Karma Provenance Client
# File:			Notification.java
# Description:	API for sending notifications to Karma Provenance Server, 
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
import java.util.ArrayList;
import java.util.Calendar;

import org.apache.xmlbeans.SchemaTypeLoader;
import org.apache.xmlbeans.XmlBeans;
import org.apache.xmlbeans.XmlError;
import org.apache.xmlbeans.XmlException;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;
import com.rabbitmq.client.ShutdownSignalException;

import edu.indiana.d2i.komadu.messaging.MessageConfig;
import edu.indiana.d2i.komadu.messaging.MessagingOperationTypes;
import edu.indiana.d2i.komadu.messaging.Sender;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 *
 */
public class Notification {
	private Sender sender;
	private File schemaFile;
	/**
	 * 
	 * @param msgconf
	 */
	public Notification(MessageConfig msgconf, String msgconfPath){
		try {
			this.sender=new Sender(msgconf, MessagingOperationTypes.SEND_NOTIFICATION);
			String schemaPath=PropertyReader.getInstance(msgconfPath).getProperty("komadu.ingest.schema");
			System.out.println(schemaPath);
			this.schemaFile=new File(schemaPath);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	/**
	 * Send Notification to Komadu Server through Message Bus.
	 * @param Notification
	 * @throws XmlException
	 */
	public void sendNotification(XmlObject Notification) throws XmlException{
		/*
		 * TO DO: Add Notification Validation code here
		 */
		try{
		if(!Validation.validate(Notification, schemaFile)){
			throw new XmlException("\nFail to Send Message: Invalid Notification Format");
		}else{
			try {
				sender.sendMessage(Notification.xmlText(new XmlOptions().setSavePrettyPrint()));
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
	}
	/**
	 * Send Notification to Komadu Server through Message Bus.
	 * @param notification
	 */
	public void sendNotification(String notification){
		//Validate Notification Format
    	try {
    		if(!Validation.validate(notification, schemaFile)){
    			throw new XmlException("\nFail to Send Message: Invalid Notification Format");
			}else{
				try {
					sender.sendMessage(notification);
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
	}
	/**
	 * Send Notification to Komadu Server through Message Bus.
	 * @param NotificationFile
	 * @throws IOException
	 */
	public void sendNotification(File NotificationFile) throws IOException{
		
		try {
			XmlObject notification=XmlObject.Factory.parse(NotificationFile);

	    	if(!Validation.validate(NotificationFile, schemaFile)){
				throw new XmlException("\nFail to Send Message: Invalid Notification Format");
			}else{
			    try {
					sender.sendMessage(notification.xmlText(new XmlOptions().setSavePrettyPrint()));
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
	}
	/**
	 * Close Messaging Channel
	 */
	public void closeChannel(){
		this.sender.closeChannel();
	}
	/**
	 * Close Messaging Channel and Close Message Bus Connection
	 */
	public void closeConnection(){
		this.sender.closeConnection();
	}

	
	
	public static void main(String[] args) {
		if(args.length!=2){
			System.out.println("SendNotification:\nargs[0]: Message Configuration File.\nargs[1]: Notification in XML file format.");
			System.out.println("Please check the parameters.");
			return;
		}
		String MessageConfigPath=args[0];
		String pathToNotificationFile=args[1];
		long startTime = System.currentTimeMillis();
		MessageConfig msgconf=new MessageConfig(MessageConfigPath);
		Notification notification=new Notification(msgconf, MessageConfigPath);
		try {
			notification.sendNotification(new File(pathToNotificationFile));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		notification.closeConnection();

		long endTime = System.currentTimeMillis();
		System.out.println("Total Execution Time: "+(endTime-startTime));
	}
}
