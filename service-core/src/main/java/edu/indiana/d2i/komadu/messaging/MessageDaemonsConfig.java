package edu.indiana.d2i.komadu.messaging;

public class MessageDaemonsConfig{
	private int NumberOfNotificationDaemons;
	private int NumberOfQueryDaemons;
	
	public MessageDaemonsConfig(){
		this.NumberOfNotificationDaemons=1;
		this.NumberOfQueryDaemons=1;
	}
	
	public void setNumberOfNotificationDaemons(int numOfNotificationDaemons){
		this.NumberOfNotificationDaemons=numOfNotificationDaemons;
	}
	public int getNumberOfNotificationDaemons(){
		return this.NumberOfNotificationDaemons;
	}
	
	public void setNumberOfQueryDaemons(int numOfQueryDaemons){
		this.NumberOfQueryDaemons=numOfQueryDaemons;
	}
	public int getNumberOfQueryDaemons(){
		return this.NumberOfQueryDaemons;
	}
}
