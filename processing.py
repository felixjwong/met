#!/usr/bin/env python
# data.py - for python 2.7+
# Version 1.0
# MET project by Chih-Yu (Andy) Liu, Tracy Lu, and Felix Wong

# Usage: 'python data.py data.txt' at the command line
# Output: random testing numbers
#-----------------------------------------------------------------------------#

# packages
#from __future__ import print_function
import sys
import matplotlib.pyplot as plt

numberofdatafiles = 2
dataframe = []
# input graphs from files specified in command line and eliminate spaces
for inputfile in range(50,50+numberofdatafiles+1):
    z = []
    fopen = open(str(inputfile)+'.txt');
    for line in fopen.readlines():
        z.append([eval(item) for item in line.split('\t')])
    fopen.close()
    dataframe.append(z)

# the variable data has all the information, in
# [
#   [
#   [timestep,heartrate,pedo,temp],[timestep,heartrate,pedo,temp],[timestep,heartrate,pedo,temp]...
#   ],
#   ........,[....],......
# ]

# timestep vs heartrate for (51.txt 52.txt data)
a = plt.figure(1)
dataplot = [[x,y] for [x,y,z,w] in dataframe[0]]
plt.scatter(*zip(*dataplot),s=2)
dataplot = [[x,y] for [x,y,z,w] in dataframe[1]]
plt.scatter(*zip(*dataplot),s=2,marker='o', color='r')

# timestep vs pedo for (51.txt 52.txt data)
b = plt.figure(2)
dataplot = [[x,z] for [x,y,z,w] in dataframe[0]]
plt.scatter(*zip(*dataplot),s=2)
dataplot = [[x,z] for [x,y,z,w] in dataframe[1]]
plt.scatter(*zip(*dataplot),s=2,marker='o', color='r')

# timestep vs temp for (51.txt 52.txt data)
c = plt.figure(3)
dataplot = [[x,w] for [x,y,z,w] in dataframe[0]]
plt.scatter(*zip(*dataplot),s=2)
dataplot = [[x,w] for [x,y,z,w] in dataframe[1]]
plt.scatter(*zip(*dataplot),s=2,marker='o', color='r')

# show plots
a.show()
b.show()
c.show()
raw_input()
