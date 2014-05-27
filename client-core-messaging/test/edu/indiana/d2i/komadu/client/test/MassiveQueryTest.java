/**
 * 
 */
package edu.indiana.d2i.komadu.client.test;

import java.io.File;

import edu.indiana.d2i.komadu.client.messaging.Query;
import edu.indiana.d2i.komadu.messaging.MessageConfig;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 *
 */
public class MassiveQueryTest {
	public static void main(String[] args) {
		if(args.length!=2){
			System.out.println("Query:\nargs[0]: Message Configuration File.\nargs[1]: Query in XML file format.\nargs[2]: Query Interation.");
			System.out.println("Please check the parameters.");
			return;
		}
		String MessageConfigPath=args[0];
		String pathToQueryFile=args[1];
		int iternation=Integer.parseInt(args[2]);
		long startTime = System.currentTimeMillis();
		MessageConfig msgconf=new MessageConfig(MessageConfigPath);
		Query query=new Query(msgconf, MessageConfigPath);
		for (int i = 0; i < iternation; i++) {
			System.out.println("["+i+"]\n"+query.query(new File(pathToQueryFile)));
			
		}
		query.closeConnection();
		
		long endTime = System.currentTimeMillis();
		System.out.println("Total Execution Time: "+(endTime-startTime));
		

	}
}
