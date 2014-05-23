package edu.indiana.d2i.komadu.messaging;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.MessageProperties;

import com.rabbitmq.client.ShutdownSignalException;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 */

public class Sender {
	
	public ConnectionFactory factory;
	public Connection conn;
	public Channel channel;
	public String ExchangeName;
	public String QueueName;
	public String RoutingKey;
	
	public Sender(MessageConfig msgconf) throws IOException{
		this.factory = new ConnectionFactory();
		this.factory.setUsername(msgconf.getUsername());
		this.factory.setPassword(msgconf.getPassword());
		this.factory.setVirtualHost(msgconf.getVirtualHost());
		this.factory.setHost(msgconf.getHost());
		this.factory.setPort(msgconf.getPort());
		
		this.conn = this.factory.newConnection();
		this.channel = this.conn.createChannel();
		this.ExchangeName = msgconf.getBaseExchangeName();
		this.RoutingKey = msgconf.getBaseRoutingKey();
		
	};	
	public Sender(MessageConfig msgconf, MessagingOperationTypes OpType) throws IOException{
		this.factory = new ConnectionFactory();
		this.factory.setUsername(msgconf.getUsername());
		this.factory.setPassword(msgconf.getPassword());
		this.factory.setVirtualHost(msgconf.getVirtualHost());
		this.factory.setHost(msgconf.getHost());
		this.factory.setPort(msgconf.getPort());
		this.conn = this.factory.newConnection();
		this.channel = this.conn.createChannel();
		
		switch (OpType) {
		case SEND_QUERY_REQUEST:
			this.ExchangeName = msgconf.getQueryRequestExchangeName();
			this.RoutingKey = msgconf.getQueryRequestRoutingKey();
			break;
		case SEND_QUERY_RESPONSE:
			this.ExchangeName = msgconf.getQueryResponseExchangeName();
			this.RoutingKey = msgconf.getQueryResponseRoutingKey();
			break;
		case SEND_NOTIFICATION:
			this.ExchangeName = msgconf.getNotificationExchangeName();
			this.RoutingKey = msgconf.getNotificationRoutingKey();
			break;
		default:
			try {
				throw new Exception("OperationType: "+OpType.toString()+" not supported.");
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			break;
		}
		
	};
	
	public void closeChannel(){
		try {
			if(this.channel.isOpen()){
				this.channel.close();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void closeConnection(){
		try {
			this.closeChannel();
			if(this.conn.isOpen()){
				this.conn.close();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	public void sendMessage(String message) throws IOException, ShutdownSignalException, InterruptedException{
		byte[] messageBodyBytes = message.getBytes();
		this.channel.basicPublish(this.ExchangeName, this.RoutingKey, MessageProperties.PERSISTENT_TEXT_PLAIN, messageBodyBytes) ;
		
	};
	
	public void sendMessage(File messageFile) throws IOException, ShutdownSignalException, InterruptedException{
		InputStream is = new FileInputStream(messageFile);

	    // Get the size of the file
	    long length = messageFile.length();
	    if (length > Integer.MAX_VALUE) {
	    	throw new IOException("Input File ("+messageFile.getName()+") is to large! ");
	    }
	    byte[] messageBodyBytes = new byte[(int)length];
	    int offset = 0;
	    int numRead = 0;
	    while (offset < messageBodyBytes.length
	           && (numRead=is.read(messageBodyBytes, offset, messageBodyBytes.length-offset)) >= 0) {
	        offset += numRead;
	    }
	    if (offset < messageBodyBytes.length) {
	        throw new IOException("Could not completely read file "+messageFile.getName());
	    }
	    is.close();
		this.channel.basicPublish(this.ExchangeName, this.RoutingKey, MessageProperties.PERSISTENT_TEXT_PLAIN, messageBodyBytes) ;
		
	};
	
	/*public static void main(String[] args) throws ShutdownSignalException, IOException, InterruptedException {
    		MessageConfig msgconf=new MessageConfig("/Users/yuanluo/WorkZone/workspace/Karma-Service/config/karma.properties");
    		Sender sender=new Sender(msgconf, MessagingOperationTypes.SEND_NOTIFICATION);
    		System.out.println(sender.RoutingKey);
    		File messageFile=new File("/Users/yuanluo/WorkZone/workspace/Karma-Client-Core/samples/sendingResponse.xml");
    		sender.sendMessage(messageFile);
    		sender.closeConnection();
		

	}*/

}