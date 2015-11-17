package edu.indiana.d2i.komadu.axis2.client;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import java.util.HashMap;
import java.util.Map;

@RunWith(JUnit4.class)
public class KomaduClientAPITests {

    private static KomaduClient client;

    @BeforeClass
    public static void init() {
        try {
            System.out.println("Initializing Komadu tests...");
            client = new KomaduClient();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @AfterClass
    public static void shutdown() {
        try {
            System.out.println("Shutting down Komadu tests...");
            client.shutdown();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testActivityGraph() {
        Map<String, String> entityAttributes = new HashMap<String, String>();
        entityAttributes.put(KomaduClientConstants.ENTITY_FILE, "true");
        entityAttributes.put(KomaduClientConstants.FILE_URI, "test_file1.text");
        entityAttributes.put(KomaduClientConstants.FILE_NAME, "test_file1.text");
        entityAttributes.put(KomaduClientConstants.FILE_SIZE, "200");
        entityAttributes.put("location", "/home/isuru/test_file1.text");
        Map<String, String> activityAttributes = new HashMap<String, String>();
        activityAttributes.put(KomaduClientConstants.ACTIVITY_WORKFLOW, "true");
        activityAttributes.put(KomaduClientConstants.WORKFLOW_ID, "test_workflow1");
        activityAttributes.put(KomaduClientConstants.WORKFLOW_NODE_ID, "node1");
        activityAttributes.put("framework", "mpi");
        activityAttributes.put("cluster", "ec2");
        Map<String, String> generationAttributes = new HashMap<String, String>();
        generationAttributes.put("generation_time", "11/20/2015");
        client.addGeneration(entityAttributes, activityAttributes, generationAttributes);
    }

}
