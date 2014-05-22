#!/bin/sh

function usage
{
echo "Usage: deploy.sh <komadu_client_base_dir>"

}

if [ "$1" = "" ];
then
usage;
exit 1
fi
KOMADU_CLIENT=$1
cd $KOMADU_CLIENT
mkdir bin
for i in $(ls etc/templates/core|grep template); do
script=bin/$i
script=`echo $script|sed 's/.template/.sh/g'`
echo "#!/bin/sh
JAVA_HOME=
KOMADU_CLIENT=$KOMADU_CLIENT
" > $script
cat etc/templates/core/$i >> $script
chmod 744 $script
done

