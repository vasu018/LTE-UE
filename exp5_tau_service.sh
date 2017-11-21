#!/bin/sh

# exp5 TAU
# attach for the newer X, attach for the older one
./ue_no_write 0 5000 1 20001 &
./ue 1 5000 1 10001 &
