#!/bin/bash

#service

parallel=(500 1000 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000 55000 60000)
printf -- "sequence array = %s\n" "${parallel[@]}"
#read -a file <<< $file
seed=1
for element in ${parallel[@]}
do
	echo " running for  "$element
	./ue 2 "$element" 1 "$seed"
	sleep 4
	seed=$((seed+element))
	echo "seeding by "$seed
done

mv detach_test_values.csv detach_plot3.csv

