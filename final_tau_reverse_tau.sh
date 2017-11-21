#!/bin/bash


parallel=(1000 10000 50000)
printf -- "sequence array = %s\n" "${parallel[@]}"

tot=0
for i in ${parallel[@]}; do
	let tot+=$i
done

#TAU

sleep 4
seed=1
start_seed=$seed
tau_seed=$tot
for element in ${parallel[@]}
do
	echo " running TAU attach for  "$element
	echo "seeding by "$seed
	./ue 0 "$element" 1 "$seed" &
	./ue_no_write 3 5000 1 $tau_seed
	sleep 4
	seed=$((seed+element))
	tau_seed=$(($tau_seed + 5000))
	mmelogfile="logs/attach_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/attach_""$element""_1_tau.txt"
done

sleep 4
seed=$start_seed
for element in ${parallel[@]}
do
	echo " running TAU service for  "$element
	echo "seeding by "$seed
	./ue 1 "$element" 1 "$seed"
	./ue_no_write 3 5000 1 $tau_seed
	sleep 4
	seed=$((seed+element))
	tau_seed=$(($tau_seed + 5000))
	mmelogfile="logs/service_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/service_""$element""_1_tau.txt"
done



