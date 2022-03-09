#!/bin/bash
PROCESS=`ps -ef | grep python3 | awk '{print $2}'`
for i in $PROCESS
do
  kill -9 $i
done
echo "test.sh进程全部kill":
