#!/usr/bin/env node
var client_home = '/Users/quzhou/Komadu/komadu/client-core-messaging-js';

var amqp = require('amqplib/callback_api');

if(process.argv.length<4)
{
    console.log('Usage:\nnode sendNotification.js <komadu.json> <notification xml>');
    process.exit(0);
}

var config_path = process.argv[2];
var notification_path = process.argv[3];
var config = require(client_home+'/'+config_path);

var username = config.messaging.username;
var password = config.messaging.password;
var hostname = config.messaging.hostname;
var hostport = config.messaging.hostport;
var virtualhost = config.messaging.virtualhost;
var exchangename = config.messaging.exchangename;
var routingkey = config.messaging.routingkey;

var amqp_url = 'amqp://'+username+':'+password+'@'+hostname+':'+hostport+virtualhost;

amqp.connect(amqp_url, function(err, conn) {
  conn.createChannel(function(err, ch) {
    var ex = exchangename + '_Notification';
    var ex_key = routingkey + '_Notification';

    ch.assertExchange(ex, 'direct', {durable: true});

    var fs = require("fs");
    // form provenance notification
    var notification = '';    

    // set path and name of data file
    notification_path = client_home+'/'+notification_path;
    notification += fs.readFileSync (notification_path).toString();

    var start = new Date().getMilliseconds();
    
    ch.publish(ex, ex_key, new Buffer(notification));

    var end = new Date().getMilliseconds();
    var execution_time = end - start;
    console.log ("[PROV] Nofication sent successfully!");
    console.log ("[INFO] Execution Time: "+execution_time+"ms");
  });

  setTimeout(function() { conn.close(); process.exit(0) }, 500);
});
