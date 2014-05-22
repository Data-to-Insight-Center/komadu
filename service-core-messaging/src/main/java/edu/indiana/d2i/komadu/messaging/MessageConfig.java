package edu.indiana.d2i.komadu.messaging;

import edu.indiana.d2i.komadu.util.PropertyReader;
/**
 * @author Quan Zhou (quzhou@indiana.edu)
 */
public class MessageConfig {
	private String Username;
	private String Password;
	private String VirtualHost;
	private String Host;
	private int Port;
	private String BaseExchangeName;
	private String BaseQueueName;
	private String BaseRoutingKey;
	private String QueryResponseRoutingKey;
	private int MessagingRetryInterval;
	private int MessagingRetryThreshold;
	private PropertyReader property = null;
	
	public MessageConfig(String propertiesPath){
		this.property = PropertyReader.getInstance(propertiesPath);
		this.setUsername(this.property.getProperty("messaging.username"));
		this.setPassword(this.property.getProperty("messaging.password"));
		this.setVirtualHost(this.property.getProperty("messaging.virtualhost"));
		this.setHost(this.property.getProperty("messaging.hostname"));
		this.setPort(Integer.parseInt(this.property.getProperty("messaging.hostport")));
		this.setBaseExchangeName(this.property.getProperty("messaging.exchangename")==null? "KarmaExchange": this.property.getProperty("messaging.exchangename"));
		this.setBaseQueueName(this.property.getProperty("messaging.queuename")==null? "KarmaQueue": this.property.getProperty("messaging.queuename"));
		this.setBaseRoutingKey(this.property.getProperty("messaging.routingkey")==null? "KarmaKey": this.property.getProperty("messaging.routingkey"));
		this.setMessagingRetryInterval(Integer.parseInt(this.property.getProperty("messaging.retry.interval")==null? "5": this.property.getProperty("messaging.retry.interval")));
		this.setMessagingRetryThreshold(Integer.parseInt(this.property.getProperty("messaging.retry.threshold")==null? "5": this.property.getProperty("messaging.retry.threshold")));
	};
	public MessageConfig(String Username, String Password, String Host, int Port, String VirtualHost, String ExchangeName, String QueueName, String RoutingKey, int MessagingRetryInterval, int MessagingRetryThreshold){
		this.setUsername(Username);
		this.setPassword(Password);
		this.setVirtualHost(VirtualHost);
		this.setHost(Host);
		this.setPort(Port);
		this.setBaseExchangeName(ExchangeName);
		this.setBaseQueueName(QueueName);
		this.setBaseRoutingKey(RoutingKey);
		this.setMessagingRetryInterval(MessagingRetryInterval);
		this.setMessagingRetryThreshold(MessagingRetryThreshold);
	};
	public MessageConfig(MessageConfig msgconf){
		this.setUsername(msgconf.getUsername());
		this.setPassword(msgconf.getPassword());
		this.setVirtualHost(msgconf.getVirtualHost());
		this.setHost(msgconf.getHost());
		this.setPort(msgconf.getPort());
		this.setBaseExchangeName(msgconf.getBaseExchangeName());
		this.setBaseQueueName(msgconf.getBaseQueueName());
		this.setBaseRoutingKey(msgconf.getBaseRoutingKey());
		this.setMessagingRetryInterval(msgconf.getMessagingRetryInterval());
		this.setMessagingRetryThreshold(msgconf.getMessagingRetryThreshold());
	};
	
	public void	setUsername(String Username){
		this.Username=Username;
	};
	public void	setPassword(String Password){
		this.Password=Password;
	};
	public void	setVirtualHost(String VirtualHost){
		this.VirtualHost=VirtualHost;
	};
	public void	setHost(String Host){
		this.Host=Host;
	};
	public void setPort(int Port){
		this.Port=Port;
	};
	public void	setBaseExchangeName(String ExchangeName){
		this.BaseExchangeName=ExchangeName;
	};
	public void	setBaseRoutingKey(String RoutingKey){
		this.BaseRoutingKey=RoutingKey;
	};
	public void	setBaseQueueName(String QueueName){
		this.BaseQueueName=QueueName;
	};
	public void setMessagingRetryInterval(int MessagingRetryInterval){
		this.MessagingRetryInterval=MessagingRetryInterval;
	};
	public void setMessagingRetryThreshold(int MessagingRetryThreshold){
		this.MessagingRetryThreshold=MessagingRetryThreshold;
	};
	public String getUsername(){
		return this.Username;
	};
	public String getPassword(){
		return this.Password;
	};
	public String getVirtualHost(){
		return this.VirtualHost;
	};
	public String getHost(){
		return this.Host;
	};
	public int getPort(){
		return this.Port;
	};
	public String getBaseExchangeName(){
		return this.BaseExchangeName;
	};
	public String getBaseRoutingKey(){
		return this.BaseRoutingKey;
	};
	public String getBaseQueueName(){
		return this.BaseQueueName;
	};
	public String getNotificationExchangeName(){
		return this.BaseExchangeName+"_Notification";
	};
	public String getNotificationRoutingKey(){
		return this.BaseRoutingKey+"_Notification";
	};
	public String getNotificationQueueName(){
		return this.BaseQueueName+"_Notification";
	};
	public String getQueryRequestExchangeName(){
		return this.BaseExchangeName+"QueryRequest";
	};
	public String getQueryRequestRoutingKey(){
		return this.BaseRoutingKey+"QueryRequest";
	};
	public String getQueryRequestQueueName(){
		return this.BaseQueueName+"QueryRequest";
	};
	public String getQueryResponseExchangeName(){
		return this.BaseExchangeName+"QueryResponse";
	};
	public String getQueryResponseQueueName(){
		return this.BaseQueueName+"QueryResponse";
	};
	public String getQueryResponseRoutingKey(){
		return this.QueryResponseRoutingKey;
	};
	public void setQueryResponseRoutingKey(String QueryResponseRoutingKey){
		this.QueryResponseRoutingKey=QueryResponseRoutingKey;
	};
	
	public int getMessagingRetryInterval(){
		return this.MessagingRetryInterval;
	};
	public int getMessagingRetryThreshold(){
		return this.MessagingRetryThreshold;
	};
	

}
