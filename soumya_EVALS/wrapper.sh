#!/bin/bash

rm logs/attach_*.log

rm logs/ue*.log

rm logs/launcher*.log

rm logs/test_*.log

rm logs/*time.txt

LB=$1

counter=1

while [ $counter -le 1 ]
do

echo "running experiment $counter"

conf_file="conf${counter}.dat"

UE_COUNT=`grep "UE_COUNT" $conf_file | cut -d"=" -f2`

DURATION=`grep "DURATION" $conf_file | cut -d"=" -f2`

GROUP_COUNT=`grep "GROUP" $conf_file | wc -l`

PER_GROUP=`expr $UE_COUNT / $GROUP_COUNT`

#tot_conn=`expr 300 \* $DURATION`

echo "UE COUNT: $UE_COUNT DURATION: $DURATION GROUP COUNT: $GROUP_COUNT"


i=1

if [ $counter -eq 1 ]
then
	echo "starting attach"
	while [ $i -le $GROUP_COUNT ]
	do
		j=0
		while [ $j -lt 100 ]
		do
			./ue 0 1 30 $i >> logs/attach_${j}.log &
			i=`expr $i + 1`
			j=`expr $j + 1`
		done
		wait
	done

	echo "attach complete"

fi

./ue 4

sleep 1

i=0

SECONDS=0

while [ $i -lt $GROUP_COUNT ]
do
	#echo "starting group $i"
	./launch_group.sh $i $PER_GROUP $DURATION $counter > logs/launcher_${i}.log &
	i=`expr $i + 1` 

done
wait

time=`expr $SECONDS \* 1000`

echo "duration: $time ms" > ${LB}_experiment_${counter}_stats.txt

grep 'connection count:' logs/ue_*.log | cut -d":" -f3 | cut -d" " -f2 > all_conn.dat
grep 'FAIL_COUNT:' logs/ue_*.log | cut -d":" -f3 > fail_conn.dat

all_conn=0

while read line
do

all_conn=`expr $all_conn + $line`

done < all_conn.dat

fail_conn=0


while read line
do

fail_conn=`expr $fail_conn + $line`

done < fail_conn.dat

i=1

rm  ${LB}_enb_id_stats_exp_${counter}.csv

while [ $i -le 9 ]
do

	grep 'TIME' logs/${i}*time.txt | cut -d":" -f3 >> ${LB}_enb_id_stats_exp_${counter}.csv
	rm logs/${i}*time.txt
	i=`expr $i + 1`

done

#grep 'TIME' logs/*time.txt | cut -d":" -f3 >> enb_id_stats_exp_${counter}.csv
#rm logs/*time.txt

echo "TOTAL SERVICE REQUEST: $all_conn" >> ${LB}_experiment_${counter}_stats.txt
echo "FAILED SERVICE REQUEST: $fail_conn" >> ${LB}_experiment_${counter}_stats.txt

counter=`expr $counter + 1`

./ue 5

done
