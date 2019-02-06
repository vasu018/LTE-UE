if [ "$#" -ne 3 ]; then
	echo "Illegal number of parameters"
	echo "usage: ./final_tau.sh <ser_load> <tau_load> <tau_batches>"
	exit
fi

if [ $1 -eq 1000 ]
then
	load_desc="heavy"
elif [ $1 -eq 100 ]
then
	load_desc="moderate"
elif [ $1 -eq 10 ]
then
	load_desc="light"
else
	exit
fi

# $1 is service request load
# $2 is TAU request single batch strength
# $3 is number of batches

let "sload = $1"
let "rload = $2"
let "batches = $3"

logfile="logs/vasu/tau_agg_""$rload""_""$batches""_""$load_desc"".txt"
finalMmelogfile="logs/vasu/tau_agg_""$rload""_""$batches""_""$load_desc""_mme.txt"
mmelogfile="logs/tau_""$rload""_1.txt"
echo "logfile is $logfile"
echo "mmelogfile is $mmelogfile"
cat /dev/null > $logfile
cat /dev/null > $mmelogfile


let "svar = 1 + ($rload * $batches)"

bash ./service_bg.sh $sload $svar > /dev/null &
child_pid=$!

for number in $(eval echo "{1..$batches}")
do
	let "var = 1 + ($rload) * ($number -1)"
	echo $var
	./ue 3 $rload 1 $var 1 5 700 | tee -a $logfile
done

kill -9 $child_pid

cp  $mmelogfile $finalMmelogfile



