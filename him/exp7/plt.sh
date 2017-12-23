#!/bin/bash

cat /dev/null > logs/attach_agg_res.txt
cat /dev/null > logs/service_agg_res.txt
cat /dev/null > logs/attach.csv
cat /dev/null > logs/service.csv
for number in 100 200 300 400 500 600 700 800 900
do
	./ue 0 $number 1 1 10 5 10> logs/attach_agg_res.txt
	./ue 1 $number 1 1 10 5 10> logs/service_agg_res.txt
	python parse.py logs/attach_agg_res.txt logs/attach.csv
	python parse.py logs/service_agg_res.txt logs/service.csv
	python percentile.py "logs/attach_""$number""_1.txt" logs/attach.csv
	python percentile.py "logs/service_""$number""_1.txt" logs/service.csv
	sleep 5
done

for number in 1000 2000 3000 4000 5000 6000 7000 8000 9000
do
	./ue 0 $number 1 1 10 5 10 > logs/attach_agg_res.txt
	./ue 1 $number 1 1 10 5 10 > logs/service_agg_res.txt
	python parse.py logs/attach_agg_res.txt logs/attach.csv
	python parse.py logs/service_agg_res.txt logs/service.csv
	python percentile.py "logs/attach_""$number""_1.txt" logs/attach.csv
	python percentile.py "logs/service_""$number""_1.txt" logs/service.csv
	sleep 5
done

for number in 10000 20000 30000 40000 50000
do
	./ue 0 $number 1 1 10 5 10> logs/attach_agg_res.txt
	./ue 1 $number 1 1 10 5 10> logs/service_agg_res.txt
	python parse.py logs/attach_agg_res.txt logs/attach.csv
	python parse.py logs/service_agg_res.txt logs/service.csv
	python percentile.py "logs/attach_""$number""_1.txt" logs/attach.csv
	python percentile.py "logs/service_""$number""_1.txt" logs/service.csv
	sleep 5
done
