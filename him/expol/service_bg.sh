#!/bin/bash

# service request over time
cat /dev/null > logs/serv_op
let "sload = $1"
let "offset = $2"

seed=1
./ue 0 1 $((sload))  $offset 1000 5 1000
while true
do
	./ue 1 1 $sload $offset 10 5 1000 >> logs/serv_op&
	sleep 0.01
done



