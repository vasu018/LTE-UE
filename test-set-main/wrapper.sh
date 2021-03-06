#!/bin/bash

rm logs/attach_*.log

rm logs/ue*.log

rm logs/launcher*.log

rm logs/test_*.log

rm logs/*time.txt

LB=$1

exp_name=$2

mkdir soumya_EVALS/${exp_name}

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

rm temp_run.sh

while [ $i -lt $GROUP_COUNT ]
do
	seed=`expr $i + 1`
	conn_count=`grep "GROUP~$seed~" $conf_file | cut -d"~" -f3`
	total_conn=`expr $conn_count \* $DURATION`
	interval=`expr $DURATION \* 60000000 / $total_conn`
	#echo "starting group $i"
	#echo "./launch_group.sh $i $PER_GROUP $DURATION $counter $conn_count > logs/launcher_${i}.log &" >> temp_run.sh
	echo "./ue 1 1 $total_conn $seed $interval 2 300 > logs/ue_${seed}_${i}.log &" >> temp_run.sh
	i=`expr $i + 1` 

done

echo "wait" >> temp_run.sh

date


chmod 777 temp_run.sh
./temp_run.sh

date

wait

./ue 5

time=`expr $SECONDS \* 1000`

echo "duration: $time ms" > soumya_EVALS/${exp_name}/${LB}_experiment_${counter}_stats.txt

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

rm  soumya_EVALS/${exp_name}/${LB}_enb_id_stats_exp_${counter}.csv

while [ $i -le 9 ]
do

	grep 'TIME' logs/${i}*time.txt | cut -d":" -f3 >> soumya_EVALS/${exp_name}/${LB}_enb_id_stats_exp_${counter}.csv
	rm logs/${i}*time.txt
	i=`expr $i + 1`

done

#grep 'TIME' logs/*time.txt | cut -d":" -f3 >> enb_id_stats_exp_${counter}.csv
#rm logs/*time.txt

echo "TOTAL SERVICE REQUEST: $all_conn" >> soumya_EVALS/${exp_name}/${LB}_experiment_${counter}_stats.txt
echo "FAILED SERVICE REQUEST: $fail_conn" >> soumya_EVALS/${exp_name}/${LB}_experiment_${counter}_stats.txt

counter=`expr $counter + 1`

./ue 5

done
