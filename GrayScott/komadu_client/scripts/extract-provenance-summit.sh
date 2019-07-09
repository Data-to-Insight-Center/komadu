#!/bin/bash

BASE_DIR=/ccs/home/swithana/komadu_system
ERLANG_HOME=/ccs/home/swithana/programs/erlang
VENV_ENV=/ccs/home/swithana/venv-sachith
DATA_PATH=
export PYTHONPATH=$PYTHONPATH:/ccs/home/swithana/komadu_system/GrayScott


if [ -z "$1" ]
  then
    DATA_PATH=$PWD
  else
    DATA_PATH=$1
fi

echo "Provenance extraction data path:" $DATA_PATH

# ========== Starting the services ================

echo "Starting RabbitMQ..."
. $ERLANG_HOME/activate
$BASE_DIR/rabbitmq/sbin/rabbitmq-server &
RABBIT_PID=$!

echo "Starting MySQL..."
$BASE_DIR/mysql/mysql.server.sh start &
MYSQL_PID=$!
sleep 5s

echo "Starting Komadu..."
$BASE_DIR/komadu/bin/KomaduServer.sh $BASE_DIR/komadu/config/komadu.properties &
KOMADU_PID=$!
sleep 5s

source $VENV_ENV/bin/activate
python $BASE_DIR/GrayScott/komadu_client/main.py --static $1
sleep 20s

# ========== Stopping the services ================
echo "Stopping Komadu..."
kill -9  $KOMADU_PID
sleep 10s

echo "Stopping RabbitMQ..."
$BASE_DIR/rabbitmq/sbin/rabbitmqctl stop
echo "Stopping MySQL..."
$BASE_DIR/mysql/mysql.server.sh stop

sleep 5s
kill $RABBIT_PID
kill $MYSQL_PID