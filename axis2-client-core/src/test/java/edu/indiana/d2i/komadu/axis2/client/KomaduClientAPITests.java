package edu.indiana.d2i.komadu.axis2.client;

import junit.framework.Assert;
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
    private static int runId;

    @BeforeClass
    public static void init() {
        try {
            System.out.println("Initializing Komadu tests...");
            client = new KomaduClient();
            runId = KomaduTests.generateID();
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
        Map<String, String> entity1 = createEntity1();
        Map<String, String> workflow = createWorkflowActivity();
        Map<String, String> agent1 = createAgent1();

        Map<String, String> associationAttributes = new HashMap<String, String>();
        associationAttributes.put("role", "developer");
        client.addAssociation(agent1, workflow, associationAttributes);

        Map<String, String> generationAttributes = new HashMap<String, String>();
        generationAttributes.put("generation_type", "dummy");
        client.addGeneration(entity1, workflow, generationAttributes);

        Map<String, String> entity2 = createEntity2();
        client.addUsage(entity2, workflow, new HashMap<String, String>());

        Map<String, String> service1 = createServiceActivity1();
        client.addCommunication(workflow, service1, new HashMap<String, String>());
        Map<String, String> service2 = createServiceActivity2();
        client.addCommunication(workflow, service2, new HashMap<String, String>());

        Map<String, String> entity3 = createEntity3();
        client.addUsage(entity3, service1, new HashMap<String, String>());

        Map<String, String> entity4 = createEntity4();
        client.addGeneration(entity4, service2, new HashMap<String, String>());

        client.addRevision(entity1, entity4, new HashMap<String, String>());

        try {
            Thread.sleep(5000);
            System.out.println(client.queryActivityGraph("test_workflow1_" + runId));
        } catch (Exception e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    private Map<String, String> createEntity1() {
        Map<String, String> entityAttributes = new HashMap<String, String>();
        entityAttributes.put(KomaduClientConstants.ENTITY_FILE, "true");
        entityAttributes.put(KomaduClientConstants.FILE_URI, "test_file1.text_" + runId);
        entityAttributes.put(KomaduClientConstants.FILE_NAME, "test_file1.text");
        entityAttributes.put(KomaduClientConstants.FILE_SIZE, "200");
        entityAttributes.put("location", "/home/isuru/test_file1.text");
        return entityAttributes;
    }

    private Map<String, String> createEntity2() {
        Map<String, String> entityAttributes = new HashMap<String, String>();
        entityAttributes.put(KomaduClientConstants.ENTITY_FILE, "true");
        entityAttributes.put(KomaduClientConstants.FILE_URI, "test_file2.text_" + runId);
        entityAttributes.put(KomaduClientConstants.FILE_NAME, "test_file2.text");
        entityAttributes.put(KomaduClientConstants.FILE_SIZE, "500");
        entityAttributes.put("location", "/home/isuru/test_file2.text");
        return entityAttributes;
    }

    private Map<String, String> createEntity3() {
        Map<String, String> entityAttributes = new HashMap<String, String>();
        entityAttributes.put(KomaduClientConstants.ENTITY_FILE, "true");
        entityAttributes.put(KomaduClientConstants.FILE_URI, "test_file3.text_" + runId);
        entityAttributes.put(KomaduClientConstants.FILE_NAME, "test_file3.text");
        entityAttributes.put(KomaduClientConstants.FILE_SIZE, "100");
        entityAttributes.put("location", "/home/isuru/test_file3.text");
        return entityAttributes;
    }

    private Map<String, String> createEntity4() {
        Map<String, String> entityAttributes = new HashMap<String, String>();
        entityAttributes.put(KomaduClientConstants.ENTITY_FILE, "true");
        entityAttributes.put(KomaduClientConstants.FILE_URI, "test_file4.text_" + runId);
        entityAttributes.put(KomaduClientConstants.FILE_NAME, "test_file4.text");
        entityAttributes.put(KomaduClientConstants.FILE_SIZE, "500");
        entityAttributes.put("location", "/home/isuru/test_file4.text");
        return entityAttributes;
    }

    private Map<String, String> createWorkflowActivity() {
        Map<String, String> activityAttributes = new HashMap<String, String>();
        activityAttributes.put(KomaduClientConstants.ACTIVITY_WORKFLOW, "true");
        activityAttributes.put(KomaduClientConstants.WORKFLOW_ID, "test_workflow1_" + runId);
        activityAttributes.put(KomaduClientConstants.WORKFLOW_NODE_ID, "node1");
        activityAttributes.put("framework", "mpi");
        activityAttributes.put("cluster", "ec2");
        return activityAttributes;
    }

    private Map<String, String> createServiceActivity1() {
        Map<String, String> serviceAttributes = new HashMap<String, String>();
        serviceAttributes.put(KomaduClientConstants.ACTIVITY_SERVICE, "true");
        serviceAttributes.put(KomaduClientConstants.SERVICE_ID, "test_service1_" + runId);
        serviceAttributes.put(KomaduClientConstants.WORKFLOW_ID, "test_workflow1_" + runId);
        serviceAttributes.put("property", "service_prop1");
        return serviceAttributes;
    }

    private Map<String, String> createServiceActivity2() {
        Map<String, String> serviceAttributes = new HashMap<String, String>();
        serviceAttributes.put(KomaduClientConstants.ACTIVITY_SERVICE, "true");
        serviceAttributes.put(KomaduClientConstants.SERVICE_ID, "test_service2_" + runId);
        serviceAttributes.put(KomaduClientConstants.WORKFLOW_ID, "test_workflow1_" + runId);
        serviceAttributes.put("property", "service_prop2");
        return serviceAttributes;
    }

    private Map<String, String> createAgent1() {
        Map<String, String> agentAttributes = new HashMap<String, String>();
        agentAttributes.put(KomaduClientConstants.AGENT_USER, "true");
        agentAttributes.put(KomaduClientConstants.AGENT_ID, "test_agent1_" + runId);
        agentAttributes.put(KomaduClientConstants.AGENT_FULL_NAME, "Isuru Suriarachchi");
        agentAttributes.put(KomaduClientConstants.AGENT_EMAIL, "isuru@gmail.com");
        agentAttributes.put("organization", "IU");
        return agentAttributes;
    }

}
