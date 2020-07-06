#!/bin/sh
JAVA_HOME=
KOMADU_CLIENT=.

cd $KOMADU_CLIENT

if [ "$2" = "" ];
then
    echo "Usage: sendNotification.sh <komadu configuration file> <notification xml file>"
    exit 1
fi
for i in $(ls lib |grep jar); do
	CLASSPATH=$CLASSPATH:$KOMADU_CLIENT/lib/$i
done
for j in $(ls build/lib |grep jar); do
	CLASSPATH=$CLASSPATH:$KOMADU_CLIENT/build/lib/$j
done
#echo $CLASSPATH
java -classpath $CLASSPATH edu.indiana.d2i.komadu.client.messaging.Notification $1 $2
