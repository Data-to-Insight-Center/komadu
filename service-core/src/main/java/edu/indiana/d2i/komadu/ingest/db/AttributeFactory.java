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

import java.util.HashMap;

public class AttributeFactory {

    protected static HashMap<String, AttributeDefinitionScopeEnum> attributeScopeDictionary = null;

    public static enum AttributeDefinitionScopeEnum {
        PROV_ATTRIBUTE,
        KOMADU_ATTRIBUTE,
        EXTERNAL_SOURCE
    }

    public static void addScopeDefinition(String property, AttributeDefinitionScopeEnum scope) {
        if (attributeScopeDictionary == null) {
            attributeScopeDictionary = new HashMap<String, AttributeDefinitionScopeEnum>();
        }
        attributeScopeDictionary.put(property, scope);
    }

    public static AttributeDefinitionScopeEnum getScopeDefinition(String property) {
        AttributeDefinitionScopeEnum scope = attributeScopeDictionary.get(property);
        if (scope == null)
            scope = AttributeDefinitionScopeEnum.EXTERNAL_SOURCE;
        return scope;
    }
}
