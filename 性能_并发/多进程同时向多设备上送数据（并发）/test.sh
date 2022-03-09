#!/bin/bash
for i in {1..6000}
do
  a=snjj
  b=${a}${i}
  python3 /home/liufei/test/snj_simulator.py ${b} &
  echo ${i}
done
