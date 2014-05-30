/*
#
# Copyright 2007 The Trustees of Indiana University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or areed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -----------------------------------------------------------------
#
# Project: Karma-Service-core
# File:  QuerySummary.java
# Description:  Summary of query messages
#
# -----------------------------------------------------------------
# 
 */

package edu.indiana.d2i.komadu.query;

import org.apache.xmlbeans.XmlObject;

/**
 * @author Quan Zhou(quzhou@indiana.edu)
 * 
 */

public class QuerySummary {

	public static final QuerySummary UNKNOWN_QUERY_SUMMARY = new QuerySummary(
			QueryTypeEnum.UNKNOWN_TYPES);

	public static enum QueryTypeEnum {
        FIND_ACTIVITY, 
        GET_ACTIVITY_DETAIL,
        FIND_ENTITY,
        GET_ENTITY_DETAIL,
		GET_CONTEXT_WORKFLOW_GRAPH, 
		GET_ENTITY_GRAPH, 
		GET_ACTIVITY_GRAPH, 
		GET_AGENT_GRAPH, 
		UNKNOWN_TYPES;

		public static QueryTypeEnum determineQueryTypeFromXmlBeansDocument(
				XmlObject document) {
			if (document instanceof  FindActivityRequestDocument) {
				return FIND_ACTIVITY;
            } else if (document instanceof GetActivityDetailRequestDocument) {
                return GET_ACTIVITY_DETAIL;
            } else if (document instanceof FindEntityRequestDocument) {
                return FIND_ENTITY;
            } else if (document instanceof GetEntityDetailRequestDocument) {
                return GET_ENTITY_DETAIL;
			} else if (document instanceof GetContextWorkflowGraphRequestDocument) {
				return GET_CONTEXT_WORKFLOW_GRAPH;
			} else if (document instanceof GetEntityGraphRequestDocument) {
				return GET_ENTITY_GRAPH;
			} else if (document instanceof GetActivityGraphRequestDocument) {
				return GET_ACTIVITY_GRAPH;
			} else if (document instanceof GetAgentGraphRequestDocument) {
				return GET_AGENT_GRAPH;
			}
			return UNKNOWN_TYPES;
		}
	}

	private final QueryTypeEnum type;

	QuerySummary(QueryTypeEnum type) {
		this.type = type;
	}

	public QueryTypeEnum getQueryType() {
		return type;
	}

	public static void main(String args[]) {

	}
}
