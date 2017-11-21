#!/bin/bash

#attach

parallel=(500 1000 5000 10000 15000 20000 25000 30000)
printf -- "sequence array = %s\n" "${parallel[@]}"
#read -a file <<< $file
rm attach_test_values.csv
seed=1
for element in ${parallel[@]}
do
	echo " running for  "$element
	./ue 0 "$element" 1 "$seed"
	sleep 4
	seed=$((seed+element))
	echo "seeding by "$seed
done

mv attach_test_values.csv attach_plot1.csv


