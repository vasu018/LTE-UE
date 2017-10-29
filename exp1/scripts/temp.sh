#!/bin/sh


#parallel=(1 2 3 4 5)
parallel=(1 2 3 4 5 6 7 8 9 10)
printf -- "sequence array = %s\n" "${parallel[@]}"
#read -a file <<< $file
rm *.csv
time_delay=1000 # usecs
for element in ${parallel[@]}
do
	echo " running for  "$element
	./ue 0 1 1000 "$element" "$time_delay" > "$element".txt &
done

