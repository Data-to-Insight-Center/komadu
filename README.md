komadu
======

Provenance Collection and Visualization Tool

Komadu is a redesign of Karma (OPM based provenance implementation) which supports the W3C PROV 
specification. It comes with a new Client API which aligns with the W3C PROV standards. This Client API 
is more generalized and supports capturing any kind of provenance. 

Following is a quick start guide for Komadu. More information can be found in docs/KomaduUserGuide.pdf.

User Guide
==========

Software Dependencies
---------------------

1. Apache Maven 3.0 or higher
2. MySQL database server 5.1
3. MySQL Connector/JDBC 5.1 or higher
4. JDK 1.6 or higher
5. Apache XML Beans 2.3.0
6. Apache Tomcat 6.0.x or higher
7. Apache Axis2 1.6.2

Building the Source
-------------------

1. Download ProvToolbox-0.4.0 from https://github.com/lucmoreau/ProvToolbox/releases. 
    Build (mvn clean install) prov-model and prov-xml modules under it using Maven.

2. Check out the Komadu code from the git repository.
    git clone https://github.iu.edu/isuriara/komadu.git komadu

3. Edit the services.xml file found under service-core-aar/src/main/resources/META-INF and set the correct 
    path in the "komadu.properties.file.path" parameter.

4. Build Komadu. You have to skip the test cases till we deploy Komadu on Tomcat.
    mvn clean install -Dmaven.test.skip=true

Set up Komadu Database
----------------------

1. Log into MySQL as admin
    mysql -u root -p

2. Create Komadu Database
    CREATE DATABASE komadu;

3. Grant permissions
    GRANT ALL ON komadu.* TO 'komaduuser'@'localhost' IDENTIFIED BY 'komadupwd';
    GRANT SELECT ON mysql.proc TO 'komaduuser'@'localhost';

4. Execute the Komadu database schema
    mysql -u root -p karma < {komadu_checkout_path}/service-core/config/komadu_db_schema.sql

Configure Komadu Properties
---------------------------

Edit the "komadu.properties" file at the path that you set in the services.xml and configure the 
following required parameters.
    log4j.properties.path
    database.location
    database.username
    database.password

Set up Tomcat and deploy Komadu service
---------------------------------------

1. Download Apache Axis2 1.6.2 war file and extract it. 
2. Copy it to {your_tomcat_home}/webapps directory and start Tomcat once and then shut it down.
3. Copy {komadu_checkout_path}/service-core-aar/target/komadu-service-1.0.aar file to 
    {your_tomcat_home}/webapps/axis2/WEB-INF/services directory.
4. Download and copy mysql-connection-java-5.1.x-bin.jar to {your_tomcat_home}/lib
5. Create a directory {your_tomcat_home}/endorsed and copy following 2 jar files into it. You can find these
    jars in your local maven repository.
    {your_home}/.m2/repository/javax/xml/bind/jaxb-api/2.2.4/jaxb-api-2.2.4.jar  
    {your_home}/.m2/repository/com/sun/xml/bind/jaxb-impl/2.1.10/jaxb-impl-2.1.10.jar
6. Start Tomcat.

Executing Test Cases
--------------------

Once you have successfully deployed Komadu on Tomcat, you can execute the test cases through maven.

1. Move into axis2-client-core
2. Execute the command 'mvn clean install -o'
