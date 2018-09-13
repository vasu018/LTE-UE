import csv
import numpy as np
from pylab import *

def draw(Colour,expno, Label, LB,expname):
	#file=LB + '_enb_id_stats_exp_' + expno + '.csv'
	file='soumya_EVALS/' + expname + '/' + LB + '_enb_id_stats_exp_' + expno + '.csv'
	with open(file) as csvfile:
		readCSV = csv.reader(csvfile, delimiter='~')
		enb_id_lst = []
		timing_lst = []
		UE_NUM = []
		i = 0
		for row in readCSV:
			timing = row[1]
			enb_id = row[0]
		
			enb_id_lst.append(enb_id)
			timing_lst.append(float(timing)/1000)
			if float(timing)!=-1:
				i = i + 1
				UE_NUM.append(i)
			else:
				UE_NUM.append(0)
	
	timing_lst.sort()
	UE_NUM.sort()
	
	cumulative = []
	
	j = 0.00000
	
	X = []
	
	k = 0
	for i in UE_NUM:
	#    if j < len(UE_NUM):
		xval = timing_lst[k]
		k = k + 1
		j = float(i)/float(len(UE_NUM))
		if xval > 50:
			break
		if k == len(timing_lst):
			X.append(xval) 
			cumulative.append(j)
		elif xval != timing_lst[k] and xval>=0:    
			X.append(xval) 
			cumulative.append(j)
	
	#print len(timing_lst),' ',len(UE_NUM)
	#print len(cumulative)
	#print len(X)
	#print X
	#print cumulative
	
	plot(X,cumulative,linewidth=2, color=Colour, label=Label)

expno = sys.argv[1]
expname = sys.argv[2]
LB = sys.argv[3]
draw('blue','1','experiment 1',LB,expname)
#draw('red','2','experiment 2',LB,expname)
#draw('green','3','experiment 3',LB,expname)
plt.ylabel("CDF of SERVICE requests")
plt.xlabel("Latency (ms)")
plt.legend(loc='lower right')
plt.title(LB);
#xticks(np.arange(0,10,1))
yticks(np.arange(0.1,1.5,0.1))

#xscale('log')
plt.savefig(LB + '_traffic_cdf.pdf')

show()
