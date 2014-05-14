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

import java.util.ArrayList;
import java.util.List;

/**
 * A Bean to represent a Tuple to be inserted into a Table
 */
public class TupleData {

    private List<TableAttributeData> attributeList = new ArrayList<TableAttributeData>();

    public void addAttribute(TableAttributeData attribute) {
        attributeList.add(attribute);
    }

    public void addAttribute(String name, Object value, TableAttributeData.DataType type) {
        attributeList.add(new TableAttributeData(name, value, type));
    }

    public void removeAttribute(TableAttributeData attribute) {
        attributeList.remove(attribute);
    }

    public List<TableAttributeData> getAttributeList() {
        return attributeList;
    }

}
