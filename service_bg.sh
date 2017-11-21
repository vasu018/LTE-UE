#!/bin/bash

# service request over time

let "sload = $1"
let "offset = $2"

seed=1
./ue_no_write 0 $((sload)) 1 $offset
while true
do
	./ue_no_write 1 $sload 1 $offset
done



