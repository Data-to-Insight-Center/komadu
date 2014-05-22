/**
 * 
 */
package edu.indiana.d2i.komadu.client.test;

import java.io.File;
import java.io.IOException;

import edu.indiana.d2i.komadu.client.messaging.Notification;
import edu.indiana.d2i.komadu.messaging.MessageConfig;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 *
 */
public class MassiveNotificationTest {
	public static void main(String[] args) {
		if(args.length!=3){
			System.out.println("SendNotification:\nargs[0]: Message Configuration File.\nargs[1]: Notification in XML file format.\nargs[2]: Notification Interation.");
			System.out.println("Please check the parameters.");
			return;
		}
		String MessageConfigPath=args[0];
		String pathToNotificationFile=args[1];
		int iternation=Integer.parseInt(args[2]);
		long startTime = System.currentTimeMillis();
		for (int i = 0; i < iternation; i++) {
			MessageConfig msgconf=new MessageConfig(MessageConfigPath);
			Notification notification=new Notification(msgconf,MessageConfigPath);
			try {
				notification.sendNotification(new File(pathToNotificationFile));
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			notification.closeConnection();
		}
		long endTime = System.currentTimeMillis();
		System.out.println("Total Execution Time: "+(endTime-startTime));
		
	}
}
