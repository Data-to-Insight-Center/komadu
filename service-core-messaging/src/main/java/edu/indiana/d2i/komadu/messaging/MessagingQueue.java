package edu.indiana.d2i.komadu.messaging;

import java.io.IOException;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.QueueingConsumer;
import com.rabbitmq.client.ShutdownSignalException;
/**
 * @author Quan Zhou (quzhou@indiana.edu)
 */

public class MessagingQueue {
	
	
	public class QueueBind{
		public ConnectionFactory factory;
		public Connection conn;
		public Channel channel;
		public String ExchangeName;
		public String QueueName;
		public String RoutingKey;
		public QueueingConsumer consumer;
		
		public QueueBind(MessageConfig msgconf, String ExchangeName, String QueueName, String RoutingKey) throws IOException{
			this.factory = new ConnectionFactory();
			this.factory.setUsername(msgconf.getUsername());
			this.factory.setPassword(msgconf.getPassword());
			this.factory.setVirtualHost(msgconf.getVirtualHost());
			this.factory.setHost(msgconf.getHost());
			this.factory.setPort(msgconf.getPort());

			this.ExchangeName = ExchangeName;
			this.QueueName = QueueName;
			this.RoutingKey = RoutingKey;
			createConnection();
			createChannel();
			bind();
			closeChannel();
			closeConnection();
			
		};

		private void createConnection() throws IOException{
			this.conn = this.factory.newConnection();
		}
		private void createChannel() throws IOException{
			this.channel = this.conn.createChannel();
		}
		private void bind() throws IOException{
			
			boolean durable = true;
			this.channel.exchangeDeclare(this.ExchangeName, "direct", durable);
			this.channel.queueDeclare(this.QueueName, durable,false,false,null);
			this.channel.queueBind(this.QueueName, this.ExchangeName, this.RoutingKey);

		}
		
		private void unbind() throws IOException{
			
			boolean durable = true;
			this.channel.exchangeDeclare(this.ExchangeName, "direct", durable);
			this.channel.queueDeclare(this.QueueName, durable,false,false,null);
			this.channel.queueUnbind(this.QueueName, this.ExchangeName, this.RoutingKey);

		}
		private void abortChannel(){
			try {
				this.channel.abort();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		private void closeChannel(){
			try {
				this.channel.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		private void abortConnection(){
			this.conn.abort();
		}
		private void closeConnection(){
			try {
				this.conn.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

	}
	public class QueueUnBind{
		public ConnectionFactory factory;
		public Connection conn;
		public Channel channel;
		public String ExchangeName;
		public String QueueName;
		public String RoutingKey;
		public QueueingConsumer consumer;
		
		public QueueUnBind(MessageConfig msgconf, String ExchangeName, String QueueName, String RoutingKey) throws IOException{
			this.factory = new ConnectionFactory();
			this.factory.setUsername(msgconf.getUsername());
			this.factory.setPassword(msgconf.getPassword());
			this.factory.setVirtualHost(msgconf.getVirtualHost());
			this.factory.setHost(msgconf.getHost());
			this.factory.setPort(msgconf.getPort());

			this.ExchangeName = ExchangeName;
			this.QueueName = QueueName;
			this.RoutingKey = RoutingKey;
			createConnection();
			createChannel();
			unbind();
			closeChannel();
			closeConnection();
			
		};

		private void createConnection() throws IOException{
			this.conn = this.factory.newConnection();
		}
		private void createChannel() throws IOException{
			this.channel = this.conn.createChannel();
		}
		private void bind() throws IOException{
			
			boolean durable = true;
			this.channel.exchangeDeclare(this.ExchangeName, "direct", durable);
			this.channel.queueDeclare(this.QueueName, durable,false,false,null);
			this.channel.queueBind(this.QueueName, this.ExchangeName, this.RoutingKey);

		}
		
		private void unbind() throws IOException{
			
			boolean durable = true;
			this.channel.exchangeDeclare(this.ExchangeName, "direct", durable);
			this.channel.queueDeclare(this.QueueName, durable,false,false,null);
			this.channel.queueUnbind(this.QueueName, this.ExchangeName, this.RoutingKey);

		}
		private void abortChannel(){
			try {
				this.channel.abort();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		private void closeChannel(){
			try {
				this.channel.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		private void abortConnection(){
			this.conn.abort();
		}
		private void closeConnection(){
			try {
				this.conn.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

	}
}
