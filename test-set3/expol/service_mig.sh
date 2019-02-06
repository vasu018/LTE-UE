if [ "$#" -ne 4 ]; then
	echo "Illegal number of parameters"
	echo "usage: ./final_tau.sh <ser_load> <tau_load> <tau_batches> <retry_timeout>"
	exit
fi

if [ $1 -eq 10000 ]
then
	load_desc="heavy"
elif [ $1 -eq 1000 ]
then
	load_desc="moderate"
elif [ $1 -eq 100 ]
then
	load_desc="light"
else
	load_desc="light"
fi

# $1 is service request load
# $2 is TAU request single batch strength
# $3 is number of batches
# $4 is delay for retry

let "sload = $1"
let "rload = $2"
let "batches = $3"
let "timeout = $4"

#logfile="logs/vasu/tau_agg_""$rload""_""$batches""_""$load_desc"".txt"
#finalMmelogfile="logs/vasu/tau_agg_""$rload""_""$batches""_""$load_desc""_mme.txt"
#mmelogfile="logs/tau_""$rload""_1.txt"
#echo "logfile is $logfile"
#echo "mmelogfile is $mmelogfile"
#cat /dev/null > $logfile
#cat /dev/null > $mmelogfile

cat /dev/null > "logs/service_1_""$sload"".txt"
cat /dev/null > logs/tau_1000_1.txt

#for number in $(eval echo "{1..$batches}")
#do
#	let "var = 1 + ($rload) * ($number -1)"
#	echo $var
#	./ue 0 1 $rload $var 10 5 $timeout
	#| tee -a $logfile
#done

let "svar = 1 + ($rload * $batches)"
./ue 10 1 1 1
#bash ./service_bg.sh $sload $svar > /dev/null &
bash ./service_bg.sh $sload $svar &
child_pid=$!
sleep 7

#for number in $(eval echo "{1..$batches}")
#do
#	let "var = 1 + ($rload) * ($number -1)"
#	echo $var
#	./ue 5 1 $rload $var 10 5 $timeout
	#| tee -a $logfile
#done
#sleep 2
./ue 11 1 1 1
kill -9 $child_pid

#cp  $mmelogfile $finalMmelogfile

 

