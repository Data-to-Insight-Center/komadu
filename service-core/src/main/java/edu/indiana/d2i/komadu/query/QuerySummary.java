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
import org.openprovenance.prov.model.*;
import org.openprovenance.prov.xml.Other;
import org.w3.www.ns.prov.Document;

import org.openprovenance.prov.model.*;
import org.openprovenance.prov.model.ActedOnBehalfOf;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Agent;
import org.openprovenance.prov.model.AlternateOf;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.HadMember;
import org.openprovenance.prov.model.SpecializationOf;
import org.openprovenance.prov.model.Used;
import org.openprovenance.prov.model.WasAssociatedWith;
import org.openprovenance.prov.model.WasAttributedTo;
import org.openprovenance.prov.model.WasDerivedFrom;
import org.openprovenance.prov.model.WasEndedBy;
import org.openprovenance.prov.model.WasGeneratedBy;
import org.openprovenance.prov.model.WasInformedBy;
import org.openprovenance.prov.model.WasInvalidatedBy;
import org.openprovenance.prov.model.WasStartedBy;
import org.openprovenance.prov.xml.*;
import org.w3.www.ns.prov.Document;
/**
 * @author Quan Zhou(quzhou@indiana.edu)
 * 
 */

public class QuerySummary {

	public static final QuerySummary UNKNOWN_QUERY_SUMMARY = new QuerySummary(
			QueryTypeEnum.UNKNOWN_TYPES);

	/*  public FindActivityResponseDocument findActivity(
            FindActivityRequestDocument findServiceRequest)
            throws QueryException;

    public GetContextWorkflowGraphResponseDocument getContextWorkflowGraph(
            GetContextWorkflowGraphRequestDocument getWorkflowGraphRequest)
            throws QueryException;
    
    public GetEntityGraphResponseDocument getEntityGraph(
            GetEntityGraphRequestDocument getEntityGraphRequest) 
            throws QueryException;

    public GetActivityGraphResponseDocument getActivityGraph(
            GetActivityGraphRequestDocument getActivityGraphRequest)
            throws QueryException;

    public GetAgentGraphResponseDocument getAgentGraph(
            GetAgentGraphRequestDocument getAgentGraphRequest)
            throws QueryException;*/
	
	public static enum QueryTypeEnum {
		FIND_SERVICE, 
		GET_CONTEXT_WORKFLOW_GRAPH, 
		GET_ENTITY_GRAPH, 
		GET_ACTIVITY_GRAPH, 
		GET_AGENT_GRAPH, 
		UNKNOWN_TYPES;

		public static QueryTypeEnum determineQueryTypeFromXmlBeansDocument(
				XmlObject document) {
			if (document instanceof  FindActivityRequestDocument) {
				return FIND_SERVICE;
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
