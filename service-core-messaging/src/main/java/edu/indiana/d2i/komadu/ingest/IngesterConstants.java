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

import org.apache.xmlbeans.XmlOptions;

public class IngesterConstants {

    public static final XmlOptions PRETTY_PRINT_OPTS = new XmlOptions().setSavePrettyPrint();

    public static enum ProcessingStatus {
        RAW,
        PROCESSING,
        PROCESSED,
        ERROR
    }

    public static enum ProcessingFilterType {
        KNOWN_TYPES,
        UNKNOWN_TYPES;
    }

    public static final String EXPMSG_INVALID_NOTIFICATION = "Invalid notification in ";
    public static final String EXPMSG_NOT_IMPLEMENTED = "Operation not implemented for ";
    public static final String EXPMSG_MISSING_SENDER_INFO = "Missing sender information in ";
    public static final String EXPMSG_MISSING_RECEIVER_INFO = "Missing receiver information in ";
    public static final String EXPMSG_MISSING_FAULT_INFO = "Missing fault information in ";
    public static final String EXPMSG_MISSING_RESULT_INFO = "Missing result information in ";
    public static final String EXPMSG_MISSING_DATA_INFO = "Missing result or fault information in ";
    public static final String EXPMSG_ACTION_MISMATCH_NOTIFICATION_TYPE = "Action mismatch notification type in ";

}
