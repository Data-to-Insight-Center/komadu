package edu.indiana.d2i.komadu.client.util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import edu.indiana.d2i.komadu.messaging.MessageConfig;
import edu.indiana.d2i.komadu.messaging.MessagingQueue;
import edu.indiana.d2i.komadu.messaging.MessagingQueue.QueueUnBind;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 *
 */
public class QueueUnbind {
public static void main(String[] args) {
	if(args.length!=2){
		System.out.println("SendQuery:\nargs[0]: Message Configuration File.\nargs[1]: Bindings in a file.");
		System.out.println("Please check the parameters.\n" +
				"Execute command \"rabbitmqctl list_bindings\", and copy the lines (bindings) you want to unbind, to a file");
		return;
	}
	String MessageConfigPath=args[0];
	String pathToUnbindFile=args[1];
	long startTime = System.currentTimeMillis();
	BufferedReader reader = null;
	
	
	 try {
		 reader = new BufferedReader(new FileReader(new File(pathToUnbindFile)));
		 String line = null;
		 MessageConfig msgconf=new MessageConfig(MessageConfigPath);
				
	   	while ((line = reader.readLine()) != null){
			String[] elements=line.trim().replace('	', ' ').split(" ");
			
			
			try {
				new MessagingQueue().new QueueUnBind(msgconf, elements[0], elements[1], elements[2]);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	long endTime = System.currentTimeMillis();
	System.out.println("Total Execution Time: "+(endTime-startTime));
	
	


}


}
