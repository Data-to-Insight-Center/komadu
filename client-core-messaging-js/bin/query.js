#!/usr/bin/env node

var client_home = '/Users/quzhou/Komadu/komadu/client-core-messaging-js';

var amqp = require('amqplib/callback_api');

if(process.argv.length<4)
{
    console.log('Usage:\nnode query.js <komadu.json> <query xml> <output path>');
    process.exit(0);
}

var config_path = process.argv[2];
var query_path = client_home+'/'+process.argv[3];
var output_path = client_home+'/'+process.argv[4];
var config = require(client_home+'/'+config_path);

var username = config.messaging.username;
var password = config.messaging.password;
var hostname = config.messaging.hostname;
var hostport = config.messaging.hostport;
var virtualhost = config.messaging.virtualhost;
var exchangename = config.messaging.exchangename;
var queuename = config.messaging.queuename;
var routingkey = config.messaging.routingkey;

var amqp_url = 'amqp://'+username+':'+password+'@'+hostname+':'+hostport+virtualhost;

amqp.connect(amqp_url, function(err, conn) {
  conn.createChannel(function(err, ch) {
    var response_queuename = queuename + 'QueryResponse';
    
    var fs = require("fs");
    // form provenance query
    var query = '';
    var uuid = guid();
    query += uuid+'#';
    query += fs.readFileSync (query_path).toString();

    // setup request exchange & routingkey
    var request_ex = exchangename+'QueryRequest';
    var response_ex = exchangename+'QueryResponse';
    routingkey = routingkey +'QueryRequest';
    
    //publish request and setup start timer
    var start = new Date().getMilliseconds();
    ch.assertExchange(request_ex, 'direct', {durable: true});
    ch.publish(request_ex, routingkey, new Buffer(query));
    console.log ("[PROV] Query sent sucessfully!");

    // setup response exchange
    ch.assertExchange(response_ex, 'direct', {durable: false});

    ch.assertQueue(response_queuename, {exclusive: true}, function(err, q) {
      console.log("[INFO] Waiting for response...");
        ch.bindQueue(q.queue, response_ex, uuid);
      ch.consume(q.queue, function(msg) {
        console.log("[PROV] Query response received:\n"+msg.content.toString());
  	
	//write query response to output file
	var response = msg.content.toString();
	fs.writeFile(output_path, response, function(error) {
             if (error) {
                console.error("[ERROR] File I/O Error: " + error.message);
     		} else {
       		console.log("[INFO] Query response successfully write to " + output_path);
     		}

	     //setup end timer and log execution time
             var end = new Date().getMilliseconds();
             var execution_time = end - start;
             console.log("[INFO]Execution time: "+execution_time+"ms");
             process.exit(0);	
  	});
      }, {noAck: true});
    });
  });

  setTimeout(function() { conn.close(); process.exit(0) }, 5000);
});

function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
    s4() + '-' + s4() + s4() + s4();
}













