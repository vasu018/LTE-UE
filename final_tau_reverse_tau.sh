#!/bin/bash


parallel=(100 1000 10000 25000 50000 75000)
printf -- "sequence array = %s\n" "${parallel[@]}"
tau_size=20000

tot=0
for i in ${parallel[@]}; do
	let tot+=$i
done

#TAU

mkdir "logs/tau_reverse_logs/migration_""$tau_size""_$1"

sleep 4
seed=1
start_seed=$seed
tau_seed=$tot
for element in ${parallel[@]}
do
	echo " running TAU attach for  "$element
	echo "seeding by "$seed
	./ue_no_write 3 $tau_size 1 $tau_seed &
	./ue 0 "$element" 1 "$seed" &
	sleep 7
	seed=$((seed+element))
	tau_seed=$(($tau_seed + $tau_size))
	mmelogfile="logs/attach_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/migration_""$tau_size""_$1""/attach_""$element""_1_tau.txt"
done

sleep 4
seed=$start_seed
for element in ${parallel[@]}
do
	echo " running TAU service for  "$element
	echo "seeding by "$seed
	./ue_no_write 3 $tau_size 1 $tau_seed &
	./ue 1 "$element" 1 "$seed" &
	sleep 7
	seed=$((seed+element))
	tau_seed=$(($tau_seed + $tau_size))
	mmelogfile="logs/service_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/migration_""$tau_size""_$1""/service_""$element""_1_tau.txt"
done



