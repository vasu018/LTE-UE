#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "Illegal number of parameters"
	echo "usage: ./final_tau_reverse_migration.sh <src/dst> <migration_size> <run_number>"
	exit
fi

parallel=(100 1000 10000 25000 50000 75000)
printf -- "sequence array = %s\n" "${parallel[@]}"
tau_size=$2

# Before running exp, set up exp so that requests are set for migration

#Migration

exp=""
host=""
if [ "$1" == "src" ]
then
	exp="src"
	host="130.245.144.70"
else
	exp="dst"
	host="130.245.144.30"
fi

mkdir "logs/tau_reverse_logs/migration_""$tau_size"_"$3"

sleep 4
seed=$((tau_size + 1))
for element in ${parallel[@]}
do
	echo " running TAU attach for  "$element
	echo "seeding by "$seed
	ssh -l vasu -t $host "echo 'password_123' | sudo -S /home/vasu/openNetVM/examples/ue_state_client2/go.sh ""$tau_size"" 1 1" &
	sleep 0.05
	./ue 0 "$element" 1 "$seed"
	sleep 3
	seed=$((seed+element))
	mmelogfile="logs/attach_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/migration_""$tau_size"_"$3""/attach_""$element""_1_migration_""$exp"".txt"
done

sleep 4
seed=$((tau_size + 1))
for element in ${parallel[@]}
do
	echo " running TAU service for  "$element
	echo "seeding by "$seed
	ssh -l vasu -t $host "echo 'password_123' | sudo -S /home/vasu/openNetVM/examples/ue_state_client2/go.sh ""$tau_size"" 1 1" &
	sleep 0.05
	./ue 1 "$element" 1 "$seed"
	sleep 3
	seed=$((seed+element))
	mmelogfile="logs/service_""$element""_1.txt"
	cp $mmelogfile "logs/tau_reverse_logs/migration_""$tau_size"_"$3""/service_""$element""_1_migration_""$exp"".txt"
done



