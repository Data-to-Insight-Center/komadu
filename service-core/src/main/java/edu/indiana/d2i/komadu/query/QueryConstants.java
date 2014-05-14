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

public class QueryConstants {

    public static final String FILE_IDENTIFIER = "File_";
    public static final String BLOCK_IDENTIFIER = "Block_";
    public static final String ACTIVITY_IDENTIFIER = "Activity_";
    public static final String AGENT_IDENTIFIER = "Agent_";
    public static final String ENTITY_IDENTIFIER = "Entity_";
    public static final String COLLECTION_IDENTIFIER = "Collection_";
    public static final String REG_ACTIVITY_IDENTIFIER = "Registry_activity_";
    public static final String DERIVATION_IDENTIFIER = "Derivation_";
    public static final String COMMUNICATION_IDENTIFIER = "Communication_";
    public static final String ASSOCIATION_IDENTIFIER = "Association_";
    public static final String USAGE_IDENTIFIER = "Usage_";
    public static final String GENERATION_IDENTIFIER = "Generation_";
    public static final String START_IDENTIFIER = "Start_";
    public static final String END_IDENTIFIER = "End_";
    public static final String INVALIDATION_IDENTIFIER = "Invalidation_";
    public static final String ATTRIBUTION_IDENTIFIER = "Attribution_";
    public static final String DELEGATION_IDENTIFIER = "Delegation_";

    public static final String KOMADU_NS = "http://komadu.d2i.indiana.edu";
    public static final String KOMADU_PREFIX = "kom";

    public static final String KOMADU_EXTERNAL_NS = "http://komadu.d2i.indiana.edu/external";
    public static final String KOMADU_EXTERNAL_PREFIX = "ext";

    public static final String ENTITY_FILE = "File";
    public static final String ENTITY_BLOCK = "Block";
    public static final String ENTITY_COLLECTION = "Collection";
    public static final String ENTITY_GENERIC = "Generic";

    public static final int MAX_CACHE_ENTRIES = 10000;

    // graph cache prefixes
    public static final String CONTEXT_GRAPH_CACHE_PREFIX = "context_";
    public static final String ACTIVITY_GRAPH_CACHE_PREFIX = "activity_";
    public static final String ENTITY_GRAPH_CACHE_PREFIX = "entity_";
    public static final String AGENT_GRAPH_CACHE_PREFIX = "agent_";

}
