#!/bin/bash


START=$SECONDS

echo "START: $START"

conn_count=$1

thread_count=$2

dur=$3

seed=$4

sno=$5

total_conn=`expr $conn_count \* $dur`
interval=`expr $dur \* 1000000 / $total_conn`

#sno=$4

echo "seed: $seed"
echo "conn count: $conn_count"
echo "interval: $interval"
echo "total conn: $total_conn"



./ue 1 $thread_count $total_conn $seed $interval 2 4000 > logs/ue_${seed}_${sno}.log

