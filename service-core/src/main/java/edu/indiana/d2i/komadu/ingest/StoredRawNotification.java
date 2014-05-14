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
 * Interface for representing a raw notification which was stored in the database
 * and retrieved later
 *
 * @param <K> notification id
 * @param <V> full raw notification
 */

public interface StoredRawNotification<K, V> {
    public K getInternalID();
    public V getNotification();
    public NotificationSummary.NotificationTypeEnum getNotificationType();
}
