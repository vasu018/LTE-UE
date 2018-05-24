#!/usr/bin/python


# Generate latency Data
flatency = open('./latency_datasf.txt', 'w')

dataLatency = []
dataLatencysf = []
with open("./latency_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        y = float(words[5])
        print x, y
        
