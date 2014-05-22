package edu.indiana.d2i.komadu.messaging;

import java.io.IOException;

import org.apache.log4j.Logger;
import org.apache.xmlbeans.XmlException;
import org.apache.xmlbeans.XmlObject;

import com.rabbitmq.client.ShutdownSignalException;
import edu.indiana.d2i.komadu.ingest.NotificationIngester;
import edu.indiana.d2i.komadu.ingest.NotificationSummary.NotificationTypeEnum;
import edu.indiana.d2i.komadu.util.ServiceLauncher;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 */

public class NotificationReceiverRunnable  implements Runnable  {

	private Receiver receiver;
	private NotificationIngester ingester;
	private Logger log;
	private int RETRY_INTERVAL;
	private int RETRY_THRESHOLD;
	
	
	public NotificationReceiverRunnable(MessageConfig msgconf, NotificationIngester ingester) throws IOException{
		this.receiver=new Receiver(msgconf, MessagingOperationTypes.RECEIVE_NOTIFICATIONS);
		this.ingester=ingester;
		this.log = Logger.getLogger(NotificationReceiverRunnable.class);
		this.RETRY_INTERVAL=msgconf.getMessagingRetryInterval();
		this.RETRY_THRESHOLD=msgconf.getMessagingRetryThreshold();
		
	}
	
	public void run() throws java.lang.IllegalMonitorStateException{
		boolean runInfinite=true;
		String notification;
		while (runInfinite) {
			try {
				log.info("[Komadu server: Listening to Messaging System]");
				notification=this.receiver.getMessage();
				log.info("[Komadu server: One Message received]\n"+notification);
				
				System.out.println(NotificationTypeEnum.determineNotificationTypeFromXmlBeansDocument(XmlObject.Factory.parse(notification),1));
				KomaduOperations.storeNotification(this.ingester, 
												NotificationTypeEnum.determineNotificationTypeFromXmlBeansDocument(XmlObject.Factory.parse(notification),1),
												notification);
				
			} catch (ShutdownSignalException e) {
				e.printStackTrace();
					
				this.receiver.abortChannel();
				this.receiver.abortConnection();
				
				boolean reconnected=false;
				int retry_count=0;
				while(!reconnected){
					if(retry_count>this.RETRY_THRESHOLD){
						ServiceLauncher.shutdown();
						return;
					}
					retry_count++;
					reconnected=false;
					try {
						log.info("Reconneting to Messaging Server.");
						this.receiver.createConnection();
						this.receiver.createChannel();
						reconnected=true;
					} catch (IOException e1) {
						log.error("Can't connect to Messaging Server.");
						reconnected=false;
						e1.printStackTrace();
					}
					//Sleep 5*retry_count seconds and try to reconnect again
					try {
						Thread.sleep(this.RETRY_INTERVAL*1000);
					} catch (InterruptedException e3) {
						e3.printStackTrace();
					}
					//break the while loop when reconnected
					if(reconnected){
						try {
							this.receiver.formatChannel();
							log.info("Reconneted to Messaging Server.");
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
				log.error("", e);
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				log.error("", e);
				e.printStackTrace();
			} catch (XmlException e) {
				// TODO Auto-generated catch block
				log.error("", e);
				e.printStackTrace();
			}
			catch (Exception e) {
				// TODO Auto-generated catch block
				log.error("", e);
				e.printStackTrace();
			}

		}
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
