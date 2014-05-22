package edu.indiana.d2i.komadu.messaging;

import java.io.IOException;
import org.apache.log4j.Logger;
import edu.indiana.d2i.komadu.ingest.NotificationIngester;
import edu.indiana.d2i.komadu.query.QueryImplementer;
import edu.indiana.d2i.komadu.util.ServiceLauncher;
/**
 * @author Quan Zhou (quzhou@indiana.edu)
 */
public class MessageDaemons  {

	private Thread[] NotificationDeamons;
	private Thread[] QueryDeamons;
	private int numOfNofiticationDeamons;
	private int numOfQueryDaemons;
	
	private Logger log;
	
	public MessageDaemons(MessageDaemonsConfig msgdmconf, MessageConfig msgconf, NotificationIngester ingester, QueryImplementer querier) throws IOException{
		this.numOfNofiticationDeamons = msgdmconf.getNumberOfNotificationDaemons();
		this.numOfQueryDaemons=msgdmconf.getNumberOfQueryDaemons();
		this.NotificationDeamons=new Thread[numOfNofiticationDeamons];
		this.QueryDeamons=new Thread[numOfQueryDaemons];
		
		NotificationReceiverRunnable msgrr=new NotificationReceiverRunnable(msgconf, ingester);
	    for (int i = 0; i < this.numOfNofiticationDeamons; i++) {
			this.NotificationDeamons[i]= new Thread(msgrr);
		}
	    
	    QueryReceiverRunnable qsgrr=new QueryReceiverRunnable(msgconf, querier);
	    for (int i = 0; i < this.numOfQueryDaemons; i++) {
			this.QueryDeamons[i]= new Thread(qsgrr);
		}
	    
	    
	}
	
	public void start() throws java.lang.IllegalMonitorStateException{
		log = Logger.getLogger(MessageDaemons.class);
		for (int i = 0; i < this.numOfNofiticationDeamons; i++) {
			log.info("Starting Notification Deamon ["+i+"]  for receiving notifications from Client.");    
			this.NotificationDeamons[i].start();
		    log.info("Notification Deamon ["+i+"] Started.");
		}
	    
		for (int i = 0; i < this.numOfQueryDaemons; i++) {
			log.info("Starting Query Deamon ["+i+"] for receiving queries from Client.");
		    this.QueryDeamons[i].start();
		    log.info("Query Deamon ["+i+"] Started.");

		}
	    
	}
		
	/**
	 * @param args
	 */
	public static void main(String[] args) {
        try {
            
            if (args.length < 1) {
                System.err.println("ERROR: properties file not specified");
                System.err.println("Usage:  ServiceLauncher <propertiesFilePath>");
                throw new Exception("ERROR: properties file not specified");
            }
            String propertiesFilePath = args[0];
            ServiceLauncher.start(propertiesFilePath);
            if(!ServiceLauncher.startMessageReceiverDaemon()){
            	//If MessageReceiverDaemon can't be started, shall we shutdown the whole Karma Server? If yes, add the code here.
            	System.err.println("Unable to launch MessageReceiverDaemon");
            }
           
        } catch (Throwable e) {
        	System.err.println("Unable to launch service");
        }
        System.out.println("Main ends here");

    }

}