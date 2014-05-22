package edu.indiana.d2i.komadu.messaging;

import java.io.IOException;

import org.apache.log4j.Logger;
import org.apache.xmlbeans.XmlException;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;

import com.rabbitmq.client.ShutdownSignalException;
import edu.indiana.d2i.komadu.ingest.NotificationIngester;
import edu.indiana.d2i.komadu.ingest.NotificationSummary.NotificationTypeEnum;
import edu.indiana.d2i.komadu.query.QueryImplementer;
import edu.indiana.d2i.komadu.util.ServiceLauncher;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 */

public class QueryReceiverRunnable  implements Runnable  {

	private MessageConfig msgconf;
	private Receiver receiver;
	private QueryImplementer querier;
	private Logger log;
	private int RETRY_INTERVAL;
	private int RETRY_THRESHOLD;
	public static final String  INVALID_QUERY_ERROR_STRING = "Invalid Query";
	
	public QueryReceiverRunnable(MessageConfig msgconf, QueryImplementer querier) throws IOException{
		this.msgconf=msgconf;
		this.receiver=new Receiver(msgconf, MessagingOperationTypes.RECEIVE_QUERY_REQUESTS);
		this.querier=querier;
		this.log = Logger.getLogger(QueryReceiverRunnable.class);
		this.RETRY_INTERVAL=msgconf.getMessagingRetryInterval();
		this.RETRY_THRESHOLD=msgconf.getMessagingRetryThreshold();
		
	}
	
	public void run() throws java.lang.IllegalMonitorStateException{
		boolean runInfinite=true;
		String queryMessage;
		while (runInfinite) {
			try {
				log.info("[Komadu server: Listening Queries from Messaging System]");
				queryMessage=this.receiver.getMessage();
				log.info("[Komadu server: One Query received]\n"+queryMessage);
				// Parse the queryMessage
				if(queryMessage!=null){
					String[] queryMessageContents=queryMessage.trim().split("#",2);
					if (queryMessageContents.length!=2) {
						log.info("[Karma server: Invalid Query Request]\n");
					} else {
						String QueryResponseRoutingKey=queryMessageContents[0];
						String query=queryMessageContents[1];
						log.info("[Karma server: Query] "+query);
						log.info("[Karma server: Query Response Routing Key] "+QueryResponseRoutingKey);
						
						//Query
						String queryResult=null;
						try{
							queryResult=KomaduOperations.queryProvenance(querier, XmlObject.Factory.parse(query));
						}catch(Exception e){
							
							queryResult=INVALID_QUERY_ERROR_STRING;
							log.info("[Komadu server: Query Error] "+e.toString());
						}
						//Response
						msgconf.setQueryResponseRoutingKey(QueryResponseRoutingKey);
						Sender sender=new Sender(msgconf, MessagingOperationTypes.SEND_QUERY_RESPONSE);
						try {
							sender.sendMessage(queryResult);
							log.info("[Komadu server: Send Query Response to Client]");
							sender.closeChannel();
							sender.closeConnection();
						} catch (ShutdownSignalException e) {
							// TODO Resend to client
							log.info("[Komadu server: Query Messaging Response Error] "+e.toString());
						} catch (IOException e) {
							// TODO Resend to client
							log.info("[Komadu server: Query Messaging Response Error] "+e.toString());
						} catch (InterruptedException e) {
							// TODO Resend to client
							log.info("[Komadu server: Query Messaging Response Error] "+e.toString());
						} 
					}
				}else {
					log.info("[Komadu server: Empty Query Request]\n");
				}
				
				
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
