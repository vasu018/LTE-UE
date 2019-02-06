#!/bin/bash

# service request over time

let "sload = $1"
let "offset = $2"

seed=1
./ue_no_write 0 $((sload)) 1 $offset 5 1000
while true
do
	./ue_no_write 1 $sload 1 $offset 5 1000&
	sleep 2.4
done



