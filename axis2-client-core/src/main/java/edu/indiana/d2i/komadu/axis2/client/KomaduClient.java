package edu.indiana.d2i.komadu.axis2.client;

import edu.indiana.d2i.komadu.axis2.client.handler.*;
import edu.indiana.d2i.komadu.query.DetailEnumType;
import edu.indiana.d2i.komadu.query.GetActivityGraphRequestDocument;
import edu.indiana.d2i.komadu.query.GetActivityGraphRequestType;
import edu.indiana.d2i.komadu.query.GetActivityGraphResponseDocument;

import java.io.InputStream;
import java.rmi.RemoteException;
import java.util.Map;
import java.util.Properties;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class KomaduClient {

    private static final int THREAD_POOL_SIZE = 5;
    private final KomaduServiceStub stub;
    private final ExecutorService executor;

    public KomaduClient() throws Exception {
        // Initialize the thread pool to be used to send messages to Komadu
        // server. This makes sure that the application thread is not blocked
        // when doing provenance related activities.
        executor = Executors.newFixedThreadPool(THREAD_POOL_SIZE);

        // read the service URL from client properties file
        Properties prop = new Properties();
        ClassLoader loader = Thread.currentThread().getContextClassLoader();
        InputStream stream = loader.getResourceAsStream("komadu.client.properties");
        prop.load(stream);
        String komaduURL = prop.getProperty("komadu.service.url");
        // create stub
        stub = new KomaduServiceStub(komaduURL);
    }

    public void shutdown() throws InterruptedException {
        executor.shutdown();
        while (!executor.isTerminated()) {
            Thread.sleep(100);
        }
    }

    public void addAssociation(Map<String, String> agentAttributes,
                               Map<String, String> activityAttributes,
                               Map<String, String> associationAttributes) {
        Runnable handler = new AssociationHandler(stub, agentAttributes,
                activityAttributes, associationAttributes);
        executor.execute(handler);
    }

    public void addUsage(Map<String, String> entityAttributes,
                         Map<String, String> activityAttributes,
                         Map<String, String> usageAttributes) {
        Runnable handler = new UsageHandler(stub, entityAttributes,
                activityAttributes, usageAttributes);
        executor.execute(handler);
    }

    public void addGeneration(Map<String, String> entityAttributes,
                              Map<String, String> activityAttributes,
                              Map<String, String> generationAttributes) {
        Runnable handler = new GenerationHandler(stub, entityAttributes,
                activityAttributes, generationAttributes);
        executor.execute(handler);
    }

    public void addStart(Map<String, String> entityAttributes,
                         Map<String, String> activityAttributes,
                         Map<String, String> startAttributes) {
        Runnable handler = new StartHandler(stub, entityAttributes,
                activityAttributes, startAttributes);
        executor.execute(handler);
    }

    public void addEnd(Map<String, String> entityAttributes,
                       Map<String, String> activityAttributes,
                       Map<String, String> endAttributes) {
        Runnable handler = new EndHandler(stub, entityAttributes,
                activityAttributes, endAttributes);
        executor.execute(handler);
    }

    public void addInvalidation(Map<String, String> entityAttributes,
                                Map<String, String> activityAttributes,
                                Map<String, String> invalidationAttributes) {
        Runnable handler = new InvalidationHandler(stub, entityAttributes,
                activityAttributes, invalidationAttributes);
        executor.execute(handler);
    }

    public void addDelegation(Map<String, String> delegateAttributes,
                              Map<String, String> responsibleAttributes,
                              Map<String, String> delegationAttributes) {
        Runnable handler = new DelegationHandler(stub, delegateAttributes,
                responsibleAttributes, delegationAttributes);
        executor.execute(handler);
    }

    public void addAttribution(Map<String, String> entityAttributes,
                               Map<String, String> agentAttributes,
                               Map<String, String> attributionAttributes) {
        Runnable handler = new AttributionHandler(stub, entityAttributes,
                agentAttributes, attributionAttributes);
        executor.execute(handler);
    }

    public void addCommunication(Map<String, String> informantAttributes,
                                 Map<String, String> informedAttributes,
                                 Map<String, String> communicationAttributes) {
        Runnable handler = new CommunicationHandler(stub, informantAttributes,
                informedAttributes, communicationAttributes);
        executor.execute(handler);
    }

    public void addDerivation(Map<String, String> usedAttributes,
                              Map<String, String> generatedAttributes,
                              Map<String, String> derivationAttributes) {
        Runnable handler = new DerivationHandler(stub, KomaduClientConstants.Derivation.DERIVATION,
                usedAttributes, generatedAttributes, derivationAttributes);
        executor.execute(handler);
    }

    public void addRevision(Map<String, String> usedAttributes,
                            Map<String, String> generatedAttributes,
                            Map<String, String> revisionAttributes) {
        Runnable handler = new DerivationHandler(stub, KomaduClientConstants.Derivation.REVISION,
                usedAttributes, generatedAttributes, revisionAttributes);
        executor.execute(handler);
    }

    public void addQuotation(Map<String, String> usedAttributes,
                             Map<String, String> generatedAttributes,
                             Map<String, String> quotationAttributes) {
        Runnable handler = new DerivationHandler(stub, KomaduClientConstants.Derivation.QUOTATION,
                usedAttributes, generatedAttributes, quotationAttributes);
        executor.execute(handler);
    }

    public void addPrimarySource(Map<String, String> usedAttributes,
                                 Map<String, String> generatedAttributes,
                                 Map<String, String> primarySourceAttributes) {
        Runnable handler = new DerivationHandler(stub, KomaduClientConstants.Derivation.PRIMARY_SOURCE,
                usedAttributes, generatedAttributes, primarySourceAttributes);
        executor.execute(handler);
    }

    public void addAlternate(Map<String, String> alt1Attributes,
                             Map<String, String> alt2Attributes) {
        Runnable handler = new AlternateHandler(stub, alt1Attributes, alt2Attributes);
        executor.execute(handler);
    }

    public void addSpecialization(Map<String, String> specificAttributes,
                                  Map<String, String> generalAttributes) {
        Runnable handler = new SpecializationHandler(stub, specificAttributes, generalAttributes);
        executor.execute(handler);
    }

    public String queryActivityGraph(String activityId) throws RemoteException {
        GetActivityGraphRequestDocument activityGraphRequest =
                GetActivityGraphRequestDocument.Factory.newInstance();
        GetActivityGraphRequestType actRequestType =
                GetActivityGraphRequestType.Factory.newInstance();
        actRequestType.setInformationDetailLevel(DetailEnumType.FINE);
        actRequestType.setActivityURI(activityId);
        activityGraphRequest.setGetActivityGraphRequest(actRequestType);
        GetActivityGraphResponseDocument actResponse = stub.getActivityGraph(activityGraphRequest);
        return actResponse.getGetActivityGraphResponse().getDocument().toString();
    }

}
