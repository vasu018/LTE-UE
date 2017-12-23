#!/bin/bash

#attach for new x and service for earlier x
./ue 0 1 10000 1 100
./ue1 1 1 10000 1 10000 5 1000 &
./ue2 1 1 10000 1 10000 5 1000
#sleep 22
./ue2 0 1 10000 10001 1000 5 1000 

