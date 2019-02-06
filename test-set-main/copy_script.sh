#!/bin/bash


parallel=( 100 1000 10000 25000 50000)
printf -- "sequence array = %s\n" "${parallel[@]}"

seed=1
for element in ${parallel[@]}
do
	mmelogfile="logs/attach_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/migration_10000/attach_""$element""_1_""$1"".txt"
done

sleep 4
for element in ${parallel[@]}
do
	mmelogfile="logs/service_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/migration_10000/service_""$element""_1_""$1"".txt"
done



