#!/bin/bash


group_num=$1

PER_GROUP=$2

DURATION=$3

expno=$4

j=0

conf_file="conf${expno}.dat"

seed=`expr $group_num + 1`
conn_count=`grep "GROUP~$seed~" $conf_file | cut -d"~" -f3`

loop_count=`expr $PER_GROUP / 1`
rem=`expr $PER_GROUP % 1`
echo "conn count: $conn_count"
echo "seed $seed"
while [ $j -lt $loop_count ]
do
        seed=`expr $group_num + 1`
        ./test_skewed_chash.sh $conn_count 1 $DURATION $seed $j > logs/test_${seed}_${j}.log &
        j=`expr $j + 1`
done

if [ $rem -gt 0 ]
then
	./test_skewed_chash.sh $conn_count $rem $DURATION $seed $j > logs/test_${seed}_${j}.log &

fi
wait

