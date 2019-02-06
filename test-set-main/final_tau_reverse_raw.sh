#!/bin/bash


parallel=(1000 10000 50000)
printf -- "sequence array = %s\n" "${parallel[@]}"
seed=1
for element in ${parallel[@]}
do
	echo " running for  "$element
	echo "seeding by "$seed
	./ue 0 "$element" 1 "$seed"
	sleep 4
	seed=$((seed+element))
	mmelogfile="logs/attach_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/attach_""$element""_1_raw.txt"
done

sleep 4
seed=1
for element in ${parallel[@]}
do
	echo " running for  "$element
	echo "seeding by "$seed
	./ue 1 "$element" 1 "$seed"
	sleep 4
	seed=$((seed+element))
	mmelogfile="logs/service_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/service_""$element""_1_raw.txt"
done


