#!/bin/sh
JAVA_HOME=
KOMADU_CLIENT=.

cd $KOMADU_CLIENT

for i in $(ls lib |grep jar); do
	CLASSPATH=$CLASSPATH:$KOMADU_CLIENT/lib/$i
done
for j in $(ls build/lib |grep jar); do
	CLASSPATH=$CLASSPATH:$KOMADU_CLIENT/build/lib/$j
done
echo $CLASSPATH

while [ "$*" != "" ]
do
  args=$args' '$1
  shift
done
java -classpath $CLASSPATH $args
