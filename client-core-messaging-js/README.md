Komadu JavaScript messaging client
=========

A lightweight javascript messaging client for Komadu Provenance Toolset. This client supports sending provenance notifications and querying provenance graph. It provides command line usage and easy-to-use npm module usage which can be integrated into web UIs or other infrastructure. Please refer to github Komadu repository https://github.com/Data-to-Insight-Center/komadu or find this module on http://npmjs.org website with module name "client-core-messaging-js".

## Prerequirements

Setup Komadu Standalone Server: https://github.com/Data-to-Insight-Center/komadu

Specific guide can be found at: https://github.com/Data-to-Insight-Center/komadu/blob/master/docs/KomaduUserGuide.pdf


## Installation

    npm install client-core-messaging-js --save

## Usage -- command line usage

Command line usage requires node module "amqplib" to run.

    npm install amqplib --save

    //Sending provenance notifications
    vi ./bin/sendNotification.js  //update CLIENT_HOME path to your own path
    node ./bin/sendNotification.js <komadu.json> <notification xml>
    
    //Querying provenance graph
    vi ./bin/query.js   //update CLIENT_HOME path to your own path
    node ./bin/query.js <komadu.json> <query xml> <output path>

  One example configuration json file for Komadu messaging client is as below:

    {
     "messaging":
     {
        "username":"guest",
        "password":"guest",
        "hostname":"localhost",
        "hostport":"5672",
        "virtualhost":"/",
        "exchangename":"KomaduExchange",
        "queuename":"KomaduQueue",
        "routingkey":"KomaduKey"
     },
     "schema":
     {
        "ingest":"$CLIENT_HOME/config/komadu_ingest_schema.xsd",
        "query":"$CLIENT_HOME/config/komadu_query_schema.xsd"
     }
    }


## Usage -- node module usage

### Sending provenance notification

(1) As FILE

    var komadu_client = require('client-core-messaging-js');
    sendNotification = komadu_client.sendNotification;
    var config = require('config/komadu.json');
    var notification = <notification xml path>;
    sendNotification(config, notification, {"type":"FILE"});
    
(2) As STRING

    var komadu_client = require('client-core-messaging-js');
    sendNotification = komadu_client.sendNotification;
    var config = require('config/komadu.json');
    var notification = <notification xml string>;
    sendNotification(config, notification, {"type":"STRING"});


### Querying provnenance graph

(1) Query as FILE

    var komadu_client = require('client-core-messaging-js');
    query = komadu_client.query;
    var config = require('config/komadu.json');
    var query = <query xml path>;
    var output = <output file path>;
    query(config, query, output, {"type":"FILE"});
    
(2) Query as STRING

    var komadu_client = require('client-core-messaging-js');
    query = komadu_client.query;
    var config = require('config/komadu.json');
    var query = <query xml STRING>;
    var output = <output file path>;
    query(config, query, output, {"type":"STRING"});

## Tests
    
    npm test

## Contributing

This node module is under ISC licence, attributing to Data to Insight Center, Indiana University Bloomington. 

## Release History

* 1.0.1 Initial release
