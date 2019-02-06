if [ "$#" -ne 5 ]; then
	echo "Illegal number of parameters"
	echo "usage: ./final_tau.sh <ser_load> <tau_load> <tau_batches> <retry_timeout> "
	exit
fi
# $1 is service request load
# $2 is TAU request single batch strength
# $3 is number of batches
# $4 is delay for retry

let "sload = $1"
let "rload = $2"
let "batches = $3"
let "timeout = $4"

#logfile="logs/amos/tau_agg_""$rload""_""$batches""_""$load_desc"".txt"
#finalMmelogfile="logs/amos/tau_agg_""$rload""_""$batches""_""$load_desc""_mme.txt"
#mmelogfile="logs/tau_""$rload""_1.txt"
#echo "logfile is $logfile"
#echo "mmelogfile is $mmelogfile"
#cat /dev/null > $logfile
#cat /dev/null > $mmelogfile

cat /dev/null > "logs/service_1_""$sload"".txt"
cat /dev/null > "logs/detach_1_""$rload"".txt"
cat /dev/null > "logs/attach_1_""$rload"".txt"

let "svar = 1 + ($rload * $batches)"

if [ 0 ]
then
	for number in $(eval echo "{1..$batches}")
	do
		let "var = 1 + ($rload) * ($number -1)"
		echo $var
		./ue 0 1 $rload $var 100 5 $timeout
		#| tee -a $logfile
	done
fi


./ue 10 1 1 1
#bash ./service_bg.sh $sload $svar > /dev/null &
bash ./service_bg.sh $sload $svar &
child_pid=$!
sleep 5

if [ 0 ]
then
	for number in $(eval echo "{1..$batches}")
	do
		let "var = 1 + ($rload) * ($number -1)"
		echo $var
		./ue 2 1 $rload $var 10 5 $timeout
	#| tee -a $logfile
	done
else
	for number in $(eval echo "{1..$batches}")
	do
		let "var = 1 + ($rload) * ($number -1)"
		echo $var
		./ue 0 1 $rload $var 10 5 $timeout
		#| tee -a $logfile
	done
fi
sleep 1
./ue 11 1 1 1
kill -9 $child_pid

#cp  $mmelogfile $finalMmelogfile

 

