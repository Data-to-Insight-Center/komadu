#!/usr/bin/env node
var komadu_client = require('../index');
sendNotification = komadu_client.sendNotification;
query = komadu_client.query;

var config = require('../config/komadu.json');

sendNotification(config, './samples/activity_activity.xml',{"type":"FILE"});
query(config,'./samples/query_activity_graph.xml','output.xml',{"type":"FILE"});

