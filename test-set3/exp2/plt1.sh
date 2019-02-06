#!/bin/bash

#attach for new x and service for earlier x

./ue 0 10000 1 $1 &
./ue 1 10000 1 1 &

