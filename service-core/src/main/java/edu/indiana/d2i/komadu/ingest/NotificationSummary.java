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

import edu.indiana.d2i.komadu.service.*;
import org.apache.xmlbeans.XmlObject;

public class NotificationSummary {

    public static enum NotificationTypeEnum {

        ADD_ACTIVITY_ACTIVITY_RELATION,
        ADD_AGENT_ACTIVITY_RELATION,
        ADD_AGENT_AGENT_RELATION,
        ADD_ENTITY_ENTITY_RELATION,
        ADD_ACTIVITY_ENTITY_RELATION,
        ADD_AGENT_ENTITY_RELATION,
        ADD_ATTRIBUTES,
        UNKNOWN_TYPES;

        public static NotificationTypeEnum determineNotificationTypeFromXmlBeansDocument(XmlObject document) {
            if (document instanceof AddActivityActivityRelationshipDocument) {
                return ADD_ACTIVITY_ACTIVITY_RELATION;
            } else if (document instanceof AddAgentActivityRelationshipDocument) {
                return ADD_AGENT_ACTIVITY_RELATION;
            } else if (document instanceof AddAgentAgentRelationshipDocument) {
                return ADD_AGENT_AGENT_RELATION;
            } else if (document instanceof AddEntityEntityRelationshipDocument) {
                return ADD_ENTITY_ENTITY_RELATION;
            } else if (document instanceof AddActivityEntityRelationshipDocument) {
                return ADD_ACTIVITY_ENTITY_RELATION;
            } else if (document instanceof AddAgentEntityRelationshipDocument) {
                return ADD_AGENT_ENTITY_RELATION;
            } else if (document instanceof AddAttributesDocument) {
                return ADD_ATTRIBUTES;
            }
            return UNKNOWN_TYPES;
        }

        // TODO : Check this..
        public static NotificationTypeEnum determineNotificationTypeFromXmlBeansDocument(XmlObject document, Integer flog) {
            String document_string = document.xmlText();
            if(document_string.contains("addAgentAgentRelationship")){
                return ADD_AGENT_AGENT_RELATION;
            } else if (document_string.contains("addAgentActivityRelationship")){
                return ADD_AGENT_ACTIVITY_RELATION;
            } else if (document_string.contains("addActivityActivityRelationship")){
                return ADD_ACTIVITY_ACTIVITY_RELATION;
            } else if (document_string.contains("addEntityEntityRelationship")){
                return ADD_ENTITY_ENTITY_RELATION;
            } else if (document_string.contains("addActivityEntityRelationship")){
                return ADD_ACTIVITY_ENTITY_RELATION;
            } else if(document_string.contains("addAgentEntityRelationship")){
                return ADD_AGENT_ACTIVITY_RELATION;
            } else if(document_string.contains("addAttributes")){
                return ADD_ATTRIBUTES;
            } else {
                return UNKNOWN_TYPES;
            }
        }

    }

}
