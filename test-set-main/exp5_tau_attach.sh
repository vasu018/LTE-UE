#!/bin/sh

# exp5 TAU
# attach for the newer X, attach for the older one
./ue_no_write 0 5000 1 1 &
./ue 0 5000 1 10001 &
