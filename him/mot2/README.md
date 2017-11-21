#Decomposition of MME

Objective : To prove that functional decomposition helps with making sure that new attach requests don’t get affected due to flooding of service requests.


System 1 - Stateful System:
Send x attach to MME_1, send x attach to MME_2. Then send Service request for all attached UEs. Tabulate latency for both attach and service
Send x attach to MME_1, send x attach to MME_2. Tabulate latency for both attach.
Send x extra attach requests and 2x service requests for the 2x in (1) together. Tabulate attach latency for 
a. the x new attach requests 
b. The 2x service requests

 Expected: 
Attach latency for Step 1 & 2 should be similar
Latency for Step 3a and 3b should be more than in Step 1.
 

System 2 - Stateless Non decomposed:
Send 2x attach to MME_1 and MME_2. Then send Service request for all attached UEs. Tabulate latency for both attach and service
Send 2x attach to MME_1 and MME_2. Tabulate latency for attach.
Send x extra attach requests and 2x service requests for the 2x in (1) together. Tabulate attach latency for 
a. the x new attach requests 
b. The 2x service requests

 Expected: 
Attach latency for Step 1 & 2 should be similar
Latency for Step 3a and 3b should be more than Step 1.


System 3 - Stateless Decomposed:
Send 2x attach to AMME. Then send Service request for all attached UEs to SMME. Tabulate latency for both attach and service
Send 2x attach to AMME. Tabulate latency for attach.
Send x extra attach requests and 2x service requests for the 2x in (1) together. Tabulate attach latency for 
a. the x new attach requests 
b. The 2x service requests

 Expected: 
Attach latency for Step 1 & 2 should be similar but more than System 1 and 2
Latency for Step 3a should be similar to Step 1 and Step 3b should be more than Step 1.
Repeat above for x=100,300,500,1000,1500,2000,2500 and so on.

Plots:

CDF of attach requests in Step 3a with latency on x-Axis
CDF of service requests in Step 3b with latency on x-Axis

