#!/bin/sh


rm attach.log

rm logs/ue_*.log

i=1


#while [ $i -le 10 ]
#do
./ue 0 50 300 $i >> attach.log
#i=`expr $i + 1`
#done

i=1

while [ $i -le 50 ]
do

./ue 1 10 200 1 4000 > logs/ue_${i}.log &

i=`expr $i + 1`

done
