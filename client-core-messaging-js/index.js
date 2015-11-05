/**
*Komadu Messaging JavaScript Client
*@auther {Quan Zhou}}
*/

/**
*Send provenance notification
*
*@param {Object} config
*@param {String} notification
*@param {Object} opts
*@return 
*/

module.exports = {
    sendNotification: function(config, notification, opts){
        var amqp = require('amqplib/callback_api');
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
	
		// form provenance notification
		var prov_notification = '';
		if(opts['type'] == 'FILE')
		{
		    var fs = require("fs");
    		 
    	 	    // set path and name of data file
    	            prov_notification += fs.readFileSync (notification).toString();
		}
		else if(opts['type'] == 'STRING')
		{ 
		    prov_notification += notification;	
		}

		var start = new Date().getMilliseconds();

	        ch.publish(ex, ex_key, new Buffer(prov_notification));

    		var end = new Date().getMilliseconds();
    		var execution_time = end - start;
    		console.log ("[PROV] Nofication sent successfully!");
    		console.log ("[INFO] Execution Time: "+execution_time+"ms");
		
	});

	setTimeout(function() { conn.close(); process.exit(0) }, 500);
      });		
    },

/**
*Send provenance query
*
*@param {Object} config
*@param {String} query
*@param {String} output
*@param {Object} opts
*@return
*/

    query: function(config, query, output, opts){
	var amqp = require('amqplib/callback_api');
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
    		var prov_query = '';
    		var uuid = guid();
    		prov_query += uuid+'#';
		
		if(opts['type'] == 'FILE')
		{
    			prov_query += fs.readFileSync (query).toString();
		}
		else if(opts['type'] == 'STRING')
		{
			prov_query += query;
		}
		
		// setup request exchange & routingkey
    		var request_ex = exchangename+'QueryRequest';
    		var response_ex = exchangename+'QueryResponse';
    		routingkey = routingkey +'QueryRequest';

    		//publish request and setup start timer
    		var start = new Date().getMilliseconds();
    		ch.assertExchange(request_ex, 'direct', {durable: true});
    		ch.publish(request_ex, routingkey, new Buffer(prov_query));
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
        		fs.writeFile(output, response, function(error) {
             	    	    if (error) {
                		console.error("[ERROR] File I/O Error: " + error.message);
                    	    } else {
               	 		console.log("[INFO] Query response successfully write to " + output);
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
	
	function guid()
	{
	    function s4() {
    		return Math.floor((1 + Math.random()) * 0x10000)
      		.toString(16)
      		.substring(1);
  	    }
  	    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
    		s4() + '-' + s4() + s4() + s4();
	}
    }
}

