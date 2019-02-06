#!/bin/bash

# service request over time

let "sload = $1"
let "offset = $2"

seed=1
while true
do
	./ue_no_write 3 $sload 1 $offset&
	sleep 0.1
done



