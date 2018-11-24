#!/bin/bash
python createDynamoDbTable.py
trap "exit" INT
while true
do
  ./heartbeat.sh -e
  sleep 60
done
trap 'exit 143' SIGTERM # exit = 128 + 15 (SIGTERM)
tail -f /dev/null & wait ${!}
