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

/**
 * A Bean to be used to return results after activity, agent or entity insertion
 */
public class IngestionResult {
    private String actualId;
    private Long dbId;

    public IngestionResult(String actualId, Long dbId) {
        this.actualId = actualId;
        this.dbId = dbId;
    }

    public String getActualId() {
        return actualId.trim();
    }

    public Long getDbId() {
        return dbId;
    }
}
