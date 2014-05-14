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

public class TableAttributeData {

    /**
     * enum to keep data types of the value to be inserted
     * add to this list if a new type is needed
     */
    public static enum DataType {
        STRING,
        INT,
        LONG,
        FLOAT,
        DOUBLE,
        SHORT,
        DATE,
        TIME,
        TIMESTAMP
    }

    private String attributeName;
    private Object value;
    private DataType type;

    public TableAttributeData(String attributeName, Object value, DataType type) {
        this.attributeName = attributeName;
        this.value = value;
        this.type = type;
    }

    public String getAttributeName() {
        return attributeName;
    }

    public void setAttributeName(String attributeName) {
        this.attributeName = attributeName;
    }

    public Object getValue() {
        return value;
    }

    public void setValue(Object value) {
        this.value = value;
    }

    public DataType getType() {
        return type;
    }

    public void setType(DataType type) {
        this.type = type;
    }

}
