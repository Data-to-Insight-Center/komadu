#!/bin/sh

SRC_JAVA=./src
BUILD=$(pwd)/target
LIB=$(pwd)/target/dependency
CLASSES=$BUILD/classes:$BUILD/generated-code/resources
BIN=$(pwd)/bin
RETVAL=0
prog="build.sh"

###################################################################

build() {
    mvn clean install -Dmaven.test.skip=true
    mvn dependency:copy-dependencies
    mkdir bin

for i in $(ls $LIB |grep ".jar"); do
        CLASSES=$CLASSES:$LIB/$i
done

for i in $(ls $BUILD |grep ".jar"); do
        CLASSES=$CLASSES:$BUILD/$i
done

echo "
#!/bin/sh
CLASSES=$CLASSES
" > ./bin/KomaduServer.sh

echo '
if [ "$1" = "" ];
then
    echo
    echo "#########################################"
    echo "#            KomaduServer.sh            #"
    echo "#########################################"
    echo
    echo "$ KomaduServer.sh <properties_file>"
    echo
    exit 1
fi

echo
echo "Komadu standalone server started..."
echo "Listening for incoming messages..."
echo

CP=:$CLASSPATH:$CLASSES:.
java -classpath $CP  edu.indiana.d2i.komadu.util.ServiceLauncher $1

# For debugging
#java -classpath $CP  -Xdebug -Xrunjdwp:transport=dt_socket,address=5005,server=y,suspend=y edu.indiana.d2i.komadu.util.ServiceLauncher $1
' >> ./bin/KomaduServer.sh
chmod 755 ./bin/KomaduServer.sh




	return $RETVAL
}
###################################################################
clean(){
	rm -rf $BIN
	mvn clean
	return $RETVAL
}
###################################################################
case "$1" in
  clean)
        clean
        ;;
  *)
        clean
        build
        RETVAL=$?
        ;;
esac

exit $RETVAL

