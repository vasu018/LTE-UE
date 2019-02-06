#!/bin/bash

#service

parallel=(500 1000 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000 55000 60000)
printf -- "sequence array = %s\n" "${parallel[@]}"
#read -a file <<< $file
rm service_test_values.csv
seed=1
for element in ${parallel[@]}
do
	echo " running for  "$element
	./ue 1 "$element" 1 "$seed"
	sleep 4
	seed=$((seed+element))
	echo "seeding by "$seed
done

mv service_test_values.csv service_plot2.csv

