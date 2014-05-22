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

import edu.indiana.d2i.komadu.ingest.NotificationSummary;
import edu.indiana.d2i.komadu.ingest.NotificationSummary.NotificationTypeEnum;
import edu.indiana.d2i.komadu.ingest.StoredRawNotification;

public class BaseDBStoredRawNotification implements StoredRawNotification<Long, String> {

    protected Long internalID;
    protected String notification;
    protected NotificationTypeEnum notificationType;

    public BaseDBStoredRawNotification(Long internalID, NotificationTypeEnum notificationType, String notification) {
        this.internalID = internalID;
        this.notificationType = notificationType;
        this.notification = notification;
    }

    public Long getInternalID() {
        return internalID;
    }

    public String getNotification() {
        return notification;
    }

    public NotificationSummary.NotificationTypeEnum getNotificationType() {
        return notificationType;
    }

}
