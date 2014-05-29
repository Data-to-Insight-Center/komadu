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

package edu.indiana.d2i.komadu.query;

public interface QueryImplementer {

    public FindActivityResponseDocument findActivity(
            FindActivityRequestDocument findActivityRequest)
            throws QueryException;

    public FindEntityResponseDocument findEntity(
            FindEntityRequestDocument findEntityRequest)
            throws QueryException;

    public GetActivityDetailResponseDocument getActivityDetail(
            GetActivityDetailRequestDocument getActivityDetailRequest)
            throws QueryException;

    public GetEntityDetailResponseDocument getEntityDetail(
            GetEntityDetailRequestDocument getEntityDetailRequest)
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
            throws QueryException;

}
