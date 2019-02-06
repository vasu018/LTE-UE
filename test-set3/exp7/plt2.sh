#!/bin/bash

cat /dev/null > logs/attach_agg_res.txt
cat /dev/null > logs/service_agg_res.txt
cat /dev/null > logs/attach2.csv
cat /dev/null > logs/service2.csv

for number in 1000 2000 3000 4000 5000 6000 7000 8000 9000
do
	./ue 0 $number 1 1 10 0 10 > logs/attach_agg_res.txt
	./ue 1 $number 1 1 10 0 10 > logs/service_agg_res.txt
	python parse.py logs/attach_agg_res.txt logs/attach2.csv
	python parse.py logs/service_agg_res.txt logs/service2.csv
	python percentile.py "logs/attach_""$number""_1.txt" logs/attach2.csv
	python percentile.py "logs/service_""$number""_1.txt" logs/service2.csv
done
