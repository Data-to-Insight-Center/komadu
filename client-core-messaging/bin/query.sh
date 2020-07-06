#!/bin/sh
JAVA_HOME=
KOMADU_CLIENT=.

cd $KOMADU_CLIENT

if [ "$3" = "" ];
then
    echo "Usage: query.sh <komadu configuration file> <query xml file> <output file>"
    exit 1
fi
for i in $(ls lib |grep jar); do
	CLASSPATH=$CLASSPATH:$KOMADU_CLIENT/lib/$i
done
for j in $(ls build/lib |grep jar); do
	CLASSPATH=$CLASSPATH:$KOMADU_CLIENT/build/lib/$j
done
#echo $CLASSPATH
java -classpath $CLASSPATH edu.indiana.d2i.komadu.client.messaging.Query $1 $2 > $3
