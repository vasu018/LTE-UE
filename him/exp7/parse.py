import sys
final_list = []
with open(sys.argv[1]) as f:
    for line in f:
        list_line = line.split()
        if (len(list_line) == 0):
            continue
	if (list_line[0] == "Attach" and list_line[1] =="Total"):
            average  = float(list_line[3])
            final_list.append((average, total, attempt, success))
        if (list_line[0] == "Total" and list_line[1] =="Time"):
            total = float(list_line[7])
        if (list_line[0] == "ATTACH_ATTEMPT" or list_line[0] == "SERVICE_ATTEMPT"):
            attempt = float(list_line[2])
        if (list_line[0] == "ATTACH_ACCEPT_COMPLETE_SENT" or list_line[0] == "SERVICE_ACCEPT_COMPLETE_SENT"):
            success = float(list_line[2])

thefile = open(sys.argv[2], 'a')
for item in final_list:
    thefile.write("%s, "%item[0])
    thefile.write("%s, "%item[1])
    thefile.write("%s, "%item[2])
    thefile.write("%s, "%item[3])
