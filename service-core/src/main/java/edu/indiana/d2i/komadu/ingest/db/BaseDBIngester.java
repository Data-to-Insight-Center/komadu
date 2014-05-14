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

package edu.indiana.d2i.komadu.ingest.db;

import edu.indiana.d2i.komadu.ingest.NotificationIngester;
import edu.indiana.d2i.komadu.ingest.IngesterImplementer;
import edu.indiana.d2i.komadu.ingest.IngestException;
import edu.indiana.d2i.komadu.ingest.StoredRawNotification;
import edu.indiana.d2i.komadu.ingest.IngesterConstants;
import edu.indiana.d2i.komadu.ingest.IngesterConstants.ProcessingStatus;
import edu.indiana.d2i.komadu.ingest.IngesterConstants.ProcessingFilterType;
import edu.indiana.d2i.komadu.ingest.NotificationSummary.NotificationTypeEnum;
import edu.indiana.d2i.komadu.service.*;
import org.apache.log4j.Logger;
import org.apache.xmlbeans.XmlError;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;
import org.apache.xmlbeans.XmlValidationError;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

public class BaseDBIngester implements NotificationIngester {

    public static final int DEFAULT_RAW_NOTIFICATION_PROCESS_BATCH_SIZE = 10;

    protected static Logger log = Logger.getLogger(BaseDBIngester.class);
    protected int processingBatchSize;

    protected IngesterImplementer ingester = null;

    public BaseDBIngester(IngesterImplementer ingester, int processingBatchSize) {
        this.ingester = ingester;
        this.processingBatchSize = processingBatchSize > 0 ? processingBatchSize :
                DEFAULT_RAW_NOTIFICATION_PROCESS_BATCH_SIZE;
    }

    public void ingestActivityActivityRelationship(AddActivityActivityRelationshipDocument
                                                           activityActivityDoc) throws IngestException {
        ingestNotification(activityActivityDoc, "ActivityActivityRelationship",
                AddActivityActivityRelationshipDocument.class.getSimpleName(),
                NotificationTypeEnum.ADD_ACTIVITY_ACTIVITY_RELATION);
    }

    public void ingestAgentActivityRelationship(AddAgentActivityRelationshipDocument
                                                        agentActivityDoc) throws IngestException {
        ingestNotification(agentActivityDoc, "AgentActivityRelationship",
                AddAgentActivityRelationshipDocument.class.getSimpleName(),
                NotificationTypeEnum.ADD_AGENT_ACTIVITY_RELATION);
    }

    public void ingestAgentAgentRelationship(AddAgentAgentRelationshipDocument
                                                     agentAgentDoc) throws IngestException {
        ingestNotification(agentAgentDoc, "AgentAgentRelationship",
                AddAgentAgentRelationshipDocument.class.getSimpleName(),
                NotificationTypeEnum.ADD_AGENT_AGENT_RELATION);
    }

    public void ingestEntityEntityRelationship(AddEntityEntityRelationshipDocument
                                                       entityEntityDoc) throws IngestException {
        ingestNotification(entityEntityDoc, "EntityEntityRelationship",
                AddEntityEntityRelationshipDocument.class.getSimpleName(),
                NotificationTypeEnum.ADD_ENTITY_ENTITY_RELATION);
    }

    public void ingestActivityEntityRelationship(AddActivityEntityRelationshipDocument
                                                         activityEntityDoc) throws IngestException {
        ingestNotification(activityEntityDoc, "ActivityEntityRelationship",
                AddActivityEntityRelationshipDocument.class.getSimpleName(),
                NotificationTypeEnum.ADD_ACTIVITY_ENTITY_RELATION);
    }

    public void ingestAgentEntityRelationship(AddAgentEntityRelationshipDocument
                                                      agentEntityDoc) throws IngestException {
        ingestNotification(agentEntityDoc, "AgentEntityRelationship",
                AddAgentEntityRelationshipDocument.class.getSimpleName(),
                NotificationTypeEnum.ADD_AGENT_ENTITY_RELATION);
    }

    @Override
    public void ingestAddAttributes(AddAttributesDocument addAttributesDoc) throws IngestException {
        ingestNotification(addAttributesDoc, "AddAttributes",
                AddAttributesDocument.class.getSimpleName(),
                NotificationTypeEnum.ADD_ATTRIBUTES);
    }

    public int processNotifications() throws IngestException {
        List<StoredRawNotification<Long, String>> list
                = ingester.retrieveUnprocessedRawNotifications(ProcessingFilterType.KNOWN_TYPES, processingBatchSize);
        List<StoredRawNotification<Long, String>> sweepList
                = new ArrayList<StoredRawNotification<Long, String>>();
        List<StoredRawNotification<Long, String>> errorList
                = new ArrayList<StoredRawNotification<Long, String>>();

        // if raw notification list is null, return 0
        if (list == null)
            return 0;

        for (StoredRawNotification<Long, String> storedRawNotification : list) {
            NotificationTypeEnum notificationType = storedRawNotification.getNotificationType();
            try {
                switch (notificationType) {
                    case ADD_ACTIVITY_ACTIVITY_RELATION: {
                        AddActivityActivityRelationshipDocument doc = AddActivityActivityRelationshipDocument
                                .Factory.parse(storedRawNotification.getNotification());
                        ingester.storeActivityActivityRelationship(doc.getAddActivityActivityRelationship());
                        break;
                    } case ADD_ACTIVITY_ENTITY_RELATION: {
                        AddActivityEntityRelationshipDocument doc = AddActivityEntityRelationshipDocument
                                .Factory.parse(storedRawNotification.getNotification());
                        ingester.storeActivityEntityRelationship(doc.getAddActivityEntityRelationship());
                        break;
                    } case ADD_AGENT_AGENT_RELATION: {
                        AddAgentAgentRelationshipDocument doc = AddAgentAgentRelationshipDocument
                                .Factory.parse(storedRawNotification.getNotification());
                        ingester.storeAgentAgentRelationship(doc.getAddAgentAgentRelationship());
                        break;
                    } case ADD_AGENT_ENTITY_RELATION: {
                        AddAgentEntityRelationshipDocument doc = AddAgentEntityRelationshipDocument
                                .Factory.parse(storedRawNotification.getNotification());
                        ingester.storeAgentEntityRelationship(doc.getAddAgentEntityRelationship());
                        break;
                    } case ADD_ENTITY_ENTITY_RELATION: {
                        AddEntityEntityRelationshipDocument doc = AddEntityEntityRelationshipDocument
                                .Factory.parse(storedRawNotification.getNotification());
                        ingester.storeEntityEntityRelationship(doc.getAddEntityEntityRelationship());
                        break;
                    } case ADD_AGENT_ACTIVITY_RELATION: {
                        AddAgentActivityRelationshipDocument doc = AddAgentActivityRelationshipDocument
                                .Factory.parse(storedRawNotification.getNotification());
                        ingester.storeAgentActivityRelationship(doc.getAddAgentActivityRelationship());
                        break;
                    }case ADD_ATTRIBUTES: {
                        AddAttributesDocument doc = AddAttributesDocument
                                .Factory.parse(storedRawNotification.getNotification());
                        ingester.storeAddAttributes(doc.getAddAttributes());
                        break;
                    } case UNKNOWN_TYPES: {
                        XmlObject xmlObject = XmlObject.Factory.parse(storedRawNotification.getNotification());
                        // TODO : add a method in ingester
                        break;
                    }
                }
                sweepList.add(storedRawNotification);

            } catch (Exception e) {
                Long internalIDObj = (Long) storedRawNotification.getInternalID();
                log.error("Unable to process raw notification with internalID " + internalIDObj.longValue(), e);
                errorList.add(storedRawNotification);

            }
        }
        ingester.markRawNotifications(sweepList, ProcessingStatus.PROCESSED);
        ingester.markRawNotifications(errorList, ProcessingStatus.ERROR);

        return list.size();
    }

    public void resetUnfinishedNotifications() throws IngestException {
        ingester.resetUnfinishedRawNotifications();
    }

    /**
     * Ingests a raw xml by calling ingester
     *
     * @param xml          - XmlObject instance to be inserted
     * @param docType      - Document type
     * @param relationship - Name of the relationship to be ingested, for logging
     * @param type         - Type of the notification
     * @throws IngestException
     */
    private void ingestNotification(XmlObject xml, String docType, String relationship,
                                    NotificationTypeEnum type) throws IngestException {
        log.debug("Ingesting Raw Notification for " + relationship);
        if (log.isDebugEnabled())
            log.debug(relationship + "Doc:\n" + xml.xmlText(IngesterConstants.PRETTY_PRINT_OPTS));
        // validation errors
        List<XmlError> errors = new ArrayList<XmlError>();
        // if the xml validates properly, store it
        if (xml.validate(new XmlOptions().setErrorListener(errors))) {
            Calendar storeTime = Calendar.getInstance();
            ingester.storeRawNotification(type, storeTime, xml);
        } else {
            log.error(IngesterConstants.EXPMSG_INVALID_NOTIFICATION + docType);
            for (XmlError err : errors) {
                if (err instanceof XmlValidationError) {
                    XmlValidationError validationError = (XmlValidationError) err;
                    log.error("Message : " + validationError.getMessage());
                }
            }
            throw new IngestException(IngesterConstants.EXPMSG_INVALID_NOTIFICATION + docType);
        }
    }

}
