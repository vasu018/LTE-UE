#!/bin/bash

cat /dev/null > logs/attach_agg_res.txt
cat /dev/null > logs/service_agg_res.txt
cat /dev/null > logs/attach3.csv
cat /dev/null > logs/service3.csv
for number in 10000 20000 30000 40000 50000
do
	./ue 0 $number 1 1 10 0 10> logs/attach_agg_res.txt
	./ue 1 $number 1 1 10 0 10> logs/service_agg_res.txt
	python parse.py logs/attach_agg_res.txt logs/attach3.csv
	python parse.py logs/service_agg_res.txt logs/service3.csv
	python percentile.py "logs/attach_""$number""_1.txt" logs/attach3.csv
	python percentile.py "logs/service_""$number""_1.txt" logs/service3.csv
done
