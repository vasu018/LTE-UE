./ue 0 20 100 3 0 0 1000 1
./ue 0 20 100 3 0 0 1000 3
./ue 0 20 100 3 0 0 1000 4
./ue 0 20 100 3 0 0 1000 5

sleep 1

./ue 1 20 100 3 0 0 1000 1 &
./ue 1 20 100 3 0 0 1000 3 &
./ue 1 20 100 3 0 0 1000 4 &
./ue 1 20 100 3 0 0 1000 5
sleep 10
#wait for logs to be written
cp logs/service_20_100_1.txt logs/nice_testing/varied/service_20_100_1.txt
cp logs/service_20_100_3.txt logs/nice_testing/varied/service_20_100_3.txt
cp logs/service_20_100_4.txt logs/nice_testing/varied/service_20_100_4.txt
cp logs/service_20_100_5.txt logs/nice_testing/varied/service_20_100_5.txt


