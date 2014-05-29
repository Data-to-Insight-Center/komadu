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

public class PROVSqlQuery {

    public static final String GET_ACTIVITIES_BY_CONTEXT_WORKFLOW_URI = "SELECT * FROM exe_activity WHERE context_workflow_uri = ? OR activity_uri = ?";

    public static final String GET_EXE_ACTIVITY_ATTRIBUTES_BY_ID = "SELECT * FROM exe_activity_attribute WHERE activity_id = ?";
    public static final String GET_EXE_USAGE_ATTRIBUTES_BY_ID = "SELECT * FROM exe_usage_attribute WHERE usage_id = ?";
    public static final String GET_EXE_GENERATION_ATTRIBUTES_BY_ID = "SELECT * FROM exe_generation_attribute WHERE generation_id = ?";
    public static final String GET_EXE_START_ATTRIBUTES_BY_ID = "SELECT * FROM exe_start_attribute WHERE start_id = ?";
    public static final String GET_EXE_END_ATTRIBUTES_BY_ID = "SELECT * FROM exe_end_attribute WHERE end_id = ?";
    public static final String GET_EXE_INVALIDATION_ATTRIBUTES_BY_ID = "SELECT * FROM exe_invalidation_attribute WHERE invalidation_id = ?";
    public static final String GET_EXE_ASSOCIATION_ATTRIBUTES_BY_ID = "SELECT * FROM exe_association_attribute WHERE association_id = ?";
    public static final String GET_EXE_ATTRIBUTION_ATTRIBUTES_BY_ID = "SELECT * FROM exe_attribution_attribute WHERE attribution_id = ?";
    public static final String GET_EXE_DELEGATION_ATTRIBUTES_BY_ID = "SELECT * FROM exe_delegation_attribute WHERE delegation_id = ?";
    public static final String GET_EXE_DERIVATION_ATTRIBUTES_BY_ID = "SELECT * FROM exe_derivation_attribute WHERE derivation_id = ?";
    public static final String GET_EXE_COMMUNICATION_ATTRIBUTES_BY_ID = "SELECT * FROM exe_communication_attribute WHERE communication_id = ?";
    public static final String GET_EXE_ENTITY_ATTRIBUTES_BY_ID = "SELECT * FROM exe_entity_attribute WHERE entity_id = ?";

    // for use with cache table
    public static final String NEW_CACHE_GRAPH = "INSERT INTO cache_graph (graph_uri, graph_content, generation_time, query_date, detailed) VALUES (?, ?, ?, ?, ?)";
    public static final String UPDATE_CACHE_GRAPH = "UPDATE cache_graph SET graph_content = ? , dirty = ? , generation_time = ? , query_date = ? WHERE graph_id = ?";
    public static final String GET_CACHE_GRAPH = "SELECT * FROM cache_graph WHERE graph_uri = ? and detailed = ?";
    public static final String GET_CACHE_COUNT = "SELECT count(*) FROM cache_graph";
    public static final String UPDATE_QUERY_DATE = "UPDATE cache_graph SET query_date = ? WHERE graph_id = ?";
    public static final String GET_GRAPH_TO_DELETE = "(SELECT * FROM cache_graph ORDER BY query_date ASC) ORDER BY generation_time ASC limit 1";

    public static final String GET_REG_ACTIVITIES_BY_ID = "SELECT * FROM reg_activity WHERE activity_id = ?";

    /**
     * TODO : should we check both context_workflow_uri and activity_uri???
     */
    public static final String GET_DATA_FILES_GENERATED = "SELECT f.file_uri, f.size, f.file_id "
            + "FROM exe_file f, exe_generation g, exe_activity a "
            + "WHERE g.activity_id = a.activity_id AND g.entity_id = f.file_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_DATA_BLOCKS_GENERATED = "SELECT b.block_id, b.block_uri, b.size, b.block_content "
            + "FROM exe_block b, exe_generation g, exe_activity a "
            + "WHERE g.activity_id = a.activity_id AND g.entity_id = b.block_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_DATA_COLLECTIONS_GENERATED = "SELECT c.collection_id, c.collection_uri "
            + "FROM exe_collection c, exe_generation g, exe_activity a "
            + "WHERE g.activity_id = a.activity_id AND g.entity_id = c.collection_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_DATA_FILES_USED = "SELECT f.file_uri, f.size, f.file_id "
            + "FROM exe_file f, exe_usage u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND u.entity_id = f.file_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_DATA_BLOCKS_USED = "SELECT b.block_id, b.size, b.block_content "
            + "FROM exe_block b, exe_usage u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND u.entity_id = b.block_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_DATA_COLLECTIONS_USED = "SELECT c.collection_id, c.collection_uri "
            + "FROM exe_collection c, exe_usage u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND u.entity_id = c.collection_id "
            + "AND (a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_AGENTS_BY_ACTIVITY_URI = "SELECT distinct g.* "
            + "FROM exe_activity a, exe_association s, reg_agent g "
            + "WHERE (a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL)) "
            + "AND s.activity_id = a.activity_id "
            + "AND s.agent_id = g.agent_id";

    public static final String GET_PROV_USAGES = "SELECT u.usage_id, u.activity_id, u.entity_id, u.location, u.usage_time "
            + "FROM exe_usage u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_GENERATIONS = "SELECT u.generation_id, u.activity_id, u.entity_id, u.location, u.generation_time "
            + "FROM exe_generation u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_STARTS = "SELECT u.start_id, u.activity_id, u.trigger_id, u.location, u.start_time "
            + "FROM exe_start u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_ENDS = "SELECT u.end_id, u.activity_id, u.trigger_id, u.location, u.end_time "
            + "FROM exe_end u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_INVALIDATIONS = "SELECT u.invalidation_id, u.activity_id, u.entity_id, u.location, u.invalidation_time "
            + "FROM exe_invalidation u, exe_activity a "
            + "WHERE u.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_ASSOCIATIONS = "SELECT s.association_id, s.activity_id, s.agent_id, s.plan_id "
            + "FROM exe_association s, exe_activity a "
            + "WHERE s.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    /**
     * This query gives the entities which are attributed to agents who are already associated with the
     * activity identified by the given workflow_uri.
     */
    public static final String GET_PROV_ATTRIBUTIONS_THROUGH_ASSOCIATIONS = "SELECT t.attribution_id, t.agent_id, t.entity_id "
            + "FROM exe_attribution t, exe_activity a, exe_association s "
            + "WHERE t.agent_id = s.agent_id AND s.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    /**
     * This query finds delegations in which the responsible agent is someone already associated with the
     * activity identified by the given workflow_uri.
     */
    public static final String GET_PROV_DELEGATIONS = "SELECT d.delegation_id, d.del_agent_id, d.res_agent_id, d.activity_id, g.agent_uri, g.agent_type, g.name, g.affiliation, g.email, g.role, g.location "
            + "FROM exe_delegation d, exe_activity a, exe_association s, reg_agent g "
            + "WHERE s.activity_id = a.activity_id AND s.agent_id = d.res_agent_id AND g.agent_id = d.del_agent_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_COMMUNICATIONS_BY_ENTITY = "SELECT g.activity_id as gen_id, u.activity_id as used_id "
            + "FROM exe_generation g, exe_usage u "
            + "WHERE g.entity_id = u.entity_id AND "
            + "g.activity_id IN (SELECT activity_id FROM exe_activity WHERE context_workflow_uri = ?) AND "
            + "u.activity_id IN (SELECT activity_id FROM exe_activity WHERE context_workflow_uri = ?)";

    public static final String GET_PROV_COMMUNICATIONS = "SELECT distinct c.communication_id, c.informed_id, c.informant_id "
            + "FROM exe_communication c, exe_activity a "
            + "WHERE (c.informed_id = a.activity_id OR c.informant_id = a.activity_id) AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_DERIVATIONS_IN_CONTEXT = "SELECT d.* "
            + "FROM exe_derivation d, exe_generation g, exe_usage u "
            + "WHERE d.used_id = u.entity_id AND d.generated_id = g.entity_id AND "
            + "g.activity_id IN (SELECT activity_id FROM exe_activity WHERE context_workflow_uri = ?) AND "
            + "u.activity_id IN (SELECT activity_id FROM exe_activity WHERE context_workflow_uri = ?)";

    public static final String GET_PROV_DERIVATIONS_GENERATED_IN_CONTEXT = "SELECT d.* "
            + "FROM exe_derivation d, exe_usage u, exe_activity a "
            + "WHERE d.generated_id = u.entity_id AND u.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_DERIVATIONS_USED_IN_CONTEXT = "SELECT d.* "
            + "FROM exe_derivation d, exe_generation g, exe_activity a "
            + "WHERE d.used_id = g.entity_id AND g.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_DERIVATIONS_BY_ACTIVITY = "SELECT g.entity_id as gen_id, u.entity_id as used_id "
            + "FROM exe_generation g, exe_usage u, exe_activity a "
            + "WHERE g.activity_id = u.activity_id AND u.activity_id = a.activity_id AND "
            + "(a.context_workflow_uri = ? OR (a.activity_uri = ? AND a.context_workflow_uri is NULL))";

    public static final String GET_PROV_ALTERNATES = "SELECT * FROM exe_alternate WHERE ";
    public static final String GET_PROV_SPECIALIZATIONS = "SELECT * FROM exe_specialization WHERE ";
    public static final String GET_PROV_MEMBERSHIPS = "SELECT * FROM exe_collection_membership WHERE ";

    public static final String FIND_ACTIVITY = "SELECT distinct(a.activity_uri) FROM exe_activity a WHERE ";

    public static String FIND_ACTIVITY_ATTRIBUTE = "SELECT distinct(a.activity_uri) FROM exe_activity a, exe_activity_attribute an WHERE "
            + "AND a.activity_id = an.activity_id ";

    public static final String FIND_ACTIVITY_COMM = "SELECT distinct(a.activity_uri) FROM exe_activity a, exe_communication c WHERE "
            + "a.activity_id = c.informant_id ";

    public static String FIND_ACTIVITY_ATTRIBUTE_COMM = "SELECT distinct(a.activity_uri) FROM exe_activity a, exe_communication c, exe_activity_attribute an WHERE "
            + "AND a.activity_id = an.activity_id AND a.activity_id = c.informant_id ";

    public static final String ATTRIBUTE_COMPARISON = "OR an.attribute_value LIKE ? ";
    public static final String GET_ACTIVITY_BY_URI = "SELECT * FROM exe_activity WHERE activity_uri = ? ";
    public static final String GET_ACTIVITY_BY_ID = "SELECT * FROM exe_activity WHERE activity_id = ? ";

    public static final String GET_ENTITY_TYPE = "SELECT entity_type FROM exe_entity WHERE entity_id = ? ";
    public static final String GET_FILE_BY_ID = "SELECT * FROM exe_file WHERE file_id = ? ";
    public static final String GET_BLOCK_BY_ID = "SELECT * FROM exe_block WHERE block_id = ? ";
    public static final String GET_COLLECTION_BY_ID = "SELECT * FROM exe_collection WHERE collection_id = ? ";
    public static final String GET_GENERIC_ENTITY_BY_ID = "SELECT * FROM exe_generic_entity WHERE generic_entity_id = ? ";


    /**
     * Queries needed for graph generations by inference
     */
    public static final String GET_ACTIVITIES_BY_ACTIVITY_URI = "SELECT * FROM exe_activity WHERE activity_uri = ?";
    public static final String GET_ACTIVITIES_BY_ACTIVITY_ID = "SELECT * FROM exe_activity WHERE activity_id = ?";
    public static final String GET_AGENTS_BY_AGENT_ID = "SELECT * FROM reg_agent WHERE agent_id = ?";
    public static final String GET_AGENTS_BY_AGENT_URI = "SELECT * FROM reg_agent WHERE agent_uri = ?";

    public static final String GET_ASSOCIATIONS_BY_ACTIVITY_ID = "SELECT * FROM exe_association WHERE activity_id = ?";
    public static final String GET_ASSOCIATIONS_BY_AGENT_ID = "SELECT * FROM exe_association WHERE agent_id = ?";

    public static final String GET_COMMUNICATIONS_BY_ACTIVITY_ID = "SELECT * FROM exe_communication WHERE (informed_id = ? OR informant_id = ?)";
    public static final String GET_COMMUNICATIONS_BY_ENTITY_NO_CONTEXT = "SELECT g.activity_id as gen_id, u.activity_id as used_id "
            + "FROM exe_generation g, exe_usage u "
            + "WHERE g.entity_id = u.entity_id AND "
            + "(g.activity_id = ? OR u.activity_id = ?)";

    public static final String GET_USAGES_BY_ACTIVITY_ID = "SELECT * FROM exe_usage WHERE activity_id = ?";
    public static final String GET_USAGES_BY_ENTITY_ID = "SELECT * FROM exe_usage WHERE entity_id = ?";

    public static final String GET_GENERATIONS_BY_ACTIVITY_ID = "SELECT * FROM exe_generation WHERE activity_id = ?";
    public static final String GET_GENERATIONS_BY_ENTITY_ID = "SELECT * FROM exe_generation WHERE entity_id = ?";

    public static final String GET_STARTS_BY_ACTIVITY_ID = "SELECT * FROM exe_start WHERE activity_id = ?";
    public static final String GET_STARTS_BY_ENTITY_ID = "SELECT * FROM exe_start WHERE trigger_id = ?";

    public static final String GET_ENDS_BY_ACTIVITY_ID = "SELECT * FROM exe_end WHERE activity_id = ?";
    public static final String GET_ENDS_BY_ENTITY_ID = "SELECT * FROM exe_end WHERE trigger_id = ?";

    public static final String GET_INVALIDATIONS_BY_ACTIVITY_ID = "SELECT * FROM exe_invalidation WHERE activity_id = ?";
    public static final String GET_INVALIDATIONS_BY_ENTITY_ID = "SELECT * FROM exe_invalidation WHERE entity_id = ?";

    public static final String GET_ATTRIBUTIONS_BY_AGENT_ID = "SELECT * FROM exe_attribution WHERE agent_id = ?";
    public static final String GET_ATTRIBUTIONS_BY_ENTITY_ID = "SELECT * FROM exe_attribution WHERE entity_id = ?";

    public static final String GET_DELEGATIONS_BY_AGENT_ID = "SELECT * FROM exe_delegation WHERE (del_agent_id = ? OR res_agent_id = ?)";

    public static final String GET_ALTERNATES_BY_ENTITY_ID = "SELECT * FROM exe_alternate WHERE (alternate1_id = ? OR alternate2_id = ?)";

    public static final String GET_SPECIALIZATIONS_BY_ENTITY_ID = "SELECT * FROM exe_specialization WHERE (specific_id = ? OR general_id = ?)";

    public static final String GET_MEMBERSHIPS_BY_COLLECTION_ID = "SELECT * FROM exe_collection_membership WHERE collection_id = ?";

    public static final String GET_DERIVATIONS_BY_ENTITY_ID = "SELECT * FROM exe_derivation WHERE (used_id = ? OR generated_id = ?)";
    public static final String GET_DERIVATIONS_BY_ACTIVITY_NO_CONTEXT = "SELECT g.entity_id as gen_id, u.entity_id as used_id "
            + "FROM exe_generation g, exe_usage u "
            + "WHERE g.activity_id = u.activity_id AND "
            + "(g.entity_id = ? OR u.entity_id = ?)";

    public static final String GET_FILE_BY_URI = "SELECT * FROM exe_file WHERE file_uri = ? ";
    public static final String GET_BLOCK_BY_URI = "SELECT * FROM exe_block WHERE block_uri = ? ";
    public static final String GET_COLLECTION_BY_URI = "SELECT * FROM exe_collection WHERE collection_uri = ? ";
    public static final String GET_GENERIC_ENTITY_BY_URI = "SELECT * FROM exe_generic_entity WHERE generic_entity_uri = ? ";

}
