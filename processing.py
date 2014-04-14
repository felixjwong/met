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

currenttime = eval(sys.argv[1])
timerange = 10
numberofdatafiles = 20


dataframe = []
# input graphs from files specified in command line and eliminate spaces
for inputfile in range(1,numberofdatafiles+1):
    z = []
    fopen = open('./data/'+str(inputfile)+'.txt');
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


import math
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pylab.figure()
ax = Axes3D(fig)


flat = [item for sublist in dataframe for item in sublist]
timedata = []
#timedata = [i for i in flat if abs(i[0]-currenttime) <= timerange]
for i in flat:
    if abs(i[0]-currenttime) <= timerange:
        if i[0] == currenttime - timerange:
            normalize =i[4]
        timedata.append([i[0],i[1],i[2],i[3],i[4]-normalize])
print timedata


x1_var = [y for [x,y,z,w,v] in timedata]
x2_var = [z for [x,y,z,w,v] in timedata]
x3_var = [w for [x,y,z,w,v] in timedata]
d_var = [v for [x,y,z,w,v] in timedata]
t_var = [x for [x,y,z,w,v] in timedata]


ax.scatter(x1_var, x2_var, x3_var)



import numpy as np
X = np.array([(x1_var[i], x2_var[i],x3_var[i]) for i in range(len(timedata))])






from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq

# data generation

# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(X,5)
# assign each sample to a cluster
idx,_ = vq(X,centroids)


ax.scatter(x1_var, x2_var, x3_var,s = .1,facecolors='none', edgecolors='b')
ax.scatter(centroids[:,0],centroids[:,1],centroids[:,2],marker='D', color='g')











from scipy.spatial import ConvexHull

hull = ConvexHull(X)
hull_points = hull.vertices

Y = hull.points[np.unique(hull.simplices)]

y1_var = [x for [x,y,z] in Y]
y2_var = [y for [x,y,z] in Y]
y3_var = [z for [x,y,z] in Y]



yd_var = []
yt_var = []
for i in np.unique(hull.simplices):
    yd_var.append(d_var[i])
    yt_var.append(t_var[i])


drange = max(yd_var)-min(yd_var)
tmap = [float(yd_var[i]*100000/drange/yt_var[i]) for i in range(len(yd_var))]

for i in range(0,len(y1_var)):
    print yt_var[i],y1_var[i], y2_var[i], y3_var[i],yd_var[i],tmap[i]

ax.scatter(y1_var, y2_var, y3_var, marker = '*',s = 150, c=tmap, cmap=plt.cm.jet)
pyplot.show()











"""
# some plotting using numpy's logical indexing
plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
show()
"""




"""
    
    #  heartrate + temperature for (1.txt 2.txt data in time range)
    a = plt.figure(1)
    dataplot = [[y,z] for [x,y,z,w,v] in timedata]
    plt.scatter(*zip(*dataplot),s=2,marker='o', color='r')
    a.show()
    raw_input()
    
    
    
    
    # timestep vs heartrate for (1.txt 2.txt data)
    a = plt.figure(1)
    dataplot = [[x,y] for [x,y,z,w] in dataframe[0]]
    plt.scatter(*zip(*dataplot),s=2)
    dataplot = [[x,y] for [x,y,z,w] in dataframe[1]]
    plt.scatter(*zip(*dataplot),s=2,marker='o', color='r')
    
    # timestep vs pedo
    b = plt.figure(2)
    dataplot = [[x,z] for [x,y,z,w] in dataframe[0]]
    plt.scatter(*zip(*dataplot),s=2)
    dataplot = [[x,z] for [x,y,z,w] in dataframe[1]]
    plt.scatter(*zip(*dataplot),s=2,marker='o', color='r')
    
    # timestep vs temp
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
    
"""






