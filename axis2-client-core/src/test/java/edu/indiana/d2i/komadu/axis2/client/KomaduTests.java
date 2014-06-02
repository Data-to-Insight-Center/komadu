/*
#
# Copyright 2014 The Trustees of Indiana University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
*/

package edu.indiana.d2i.komadu.axis2.client;

import edu.indiana.d2i.komadu.query.*;
import junit.framework.Assert;
import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import java.io.IOException;
import java.io.InputStream;
import java.rmi.RemoteException;
import java.util.Calendar;
import java.util.Properties;
import java.util.Random;

@RunWith(JUnit4.class)
public class KomaduTests {

    private static KomaduServiceStub stub = null;
    private static String workflowGraphId = null;
    private static String agentGraphId = null;
    private static String entityGraphURI = null;
    private static String service1Id = null;

    @BeforeClass
    public static void init() {
        try {
            // read the service URL from client properties file
            Properties prop = new Properties();
            ClassLoader loader = Thread.currentThread().getContextClassLoader();
            InputStream stream = loader.getResourceAsStream("komadu.client.properties");
            prop.load(stream);
            String komaduURL = prop.getProperty("komadu.service.url");
            // create stub
            stub = new KomaduServiceStub(komaduURL);
        } catch (IOException e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    @Test
    public void testContextWorkflowGraph() {
        try {
            // random id for current run
            int runId = generateID();
            /**
             * Agent Agent Relationship Test
             */
            agentGraphId = "agent1_" + runId;
            String agent2Id = "agent2_" + runId;
            AgentType agent1 = createAgent1(agentGraphId);
            AgentType agent2 = createAgent2(agent2Id);
            testDelegation(stub, agent1, agent2, agentGraphId, agent2Id);

            /**
             * Agent Activity Relationship Test
             */
            workflowGraphId = "workflow1_" + runId;
            String workflow2Id = "workflow2_" + runId;
            service1Id = "service1_" + runId;
            String method1Id = "method1_" + runId;
            ActivityType workflowActivity = createWorkflowActivity(workflowGraphId);
            ActivityType workflow2Activity = createWorkflowActivity(workflow2Id);
            ActivityType serviceActivity = createServiceActivity(workflowGraphId, service1Id);
            ActivityType methodActivity = createMethodActivity(workflowGraphId, service1Id, method1Id);

            testAssociation(stub, agent1, workflowActivity, agentGraphId, workflowGraphId);
            testAssociation(stub, agent2, serviceActivity, agent2Id, service1Id);
            testAssociation(stub, agent1, methodActivity, agentGraphId, method1Id);

            /**
             * Activity Entity Relationship Test
             */
            entityGraphURI = "file://foo/bar/data1.txt_" + runId;
            String file2URI = "file://foo/bar/data2.txt_" + runId;
            String file3URI = "file://foo/bar/data3.txt_" + runId;
            String file4URI = "file://foo/bar/data4.txt_" + runId;
            EntityType usedEntity = createFileEntity(entityGraphURI);
            EntityType generatedEntity = createFileEntity(file2URI);
            EntityType startEntity = createFileEntity(file3URI);
            EntityType endEntity = createFileEntity(file4URI);

            testUsage(stub, serviceActivity, usedEntity, service1Id, entityGraphURI);
            testGeneration(stub, workflowActivity, generatedEntity, workflowGraphId, file2URI);
            testStart(stub, workflow2Activity, startEntity, workflow2Id, file3URI);
            testEnd(stub, workflow2Activity, endEntity, workflow2Id, file4URI);
            testInvalidation(stub, serviceActivity, generatedEntity, service1Id, file2URI);

            // create collection entity
            String coll1URI = "collection1_" + runId;
            EntityType collEntity = createCollectionEntity(coll1URI, runId);
            testUsage(stub, workflow2Activity, collEntity, workflow2Id, coll1URI);

            String coll2URI = "collection2_" + runId;
            EntityType coll2Entity = createCollectionEntity(coll2URI, runId);
            testGeneration(stub, workflowActivity, coll2Entity, workflowGraphId, coll2URI);

            /**
             * Agent Entity Relationship Test
             */
            testAttribution(stub, agent1, generatedEntity, agentGraphId, file2URI);

            /**
             * Activity Activity Relationship Test
             */
            testCommunication(stub, workflowActivity, serviceActivity, workflowGraphId, service1Id);
            testCommunication(stub, workflowActivity, workflow2Activity, workflowGraphId, workflow2Id);

            /**
             * Entity Entity Relationship Test
             */
            String file5URI = "file://foo/bar/data5.txt_" + runId;
            EntityType derivationEntity = createFileEntity(file5URI);
            // derivation through activity test
            testGeneration(stub, serviceActivity, derivationEntity, service1Id, file5URI);
            // direct derivation
            String file6URI = "file://foo/bar/data6.txt_" + runId;
            EntityType e6 = createFileEntity(file6URI);
            testDerivation(stub, generatedEntity, e6, file2URI, file6URI);
            // revision
            String file7URI = "file://foo/bar/data7.txt_" + runId;
            EntityType e7 = createFileEntity(file7URI);
            testRevision(stub, e6, e7, file6URI, file7URI);
            // quotation
            String file8URI = "file://foo/bar/data8.txt_" + runId;
            EntityType e8 = createFileEntity(file8URI);
            testQuotation(stub, e6, e8, file6URI, file8URI);
            // primary source
            String file9URI = "file://foo/bar/data9.txt_" + runId;
            EntityType e9 = createFileEntity(file9URI);
            testPrimarySource(stub, e6, e9, file6URI, file9URI);
            // alternate
            String file10URI = "file://foo/bar/data10.txt_" + runId;
            EntityType e10 = createFileEntity(file10URI);
            testAlternate(stub, e6, e10, file6URI, file10URI);
            // specialization
            String file11URI = "file://foo/bar/data11.txt_" + runId;
            EntityType e11 = createFileEntity(file11URI);
            testSpecialization(stub, e6, e11, file6URI, file11URI);
            // membership
            String file12URI = "file://foo/bar/data12.txt_" + runId;
            EntityType e12 = createFileEntity(file12URI);
            testMembership(stub, collEntity, e12, coll1URI, file12URI);

            String file13URI = "file://foo/bar/data13.txt_" + runId;
            EntityType e13 = createFileEntity(file13URI);
            testMembership(stub, coll2Entity, e13, coll2URI, file13URI);

            // revision between collection entities
            testRevision(stub, collEntity, coll2Entity, coll1URI, coll2URI);

            // Add attributes test
            testAddActivityAttributes();
            testAddEntityAttributes();

            System.out.println("Giving 5 seconds for processing of notifications...");
            Thread.sleep(5000);
            System.out.println("Resuming...");

            System.out.println("\n\n Context workflow graph \n\n");

            GetContextWorkflowGraphRequestDocument workflowRequest = GetContextWorkflowGraphRequestDocument.Factory.newInstance();
            GetContextWorkflowGraphRequestType requestType = GetContextWorkflowGraphRequestType.Factory.newInstance();
            requestType.setInformationDetailLevel(DetailEnumType.FINE);
            requestType.setContextWorkflowURI(workflowGraphId);
            workflowRequest.setGetContextWorkflowGraphRequest(requestType);
            GetContextWorkflowGraphResponseDocument response = stub.getContextWorkflowGraph(workflowRequest);
            System.out.println(response.getGetContextWorkflowGraphResponse().getDocument());

        } catch (Exception e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    @Test
    public void testActivityGraph() {
        try {
            System.out.println("\n\n Activity Graph without context \n\n");
            GetActivityGraphRequestDocument activityGraphRequest = GetActivityGraphRequestDocument.Factory.newInstance();
            GetActivityGraphRequestType actRequestType = GetActivityGraphRequestType.Factory.newInstance();
            actRequestType.setInformationDetailLevel(DetailEnumType.FINE);
            actRequestType.setActivityURI(workflowGraphId);
            activityGraphRequest.setGetActivityGraphRequest(actRequestType);
            GetActivityGraphResponseDocument actResponse = stub.getActivityGraph(activityGraphRequest);
            System.out.println(actResponse.getGetActivityGraphResponse().getDocument());
        } catch (RemoteException e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    @Test
    public void testAgentGraph() {
        try {
            System.out.println("\n\n Agent Graph without context \n\n");
            GetAgentGraphRequestDocument agentGraphRequest = GetAgentGraphRequestDocument.Factory.newInstance();
            GetAgentGraphRequestType agentRequestType = GetAgentGraphRequestType.Factory.newInstance();
            agentRequestType.setInformationDetailLevel(DetailEnumType.FINE);
            agentRequestType.setAgentID(agentGraphId);
            agentGraphRequest.setGetAgentGraphRequest(agentRequestType);
            GetAgentGraphResponseDocument agentResponse = stub.getAgentGraph(agentGraphRequest);
            System.out.println(agentResponse.getGetAgentGraphResponse().getDocument());
        } catch (RemoteException e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    @Test
    public void testEntityGraph() {
        try {
            System.out.println("\n\n Entity Graph without context \n\n");
            GetEntityGraphRequestDocument entityGraphRequest = GetEntityGraphRequestDocument.Factory.newInstance();
            GetEntityGraphRequestType entityRequestType = GetEntityGraphRequestType.Factory.newInstance();
            entityRequestType.setInformationDetailLevel(DetailEnumType.FINE);
            entityRequestType.setEntityURI(entityGraphURI);
            entityRequestType.setEntityType(edu.indiana.d2i.komadu.query.EntityEnumType.FILE);
            entityGraphRequest.setGetEntityGraphRequest(entityRequestType);
            GetEntityGraphResponseDocument entityResponse = stub.getEntityGraph(entityGraphRequest);
            System.out.println(entityResponse.getGetEntityGraphResponse().getDocument());
        } catch (RemoteException e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    @Test
    public void testFindActivity() {
        try {
            System.out.println("\n\n Find Activity \n\n");
            FindActivityRequestDocument findActivityRequest = FindActivityRequestDocument.Factory.newInstance();
            FindActivityRequestType findActivityRequestType = FindActivityRequestType.Factory.newInstance();
            findActivityRequestType.setName("workflow1");
            findActivityRequestType.setNextActivityID(service1Id);
            findActivityRequest.setFindActivityRequest(findActivityRequestType);
            FindActivityResponseDocument responseDocument = stub.findActivity(findActivityRequest);
            String[] activityIDArray = responseDocument.getFindActivityResponse().getActivityIDList().getActivityIDArray();
            for (String id : activityIDArray) {
                System.out.println("Found Activity: " + id);
            }
        } catch (RemoteException e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    @Test
    public void testGetActivityDetail() {
        try {
            System.out.println("\n\n Get Activity Detail \n\n");
            GetActivityDetailRequestDocument getActivityDetailRequestDocument =
                    GetActivityDetailRequestDocument.Factory.newInstance();
            GetActivityDetailRequestType getActivityDetailRequestType = GetActivityDetailRequestType.Factory.newInstance();
            UniqueURIListType uniqueURIListType = UniqueURIListType.Factory.newInstance();
            uniqueURIListType.setUniqueURIArray(new String[]{workflowGraphId});
            getActivityDetailRequestType.setUniqueURIList(uniqueURIListType);
            getActivityDetailRequestDocument.setGetActivityDetailRequest(getActivityDetailRequestType);
            GetActivityDetailResponseDocument responseDocument = stub.getActivityDetail(getActivityDetailRequestDocument);
            ActivityDetailListType list = responseDocument.getGetActivityDetailResponse().getActivityDetailList();
            for (ActivityDetail detail : list.getActivityDetailArray()) {
                System.out.println("Activity ID: " + detail.getId());
                System.out.println("Activity Type: " + detail.getType());
                System.out.println("Activity Context Service ID: " + detail.getServiceID());
                System.out.println("Activity Timestep: " + detail.getTimestep());
                System.out.println("Activity Context Workflow ID: " + detail.getWorkflowID());
                System.out.println("Activity Node ID: " + detail.getWorkflowNodeID());
                System.out.println("Activity Instance Of: " + detail.getInstanceOf());
            }
        } catch (RemoteException e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    @Test
    public void testFindEntityAndDetail() {
        try {
            System.out.println("\n\n Find Entity \n\n");
            FindEntityRequestDocument findEntityRequest = FindEntityRequestDocument.Factory.newInstance();
            FindEntityRequestType findEntityRequestType = FindEntityRequestType.Factory.newInstance();
            findEntityRequestType.setFileSize(500);
            findEntityRequestType.setFileName(getFileName(entityGraphURI));
            findEntityRequestType.setFileOwnerID("jerry112");
            findEntityRequest.setFindEntityRequest(findEntityRequestType);
            FindEntityResponseDocument responseDocument = stub.findEntity(findEntityRequest);
            UniqueFileListType fileList = responseDocument.getFindEntityResponse().getUniqueFileURIList();
            String fileIdForDetail = null;
            for (FileURIDetailsType uriDetail : fileList.getFileURIDetailsTypeArray()) {
                System.out.println("Found File Entity");
                System.out.println("File URI : " + uriDetail.getFileURI());
                System.out.println("File ID : " + uriDetail.getFileID());
                fileIdForDetail = uriDetail.getFileID();
                System.out.println("File Creation Date : " + uriDetail.getCreationDate());
            }
            
            // getEntityDetail Test
            if (fileIdForDetail != null) {
                System.out.println("\n\n Get Entity Detail \n\n");
                GetEntityDetailRequestDocument getEntityDetailRequestDocument =
                        GetEntityDetailRequestDocument.Factory.newInstance();
                GetEntityDetailRequestType getEntityDetailRequestType = GetEntityDetailRequestType.Factory.newInstance();
                EntityIDListType idList = EntityIDListType.Factory.newInstance();
                idList.setEntityIDArray(new String[]{fileIdForDetail});
                getEntityDetailRequestType.setEntityIDList(idList);
                getEntityDetailRequestDocument.setGetEntityDetailRequest(getEntityDetailRequestType);
                GetEntityDetailResponseDocument detailResponseDocument = stub.getEntityDetail(getEntityDetailRequestDocument);
                EntityDetailListType list = detailResponseDocument.getGetEntityDetailResponse().getEntityDetailList();
                for (EntityDetail detail : list.getEntityDetailArray()) {
                    System.out.println("Entity ID: " + detail.getId());
                    System.out.println("File Name: " + detail.getFileName());
                    System.out.println("File URI: " + detail.getFileURI());
                    System.out.println("File Creation Date: " + detail.getCreationDate());
                    System.out.println("File Owner: " + detail.getOwner());
                    System.out.println("File MD5: " + detail.getMd5());
                }
            }
        } catch (RemoteException e) {
            e.printStackTrace();
            Assert.fail();
        }
    }

    private static int generateID() {
        Random num = new Random();
        return num.nextInt(10000);
    }

    private static void testAddActivityAttributes() throws Exception {
        AddAttributesDocument addAttributesDoc = AddAttributesDocument.Factory.newInstance();
        AddAttributesType addAttributesType = AddAttributesType.Factory.newInstance();
        addAttributesType.setObjectType(ObjectEnumType.ACTIVITY);
        addAttributesType.setObjectID(workflowGraphId);
        addAttributesType.setAddAttributeTimestamp(Calendar.getInstance());
        addAttributesType.setNotificationTimestamp(Calendar.getInstance());
        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[3];
        // Attribute 1
        AttributeType att1 = createAttribute("new_att_1", "new_val_1");
        attributesArr[0] = att1;
        // Attribute 2
        AttributeType att2 = createAttribute("new_att_2", "new_val_2");
        attributesArr[1] = att2;
        // Attribute 3
        AttributeType att3 = createAttribute("new_att_3", "new_val_3");
        attributesArr[2] = att3;
        attributes.setAttributeArray(attributesArr);
        addAttributesType.setAttributes(attributes);
        addAttributesDoc.setAddAttributes(addAttributesType);
        stub.addAttributes(addAttributesDoc);
    }

    private static void testAddEntityAttributes() throws Exception {
        AddAttributesDocument addAttributesDoc = AddAttributesDocument.Factory.newInstance();
        AddAttributesType addAttributesType = AddAttributesType.Factory.newInstance();
        addAttributesType.setObjectType(ObjectEnumType.ENTITY);
        addAttributesType.setEntityType(EntityEnumType.FILE);
        addAttributesType.setObjectID(entityGraphURI);
        addAttributesType.setAddAttributeTimestamp(Calendar.getInstance());
        addAttributesType.setNotificationTimestamp(Calendar.getInstance());
        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[3];
        // Attribute 1
        AttributeType att1 = createAttribute("new_entity_att_1", "new_val_1");
        attributesArr[0] = att1;
        // Attribute 2
        AttributeType att2 = createAttribute("new_entity_att_2", "new_val_2");
        attributesArr[1] = att2;
        // Attribute 3
        AttributeType att3 = createAttribute("new_entity_att_3", "new_val_3");
        attributesArr[2] = att3;
        attributes.setAttributeArray(attributesArr);
        addAttributesType.setAttributes(attributes);
        addAttributesDoc.setAddAttributes(addAttributesType);
        stub.addAttributes(addAttributesDoc);
    }

    private static void testAssociation(KomaduServiceStub stub, AgentType agent, ActivityType activity,
                                        String agentId, String activityId) throws Exception {
        AddAgentActivityRelationshipDocument agentActivity = AddAgentActivityRelationshipDocument.Factory.newInstance();
        AgentActivityType agentActivityType = AgentActivityType.Factory.newInstance();

        AssociationType association1 = createAssociation1(agentId, activityId);
        agentActivityType.setActivity(activity);
        agentActivityType.setAgent(agent);
        agentActivityType.setAssociation(association1);
        // execute
        agentActivity.setAddAgentActivityRelationship(agentActivityType);
        stub.addAgentActivityRelationship(agentActivity);
    }

    private static void testAttribution(KomaduServiceStub stub, AgentType agent, EntityType entity,
                                        String agentId, String entityId) throws Exception {
        AddAgentEntityRelationshipDocument activityEntity = AddAgentEntityRelationshipDocument.Factory.newInstance();
        AgentEntityType agentEntityType = AgentEntityType.Factory.newInstance();

        AttributionType attribution = AttributionType.Factory.newInstance();
        attribution.setAgentID(agentId);
        attribution.setEntityID(entityId);

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_att", "attribution_att");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        attribution.setAttributes(attributes);

        agentEntityType.setAgent(agent);
        agentEntityType.setEntity(entity);
        agentEntityType.setAttribution(attribution);
        activityEntity.setAddAgentEntityRelationship(agentEntityType);
        // invoke
        stub.addAgentEntityRelationship(activityEntity);
    }

    private static void testCommunication(KomaduServiceStub stub, ActivityType activity1, ActivityType activity2,
                                          String activity1Id, String activity2Id) throws Exception {
        AddActivityActivityRelationshipDocument activityActivity = AddActivityActivityRelationshipDocument.Factory.newInstance();
        ActivityActivityType activityActivityType = ActivityActivityType.Factory.newInstance();

        CommunicationType communication = CommunicationType.Factory.newInstance();
        communication.setInformantActivityID(activity1Id);
        communication.setInformedActivityID(activity2Id);

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_att", "communication_att");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        communication.setAttributes(attributes);

        activityActivityType.setActivity1(activity1);
        activityActivityType.setActivity2(activity2);
        activityActivityType.setCommunication(communication);
        activityActivity.setAddActivityActivityRelationship(activityActivityType);
        // invoke
        stub.addActivityActivityRelationship(activityActivity);
    }

    private static void testUsage(KomaduServiceStub stub, ActivityType activity, EntityType entity,
                                  String activityId, String entityId) throws Exception {
        AddActivityEntityRelationshipDocument activityEntity = AddActivityEntityRelationshipDocument.Factory.newInstance();
        ActivityEntityType activityEntityType = ActivityEntityType.Factory.newInstance();

        UsageType usage = UsageType.Factory.newInstance();
        usage.setActivityID(activityId);
        usage.setEntityID(entityId);
        usage.setLocation("Location2");
        usage.setTimestamp(Calendar.getInstance());

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("total_time", "0.53h");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        usage.setAttributes(attributes);

        activityEntityType.setActivity(activity);
        activityEntityType.setEntity(entity);
        activityEntityType.setUsage(usage);
        activityEntity.setAddActivityEntityRelationship(activityEntityType);
        // invoke
        stub.addActivityEntityRelationship(activityEntity);
    }

    private static void testGeneration(KomaduServiceStub stub, ActivityType activity, EntityType entity,
                                       String activityId, String entityId) throws Exception {
        AddActivityEntityRelationshipDocument activityEntity = AddActivityEntityRelationshipDocument.Factory.newInstance();
        ActivityEntityType activityEntityType = ActivityEntityType.Factory.newInstance();

        GenerationType generation = GenerationType.Factory.newInstance();
        generation.setActivityID(activityId);
        generation.setEntityID(entityId);
        generation.setLocation("Location1");
        generation.setTimestamp(Calendar.getInstance());

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("total_time", "1.23h");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        generation.setAttributes(attributes);

        activityEntityType.setActivity(activity);
        activityEntityType.setEntity(entity);
        activityEntityType.setGeneration(generation);
        activityEntity.setAddActivityEntityRelationship(activityEntityType);
        // invoke
        stub.addActivityEntityRelationship(activityEntity);
    }

    private static void testStart(KomaduServiceStub stub, ActivityType activity, EntityType entity,
                                  String activityId, String entityId) throws Exception {
        AddActivityEntityRelationshipDocument activityEntity = AddActivityEntityRelationshipDocument.Factory.newInstance();
        ActivityEntityType activityEntityType = ActivityEntityType.Factory.newInstance();

        StartType start = StartType.Factory.newInstance();
        start.setActivityID(activityId);
        start.setTriggerID(entityId);
        start.setLocation("Location2");
        start.setTimestamp(Calendar.getInstance());

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy", "dummy_val");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        start.setAttributes(attributes);

        activityEntityType.setActivity(activity);
        activityEntityType.setEntity(entity);
        activityEntityType.setStart(start);
        activityEntity.setAddActivityEntityRelationship(activityEntityType);
        // invoke
        stub.addActivityEntityRelationship(activityEntity);
    }

    private static void testEnd(KomaduServiceStub stub, ActivityType activity, EntityType entity,
                                String activityId, String entityId) throws Exception {
        AddActivityEntityRelationshipDocument activityEntity = AddActivityEntityRelationshipDocument.Factory.newInstance();
        ActivityEntityType activityEntityType = ActivityEntityType.Factory.newInstance();

        EndType end = EndType.Factory.newInstance();
        end.setActivityID(activityId);
        end.setTriggerID(entityId);
        end.setLocation("Location3");
        end.setTimestamp(Calendar.getInstance());

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_end_att", "dummy_val_end");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        end.setAttributes(attributes);

        activityEntityType.setActivity(activity);
        activityEntityType.setEntity(entity);
        activityEntityType.setEnd(end);
        activityEntity.setAddActivityEntityRelationship(activityEntityType);
        // invoke
        stub.addActivityEntityRelationship(activityEntity);
    }

    private static void testInvalidation(KomaduServiceStub stub, ActivityType activity, EntityType entity,
                                String activityId, String entityId) throws Exception {
        AddActivityEntityRelationshipDocument activityEntity = AddActivityEntityRelationshipDocument.Factory.newInstance();
        ActivityEntityType activityEntityType = ActivityEntityType.Factory.newInstance();

        InvalidationType invalidation = InvalidationType.Factory.newInstance();
        invalidation.setActivityID(activityId);
        invalidation.setEntityID(entityId);
        invalidation.setLocation("Location4");
        invalidation.setTimestamp(Calendar.getInstance());

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_invalidation_att", "dummy_val_invalidation");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        invalidation.setAttributes(attributes);

        activityEntityType.setActivity(activity);
        activityEntityType.setEntity(entity);
        activityEntityType.setInvalidation(invalidation);
        activityEntity.setAddActivityEntityRelationship(activityEntityType);
        // invoke
        stub.addActivityEntityRelationship(activityEntity);
    }

    private static void testDerivation(KomaduServiceStub stub, EntityType usedEntity, EntityType generatedEntity,
                                       String usedId, String generatedId) throws Exception {
        AddEntityEntityRelationshipDocument activityEntity = AddEntityEntityRelationshipDocument.Factory.newInstance();
        EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

        DerivationType derivation = DerivationType.Factory.newInstance();
        derivation.setUsedEntityID(usedId);
        derivation.setGeneratedEntityID(generatedId);

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_derivation", "dummy_val");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        derivation.setAttributes(attributes);

        entityEntityType.setEntity1(usedEntity);
        entityEntityType.setEntity2(generatedEntity);
        entityEntityType.setDerivation(derivation);
        activityEntity.setAddEntityEntityRelationship(entityEntityType);
        // invoke
        stub.addEntityEntityRelationship(activityEntity);
    }

    private static void testRevision(KomaduServiceStub stub, EntityType usedEntity, EntityType generatedEntity,
                                       String usedId, String generatedId) throws Exception {
        AddEntityEntityRelationshipDocument activityEntity = AddEntityEntityRelationshipDocument.Factory.newInstance();
        EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

        RevisionType revision = RevisionType.Factory.newInstance();
        revision.setUsedEntityID(usedId);
        revision.setGeneratedEntityID(generatedId);

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_revision", "dummy_val");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        revision.setAttributes(attributes);

        entityEntityType.setEntity1(usedEntity);
        entityEntityType.setEntity2(generatedEntity);
        entityEntityType.setRevision(revision);
        activityEntity.setAddEntityEntityRelationship(entityEntityType);
        // invoke
        stub.addEntityEntityRelationship(activityEntity);
    }

    private static void testQuotation(KomaduServiceStub stub, EntityType usedEntity, EntityType generatedEntity,
                                       String usedId, String generatedId) throws Exception {
        AddEntityEntityRelationshipDocument activityEntity = AddEntityEntityRelationshipDocument.Factory.newInstance();
        EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

        QuotationType quotation = QuotationType.Factory.newInstance();
        quotation.setUsedEntityID(usedId);
        quotation.setGeneratedEntityID(generatedId);

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_quotation", "dummy_val");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        quotation.setAttributes(attributes);

        entityEntityType.setEntity1(usedEntity);
        entityEntityType.setEntity2(generatedEntity);
        entityEntityType.setQuotation(quotation);
        activityEntity.setAddEntityEntityRelationship(entityEntityType);
        // invoke
        stub.addEntityEntityRelationship(activityEntity);
    }

    private static void testPrimarySource(KomaduServiceStub stub, EntityType usedEntity, EntityType generatedEntity,
                                       String usedId, String generatedId) throws Exception {
        AddEntityEntityRelationshipDocument activityEntity = AddEntityEntityRelationshipDocument.Factory.newInstance();
        EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

        PrimarySourceType derivation = PrimarySourceType.Factory.newInstance();
        derivation.setUsedEntityID(usedId);
        derivation.setGeneratedEntityID(generatedId);

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("dummy_derivation", "dummy_val");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        derivation.setAttributes(attributes);

        entityEntityType.setEntity1(usedEntity);
        entityEntityType.setEntity2(generatedEntity);
        entityEntityType.setPrimarySource(derivation);
        activityEntity.setAddEntityEntityRelationship(entityEntityType);
        // invoke
        stub.addEntityEntityRelationship(activityEntity);
    }

    private static void testAlternate(KomaduServiceStub stub, EntityType alt1Entity, EntityType alt2Entity,
                                      String alt1Id, String alt2Id) throws Exception {
        AddEntityEntityRelationshipDocument activityEntity = AddEntityEntityRelationshipDocument.Factory.newInstance();
        EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

        AlternateType alternate = AlternateType.Factory.newInstance();
        alternate.setAlternate1ID(alt1Id);
        alternate.setAlternate2ID(alt2Id);

        entityEntityType.setEntity1(alt1Entity);
        entityEntityType.setEntity2(alt2Entity);
        entityEntityType.setAlternate(alternate);
        activityEntity.setAddEntityEntityRelationship(entityEntityType);
        // invoke
        stub.addEntityEntityRelationship(activityEntity);
    }

    private static void testSpecialization(KomaduServiceStub stub, EntityType specificEntity, EntityType generalEntity,
                                           String specificId, String generalId) throws Exception {
        AddEntityEntityRelationshipDocument activityEntity = AddEntityEntityRelationshipDocument.Factory.newInstance();
        EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

        SpecializationType specialization = SpecializationType.Factory.newInstance();
        specialization.setSpecificEntityID(specificId);
        specialization.setGeneralEntityID(generalId);

        entityEntityType.setEntity1(specificEntity);
        entityEntityType.setEntity2(generalEntity);
        entityEntityType.setSpecialization(specialization);
        activityEntity.setAddEntityEntityRelationship(entityEntityType);
        // invoke
        stub.addEntityEntityRelationship(activityEntity);
    }

    private static void testMembership(KomaduServiceStub stub, EntityType collection, EntityType memberEntity,
                                       String collectionId, String entityId) throws Exception {
        AddEntityEntityRelationshipDocument activityEntity = AddEntityEntityRelationshipDocument.Factory.newInstance();
        EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

        MembershipType membership = MembershipType.Factory.newInstance();
        membership.setCollectionID(collectionId);
        membership.setEntityID(entityId);

        entityEntityType.setEntity1(collection);
        entityEntityType.setEntity2(memberEntity);
        entityEntityType.setMembership(membership);
        activityEntity.setAddEntityEntityRelationship(entityEntityType);
        // invoke
        stub.addEntityEntityRelationship(activityEntity);
    }

    private static void testDelegation(KomaduServiceStub stub, AgentType agent1, AgentType agent2,
                                       String agent1Id, String agent2Id) throws Exception {
        AddAgentAgentRelationshipDocument agentAgent = AddAgentAgentRelationshipDocument.Factory.newInstance();
        AgentAgentType agentAgentType = AgentAgentType.Factory.newInstance();
        // Delegate agent
        agentAgentType.setDelegateAgent(agent1);
        // Responsible agent
        agentAgentType.setResponsibleAgent(agent2);
        // Delegation
        DelegationType delegation = createDelegation1(agent1Id, agent2Id);
        agentAgentType.setDelegation(delegation);

        agentAgent.setAddAgentAgentRelationship(agentAgentType);
        // execute
        stub.addAgentAgentRelationship(agentAgent);
    }

    private static AssociationType createAssociation1(String agentId, String activityId) throws Exception {
        AssociationType association = AssociationType.Factory.newInstance();
        association.setAgentID(agentId);
        association.setActivityID(activityId);
        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("programmer", "brian");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        association.setAttributes(attributes);
        return association;
    }

    private static EntityType createFileEntity(String fileURI) throws Exception {
        EntityType entity = EntityType.Factory.newInstance();
        FileType file = FileType.Factory.newInstance();
        String fileName = getFileName(fileURI);
        file.setFileName(fileName);
        file.setFileURI(fileURI);
        file.setCreateDate(Calendar.getInstance());
        file.setMd5Sum("dummy_md5_" + fileName);
        file.setOwnerDN("jerry112");
        file.setSize(500);

        entity.setFile(file);
        return entity;
    }

    private static EntityType createCollectionEntity(String collectionURI, int runId) throws Exception {
        EntityType entity = EntityType.Factory.newInstance();
        CollectionType collection = CollectionType.Factory.newInstance();
        collection.setCollectionURI(collectionURI);
        // add a file
        String collFile1URI = "file://foo/bar/coll_data1.txt_" + runId;
        EntityType collEntity1 = createFileEntity(collFile1URI);
        MembersType members = MembersType.Factory.newInstance();
        EntityType[] memberArray = new EntityType[]{collEntity1};
        members.setMemberArray(memberArray);
        collection.setMembers(members);
        entity.setCollection(collection);

        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("coll_attribute", "coll_att_val");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        entity.setAttributes(attributes);

        return entity;
    }

    private static String getFileName(String fileURI) {
        return fileURI.substring(fileURI.lastIndexOf('/') + 1);
    }

    private static ActivityType createWorkflowActivity(String workflowId) throws Exception {
        ActivityType activity = ActivityType.Factory.newInstance();
        WorkflowInformationType workflow = WorkflowInformationType.Factory.newInstance();
        workflow.setWorkflowID(workflowId);
        workflow.setWorkflowNodeID("node1");
        workflow.setTimestep(20);
        // Instance of
        InstanceOfType instanceOf = InstanceOfType.Factory.newInstance();
        instanceOf.setInstanceOfID("slosh_workflow");
        instanceOf.setVersion("1.0.0");
        instanceOf.setCreationTime(Calendar.getInstance());
        workflow.setInstanceOf(instanceOf);
        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("domain", "scientific");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        workflow.setAttributes(attributes);

        activity.setWorkflowInformation(workflow);
        activity.setLocation("Azure");
        return activity;
    }

    private static ActivityType createServiceActivity(String workflowId, String serviceId) throws Exception {
        ActivityType activity = ActivityType.Factory.newInstance();
        ServiceInformationType service = ServiceInformationType.Factory.newInstance();
        service.setWorkflowID(workflowId);
        service.setWorkflowNodeID("node1");
        service.setServiceID(serviceId);
        service.setTimestep(20);
        // Instance of
        InstanceOfType instanceOf = InstanceOfType.Factory.newInstance();
        instanceOf.setInstanceOfID("slosh_workflow");
        instanceOf.setVersion("1.0.0");
        instanceOf.setCreationTime(Calendar.getInstance());
        service.setInstanceOf(instanceOf);
        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("domain", "scientific");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        service.setAttributes(attributes);

        activity.setServiceInformation(service);
        activity.setLocation("Azure");
        return activity;
    }

    private static ActivityType createMethodActivity(String workflowId, String serviceId, String methodId) throws Exception {
        ActivityType activity = ActivityType.Factory.newInstance();
        MethodInformationType method = MethodInformationType.Factory.newInstance();
        method.setWorkflowID(workflowId);
        method.setWorkflowNodeID("node1");
        method.setServiceID(serviceId);
        method.setMethodID(methodId);
        method.setTimestep(20);
        // Instance of
        InstanceOfType instanceOf = InstanceOfType.Factory.newInstance();
        instanceOf.setInstanceOfID("slosh_workflow");
        instanceOf.setVersion("1.0.0");
        instanceOf.setCreationTime(Calendar.getInstance());
        method.setInstanceOf(instanceOf);
        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[1];
        // Attribute 1
        AttributeType att1 = createAttribute("domain", "scientific");
        attributesArr[0] = att1;
        attributes.setAttributeArray(attributesArr);
        method.setAttributes(attributes);

        activity.setMethodInformation(method);
        activity.setLocation("Azure");
        return activity;
    }

    private static AgentType createAgent1(String agentId) throws Exception {
        // Delegate Agent
        AgentType agent = AgentType.Factory.newInstance();
        // User Agent
        UserAgentType userAgent = createUserAgent("Isuru Suriarachchi", "testaff", "isuriara@indiana.edu", agentId);
        // Attributes
        AttributesType attributes = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr = new AttributeType[2];
        // Attribute 1
        AttributeType att1 = createAttribute("phone", "8123334455");
        attributesArr[0] = att1;
        // Attribute 2
        AttributeType att2 = createAttribute("address", "10th Street, Bloomington, IN, 47408");
        attributesArr[1] = att2;
        attributes.setAttributeArray(attributesArr);

        userAgent.setAttributes(attributes);
        agent.setUserAgent(userAgent);
        agent.setType(AgentEnumType.PERSON);
        return agent;
    }

    private static AgentType createAgent2(String agentId) throws Exception {
        // Responsible Agent
        AgentType agent = AgentType.Factory.newInstance();
        // User Agent
        UserAgentType userAgent2 = createUserAgent("John Fraser", "testaff2", "john@indiana.edu", agentId);
        // Attributes
        AttributesType attributes2 = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr2 = new AttributeType[2];
        // Attribute 1
        AttributeType att3 = createAttribute("phone", "8123337788");
        attributesArr2[0] = att3;
        // Attribute 2
        AttributeType att4 = createAttribute("address", "15th Street, Bloomington, IN, 47408");
        attributesArr2[1] = att4;
        attributes2.setAttributeArray(attributesArr2);

        userAgent2.setAttributes(attributes2);
        agent.setUserAgent(userAgent2);
        agent.setType(AgentEnumType.PERSON);
        return agent;
    }

    private static DelegationType createDelegation1(String agent1Id, String agent2Id) throws Exception {
        // Delegation
        DelegationType delegation = createDelegation(agent1Id, agent2Id);

        AttributesType attributes3 = AttributesType.Factory.newInstance();
        AttributeType[] attributesArr3 = new AttributeType[1];
        // Attribute 1
        AttributeType att5 = createAttribute("type", "contract");
        attributesArr3[0] = att5;
        attributes3.setAttributeArray(attributesArr3);
        delegation.setAttributes(attributes3);
        return delegation;
    }

    private static UserAgentType createUserAgent(String name, String aff, String email, String id) {
        UserAgentType userAgent = UserAgentType.Factory.newInstance();
        userAgent.setFullName(name);
        userAgent.setAffiliation(aff);
        userAgent.setEmail(email);
        userAgent.setAgentID(id);
        return userAgent;
    }

    private static AttributeType createAttribute(String name, String val) throws Exception {
        AttributeType att = AttributeType.Factory.newInstance();
        att.setProperty(name);
        att.setValue(val);
        return att;
    }

    private static DelegationType createDelegation(String del, String res) {
        DelegationType delegation = DelegationType.Factory.newInstance();
        delegation.setDelegateAgentID(del);
        delegation.setResponsibleAgentID(res);
        return delegation;
    }

}
