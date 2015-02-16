--
-- Copyright 2014 The Trustees of Indiana University
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
-- http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
--


-- ------------------------------------------------------------------
-- MySQL Database Schema for Komadu
--
-- Version:
--          1.0.0
--
-- Authors:
--          Isuru Suriarachchi (isuriara@cs.indiana.edu)
--
-- ------------------------------------------------------------------

SET foreign_key_checks=0;

DROP TABLE IF EXISTS schema_version;
CREATE TABLE schema_version (
  version                      VARCHAR(63) NOT NULL
) ENGINE=InnoDB;

INSERT INTO schema_version(version) VALUES ("1.0.0");


-- ======================================= registry level tables below ========================

DROP TABLE IF EXISTS reg_agent;
CREATE TABLE reg_agent (
   agent_id                     BIGINT NOT NULL AUTO_INCREMENT,                   -- internal ID
   agent_uri                    VARCHAR(375) NOT NULL,                            -- unique URI of the agent
   agent_type                   VARCHAR(31) NOT NULL,                             -- ORGANIZATION, PERSON, SOFTWARE or OTHER
   name                         VARCHAR(127) NULL,                                -- name of the person/organization/software
   affiliation                  VARCHAR(31) NULL,                                 -- optional affiliation
   email                        VARCHAR(63) NULL,                                 -- optional email
   role                         VARCHAR(127) NULL,                                        -- optional role
   location                     VARCHAR(127) NULL,                                        -- optional location

   PRIMARY KEY (agent_id),
   INDEX (name),
   INDEX (agent_uri)
) ENGINE=InnoDB;


DROP TABLE IF EXISTS reg_activity;
CREATE TABLE reg_activity (
  activity_id                          BIGINT NOT NULL AUTO_INCREMENT,            -- internal ID of this activity
  activity_type                        VARCHAR(15) NOT NULL,                      -- type of the activity: WORKFLOW, SERVICE, METHOD, USER
--   activity_subtype                     VARCHAR(15) NOT NULL,                      -- subtype of the activity:
  activity_uri                         VARCHAR(375) NOT NULL,                     -- a name of the activity, e.g. URI
  version                              VARCHAR(31) NULL,                          -- optional version information for the activity
  creation_time                        DATETIME NOT NULL,                         -- time the activity was created

  PRIMARY KEY (activity_id),
  INDEX (activity_type),
--   INDEX (activity_subtype),
  INDEX (activity_uri),
  INDEX (version)

) ENGINE=InnoDB;


-- ==============================================  execution level tables below ===========================

DROP TABLE IF EXISTS exe_activity;
CREATE TABLE exe_activity (
  activity_id                          BIGINT NOT NULL AUTO_INCREMENT,              -- internal ID of activity instance
  activity_uri                         VARCHAR(375) NOT NULL,                       -- URI of the activity instance, e.g. an URI of a concrete service
  activity_type                        VARCHAR(15) NOT NULL,                        -- SERVICE, METHOD, WORKFLOW
--   activity_subtype                     VARCHAR(15) NULL,                             -- CONTROLLER, HUMAN_PROXY, REGULAR(or NULL means REGULAR)
  context_workflow_uri               VARCHAR(375) NULL,                           -- URI of the context workflow, applicable when the activity is a SERVICE or a METHOD
  context_service_uri                VARCHAR(375) NULL,                           -- URI of the context service, applicable when the activity is a METHOD
  timestep                           INT DEFAULT -1,                              -- workflow timestep
  context_wf_node_id_token           VARCHAR(255) NULL,                           -- workflow node ID
  location                           VARCHAR(127) NULL,                                   -- optional location
  instance_of                        BIGINT NULL,                                 -- optional pointer to registry level foreign key to reg_activity.activity_id

  PRIMARY KEY (activity_id),
--   INDEX (activity_uri(127), activity_type, activity_subtype, context_workflow_uri(127), context_wf_node_id_token, timestep, context_service_uri(127)),
  INDEX (activity_uri(127), activity_type, context_workflow_uri(127), context_wf_node_id_token, timestep, context_service_uri(127)),
  FOREIGN KEY (instance_of) REFERENCES reg_activity(activity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_association;
CREATE TABLE exe_association (
  association_id                    BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of association instance
  activity_id                       BIGINT NOT NULL,                              -- activity related to association
  agent_id                          BIGINT NOT NULL,                              -- agent related to association
  plan_id                           BIGINT NULL,                                  -- plan related to association

  PRIMARY KEY (association_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id),
  FOREIGN KEY (agent_id) REFERENCES reg_agent(agent_id)
--  FOREIGN KEY (plan_id) REFERENCES reg_plan(activity_id)                      -- TODO

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_communication;
CREATE TABLE exe_communication (
  communication_id                  BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of communication instance
  informed_id                       BIGINT NOT NULL,                              -- informed activity id
  informant_id                      BIGINT NOT NULL,                              -- informant activity id

  PRIMARY KEY (communication_id),
  FOREIGN KEY (informed_id) REFERENCES exe_activity(activity_id),
  FOREIGN KEY (informant_id) REFERENCES exe_activity(activity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_delegation;
CREATE TABLE exe_delegation (
  delegation_id                     BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of delegation instance
  del_agent_id                      BIGINT NOT NULL,                              -- delegate Agent
  res_agent_id                      BIGINT NOT NULL,                              -- responsible Agent
  activity_id                       BIGINT NULL,                                  -- optional activity for delegation

  PRIMARY KEY (delegation_id),
  FOREIGN KEY (del_agent_id) REFERENCES reg_agent(agent_id),
  FOREIGN KEY (res_agent_id) REFERENCES reg_agent(agent_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_attribution;
CREATE TABLE exe_attribution (
  attribution_id                    BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of attribution instance
  agent_id                          BIGINT NOT NULL,                              -- Agent ID
  entity_id                         BIGINT NOT NULL,                              -- Entity

  PRIMARY KEY (attribution_id),
  FOREIGN KEY (agent_id) REFERENCES reg_agent(agent_id),
  FOREIGN KEY (entity_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_usage;
CREATE TABLE exe_usage (
  usage_id                          BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of usage instance
  activity_id                       BIGINT NOT NULL,                              -- Activity ID
  entity_id                         BIGINT NOT NULL,                              -- Entity ID
  location                          VARCHAR(127) NULL,                                    -- optional location
  usage_time                        DATETIME NULL,                                -- usage timestamp

  PRIMARY KEY (usage_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id),
  FOREIGN KEY (entity_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_generation;
CREATE TABLE exe_generation (
  generation_id                     BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of generation instance
  activity_id                       BIGINT NOT NULL,                              -- Activity ID
  entity_id                         BIGINT NOT NULL,                              -- Entity ID
  location                          VARCHAR(127) NULL,                                    -- optional location
  generation_time                   DATETIME NULL,                                -- generation timestamp

  PRIMARY KEY (generation_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id),
  FOREIGN KEY (entity_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_start;
CREATE TABLE exe_start (
  start_id                          BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of start instance
  activity_id                       BIGINT NOT NULL,                              -- Activity ID
  trigger_id                        BIGINT NOT NULL,                              -- Trigger Entity ID
  location                          VARCHAR(127) NULL,                                    -- optional location
  start_time                        DATETIME NULL,                                -- start timestamp

  PRIMARY KEY (start_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id),
  FOREIGN KEY (trigger_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_end;
CREATE TABLE exe_end (
  end_id                            BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of end instance
  activity_id                       BIGINT NOT NULL,                              -- Activity ID
  trigger_id                        BIGINT NOT NULL,                              -- Entity ID
  location                          VARCHAR(127) NULL,                                    -- optional location
  end_time                          DATETIME NULL,                                -- end timestamp

  PRIMARY KEY (end_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id),
  FOREIGN KEY (trigger_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_invalidation;
CREATE TABLE exe_invalidation (
  invalidation_id                   BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of invalidation instance
  activity_id                       BIGINT NOT NULL,                              -- Activity ID
  entity_id                         BIGINT NOT NULL,                              -- Entity ID
  location                          VARCHAR(127) NULL,                                    -- optional location
  invalidation_time                 DATETIME NULL,                                -- invalidation timestamp

  PRIMARY KEY (invalidation_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id),
  FOREIGN KEY (entity_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_derivation;
CREATE TABLE exe_derivation (
  derivation_id                  BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of derivation instance
  used_id                        BIGINT NOT NULL,                              -- used entity id
  generated_id                   BIGINT NOT NULL,                              -- generated entity id
  derivation_type                VARCHAR(31) NOT NULL,                         -- DERIVATION, REVISION, QUOTATION or PRIMARY_SOURCE

  PRIMARY KEY (derivation_id),
  FOREIGN KEY (used_id) REFERENCES exe_entity(entity_id),
  FOREIGN KEY (generated_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_alternate;
CREATE TABLE exe_alternate (
  alternate_id                  BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of alternate instance
  alternate1_id                 BIGINT NOT NULL,                              -- used entity id
  alternate2_id                 BIGINT NOT NULL,                              -- generated entity id

  PRIMARY KEY (alternate_id),
  FOREIGN KEY (alternate1_id) REFERENCES exe_entity(entity_id),
  FOREIGN KEY (alternate2_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_specialization;
CREATE TABLE exe_specialization (
  specialization_id                  BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of specialization instance
  specific_id                        BIGINT NOT NULL,                              -- specific entity id
  general_id                         BIGINT NOT NULL,                              -- general entity id

  PRIMARY KEY (specialization_id),
  FOREIGN KEY (specific_id) REFERENCES exe_entity(entity_id),
  FOREIGN KEY (general_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_entity;
CREATE TABLE exe_entity (
  entity_id                         BIGINT NOT NULL AUTO_INCREMENT,               -- internal ID of data object
  entity_type                       VARCHAR(31) NOT NULL,                         -- FILE, BLOCK, COLLECTION, GENERIC
--   instance_of                       BIGINT NULL,                               -- foreign key to reg_entity.entity_id
  role                              VARCHAR(127) NULL,                                    -- optional role
  location                          VARCHAR(127) NULL,                                    -- optional location

  PRIMARY KEY (entity_id),
  INDEX (entity_type)
--   FOREIGN KEY (instance_of) REFERENCES reg_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_collection;
CREATE TABLE exe_collection (
  collection_id                    BIGINT NOT NULL,                               -- foreign key to exe_entity(entity_id)
  collection_uri                   VARCHAR(375) NOT NULL,                         -- uri of the collection

  INDEX(collection_uri),
  FOREIGN KEY (collection_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_collection_membership;
CREATE TABLE exe_collection_membership (
  membership_id                    BIGINT NOT NULL AUTO_INCREMENT,                -- membership internal ID
  collection_id                    BIGINT NOT NULL,                               -- foreign key to exe_collection.collection_id
  member_id                        BIGINT NOT NULL,                               -- foreign key to exe_entity.entity_id

  PRIMARY KEY (membership_id),
  FOREIGN KEY (collection_id) REFERENCES exe_collection(collection_id),
  FOREIGN KEY (member_id) REFERENCES exe_entity(entity_id),
  INDEX (collection_id, member_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_file;
CREATE TABLE exe_file (
  file_id                          BIGINT NOT NULL,                               -- foreign key to exe_entity(entity_id)
  file_uri                         VARCHAR(375) NOT NULL,                         -- a unique filename, e.g. URL or logical name
  owner_id                         BIGINT NULL,                                   -- optional owner of the file, foreign key to reg_agent.agent_id
  creation_date                    DATETIME NULL,                                 -- optional creation date of the file
  size                             BIGINT NULL,                                   -- optional size of the file
  md5_checksum                     VARCHAR(63) NULL,                              -- optional md5 checksum of the file
  file_name                        VARCHAR(127) NULL,                             -- optional short name of the file

  INDEX (file_uri),
  FOREIGN KEY (file_id) REFERENCES exe_entity(entity_id),
  FOREIGN KEY (owner_id) REFERENCES reg_agent(agent_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_block;
CREATE TABLE exe_block (
  block_id                         BIGINT NOT NULL,                               -- foreign key to exe_entity(entity_id)
  block_uri                        VARCHAR(375) NOT NULL,                         -- a unique id for block
  md5_checksum                     VARCHAR(63) NULL,                              -- md5 checksum of the block
  size                             BIGINT NULL,                                   -- size of the block
  block_content                    BLOB NOT NULL,                                 -- block content

  INDEX(md5_checksum),
  FOREIGN KEY (block_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_generic_entity;
CREATE TABLE exe_generic_entity (
  generic_entity_id                BIGINT NOT NULL,                               -- foreign key to exe_entity(entity_id)
  generic_entity_uri               VARCHAR(375) NOT NULL,                         -- a unique identifier for entity

  INDEX(generic_entity_uri),
  FOREIGN KEY (generic_entity_id) REFERENCES exe_entity(entity_id)

) ENGINE=InnoDB;

-- =============================== attribute tables for registry level ==================

DROP TABLE IF EXISTS reg_agent_attribute;
CREATE TABLE reg_agent_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  agent_id                     BIGINT NOT NULL,                                   -- foreign key to reg_agent.agent_id
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE
  
  PRIMARY KEY (attribute_id),
  FOREIGN KEY (agent_id) REFERENCES reg_agent(agent_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_activity_attribute;
CREATE TABLE exe_activity_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  activity_id                  BIGINT NOT NULL,                                   -- foreign key to exe_activity.activity_id
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (activity_id) REFERENCES exe_activity(activity_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_entity_attribute;
CREATE TABLE exe_entity_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  entity_id                    BIGINT NOT NULL,                                   -- foreign key to exe_entity.entity_id
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (entity_id) REFERENCES exe_entity(entity_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_usage_attribute;
CREATE TABLE exe_usage_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  usage_id                     BIGINT NOT NULL,                                   -- foreign key to usage
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (usage_id) REFERENCES exe_usage(usage_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_generation_attribute;
CREATE TABLE exe_generation_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  generation_id                BIGINT NOT NULL,                                   -- foreign key to generation
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (generation_id) REFERENCES exe_generation(generation_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_start_attribute;
CREATE TABLE exe_start_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  start_id                     BIGINT NOT NULL,                                   -- foreign key to start
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (start_id) REFERENCES exe_start(start_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_end_attribute;
CREATE TABLE exe_end_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  end_id                     BIGINT NOT NULL,                                   -- foreign key to end
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (end_id) REFERENCES exe_end(end_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_invalidation_attribute;
CREATE TABLE exe_invalidation_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  invalidation_id              BIGINT NOT NULL,                                   -- foreign key to invalidation
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (invalidation_id) REFERENCES exe_invalidation(invalidation_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_derivation_attribute;
CREATE TABLE exe_derivation_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  derivation_id                BIGINT NOT NULL,                                   -- foreign key to derivation
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (derivation_id) REFERENCES exe_derivation(derivation_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_association_attribute;
CREATE TABLE exe_association_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  association_id               BIGINT NOT NULL,                                   -- foreign key to association
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (association_id) REFERENCES exe_association(association_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_attribution_attribute;
CREATE TABLE exe_attribution_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  attribution_id               BIGINT NOT NULL,                                   -- foreign key to attribution
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (attribution_id) REFERENCES exe_attribution(attribution_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_communication_attribute;
CREATE TABLE exe_communication_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  communication_id             BIGINT NOT NULL,                                   -- foreign key to communication
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (communication_id) REFERENCES exe_communication(communication_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;


DROP TABLE IF EXISTS exe_delegation_attribute;
CREATE TABLE exe_delegation_attribute (
  attribute_id                 BIGINT NOT NULL AUTO_INCREMENT,                    -- internal ID
  delegation_id                BIGINT NOT NULL,                                   -- foreign key to delegation
  attribute_name               VARCHAR(127) NOT NULL,                             -- name part of the name-value pair, could be a URI per OPM v1.1
  attribute_value              VARCHAR(127) NOT NULL,                                     -- value part of the name-value pair.
  attribute_type               VARCHAR(31) NOT NULL,                              -- indicates what type of attribute this is, e.g. PROV_ATTRIBUTE, KOMADU_ATTRIBUTE, EXTERNAL_SOURCE

  PRIMARY KEY (attribute_id),
  FOREIGN KEY (delegation_id) REFERENCES exe_delegation(delegation_id),
  INDEX (attribute_name),
  INDEX (attribute_type)

) ENGINE=InnoDB;

SET foreign_key_checks=1;

-- ============================= raw notification table ==========================

DROP TABLE IF EXISTS raw_notification;
CREATE TABLE raw_notification (
  raw_id                       BIGINT NOT NULL AUTO_INCREMENT,
  store_time                   DATETIME NOT NULL,
  notification_type            VARCHAR(63) NOT NULL,
  processing_status            VARCHAR(15) NOT NULL DEFAULT 'RAW',                 -- processing status, can be RAW, PROCESSED, or ERROR
  notification                 MEDIUMTEXT,

  PRIMARY KEY (raw_id),
  INDEX (notification_type),
  INDEX (processing_status, notification_type)

) ENGINE=InnoDB;

-- ================================ cache level tables ===================================
DROP TABLE IF EXISTS cache_graph;
CREATE TABLE cache_graph (
   graph_id                     BIGINT NOT NULL AUTO_INCREMENT,						          -- internal ID
   graph_uri                    VARCHAR(375) NULL,									                -- graph uri
   graph_content                MEDIUMBLOB,												                  -- PROV graph
   query_date                   DATETIME NOT NULL,                                  -- time the query took place
   generation_time              BIGINT,                                             -- graph generation time
   dirty                        BOOLEAN default false,								              -- dirty bit to mark if updates to graph occur
   detailed                     BOOLEAN default true,                               -- bit to mark if graph is detail graph

   PRIMARY KEY (graph_id),
   INDEX (graph_uri)
) ENGINE=InnoDB;

-- ====================== Procedure PR_OBJECT_LOCK ===============================

DROP PROCEDURE IF EXISTS PR_OBJECT_LOCK;

DELIMITER |

CREATE PROCEDURE PR_OBJECT_LOCK
(IN lockOp INTEGER, IN lockTimeOut INTEGER,
IN p_object_id VARCHAR(375), OUT status INTEGER)
object_lock: BEGIN
DECLARE lockPrefix VARCHAR(7) DEFAULT "komadu.";
DECLARE lockName VARCHAR(255) DEFAULT "";
SET status = 0;
SET lockName = CONCAT(lockPrefix,RIGHT(p_object_id,100));
IF lockOp = 1 THEN -- acquire lock
IF lockTimeOut < 1 THEN
SET lockTimeOut = 1;
END IF;
SELECT GET_LOCK(lockName,lockTimeOut) INTO status;
ELSE -- release lock
SELECT RELEASE_LOCK(lockName) INTO status;
END IF;
END object_lock
|

DELIMITER ;

-- mysql -u root -p komadu < /home/isuru/checkouts/personal/iu_projects/d2i/komadu/service-core/config/komadu_db_schema.sql
-- GRANT ALL ON komadu.* TO 'komaduuser'@'localhost' IDENTIFIED BY 'user123';
-- GRANT SELECT ON mysql.proc TO 'komaduuser'@'localhost';

