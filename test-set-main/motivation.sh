#!/bin/sh

# run ue for attach 200000 serial.

# run ue for service 200000 serial with 10 usec gaps. (2000 msec experiment)
# run another bunch of 10k attach at 200th msec and 800th msec 
# these attach requests will be in serial with 1 usec gap in between
# that means that they will get over in 100 msec

#./ue 0 1 200000 1 5

./ue 1 1 200000 1 5 &
sleep 1
./ue 0 1 10000 2 1&
sleep 10
./ue_no_write 0 10000 1 10004 &



