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

package edu.indiana.d2i.komadu.ingest;

import java.util.Calendar;
import java.util.List;


import edu.indiana.d2i.komadu.service.*;
import org.apache.xmlbeans.XmlObject;

import edu.indiana.d2i.komadu.ingest.NotificationSummary.NotificationTypeEnum;


public interface IngesterImplementer<K, V> {


    // TODO : Add others

    public void storeRawNotification(NotificationTypeEnum notificationType, Calendar storeTime, XmlObject xmlObject) throws IngestException;

    public void resetUnfinishedRawNotifications() throws IngestException;

    public List<StoredRawNotification<K, V>> retrieveUnprocessedRawNotifications(IngesterConstants.ProcessingFilterType processingFilterType, int batchLimit) throws IngestException;

    public void storeActivityActivityRelationship(ActivityActivityType activityActivity) throws IngestException;

    public void storeActivityEntityRelationship(ActivityEntityType activityEntity) throws IngestException;

    public void storeAgentAgentRelationship(AgentAgentType agentAgent) throws IngestException;

    public void storeAgentEntityRelationship(AgentEntityType agentEntity) throws IngestException;

    public void storeEntityEntityRelationship(EntityEntityType entityEntity) throws IngestException;

    public void storeAgentActivityRelationship(AgentActivityType agentActivity) throws IngestException;

    public void storeAddAttributes(AddAttributesType addAttributes) throws IngestException;

    public void markRawNotifications(List<StoredRawNotification<K, V>> list, IngesterConstants.ProcessingStatus processingStatus) throws IngestException;

}