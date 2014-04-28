#!/usr/bin/env python
# processing.py - for python 2.7+
# Version 1.0
# MET project by Chih-Yu (Andy) Liu, Tracy Lu, and Felix Wong

# Usage: 'python processing.py [sparkid]' at the command line
# Sample Usage: 'python processing.py 51ff66065067545736270187'
# Output: optimal heart-rate running pace timeseries as array
#-----------------------------------------------------------------------------#

# packages
# from __future__ import print_function
from __future__ import division
import sys
import os, os.path
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import fsolve

directory = './data/'+sys.argv[1]+'/'
alldatafiles = [item for item in os.listdir(directory) if '.txt' in item]

# run FANCY PLOTS MODULE?
fancyplots = 1
# run REGRESSION PLOTING MODULE?
regressionplots = 1


#--------------------------DATA IMPORT MODULE--------------------------------#

# time, heart rate, inst. running rate, avg. running rate arrays
ti = []
hr = []
rr = []
ar = []
mean_ar = []

# input graphs from files specified in command line and eliminate spaces
for inputfile in alldatafiles:
    fopen = open(directory+inputfile);
    yy = []
    for line in fopen.readlines():
        currentline = line.split('\t')
        ti.append(eval(currentline[0]))
        hr.append(eval(currentline[1]))
        rr.append(eval(currentline[2]))
        ar.append(eval(currentline[3]))
        yy.append(eval(currentline[3]))
    mean_ar.append(np.mean(yy))
    fopen.close()

ti_np = np.array(ti)
hr_np = np.array(hr)
rr_np = np.array(rr)
ar_np = np.array(ar)
# the variables ti, hr, rr, ar store the time series of each variable




#--------------------------FANCY PLOTS MODULE--------------------------------#

if fancyplots == 1:
    # histogram of average running rates
    p0 = plt.figure(0)
    plt.hist(mean_ar, bins=10, color='blue')
    plt.title('Distribution of Average Running Rate Workouts')
    plt.xlabel('Average Running Rate During Routine')
    plt.ylabel('Frequency')

    # pairwise time series of running factors
    # ti vs hr
    p1 = plt.figure(1)
    dataplot = zip(ti_np,hr_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.title('Aggregated Data: Time vs. Heart Rate')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')

    # ti vs ar
    p2 = plt.figure(2)
    dataplot = zip(ti_np,ar_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.title('Aggregated Data: Time vs. Average Running Rate')
    plt.xlabel('Time')
    plt.ylabel('Average Running Rate')

    # hr vs ar
    p3 = plt.figure(3)
    dataplot = zip(hr_np,ar_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.title('Aggregated Data: Heart Rate vs. Average Running Rate')
    plt.xlabel('Heart Rate')
    plt.ylabel('Average Running Rate')

    # rr vs ar
    p4 = plt.figure(4)
    dataplot = zip(rr_np,ar_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.title('Aggregated Data: Instantaneous Running Rate vs. Average Running Rate')
    plt.xlabel('Instantaneous Running Rate')
    plt.ylabel('Average Running Rate')

    # hr vs rr
    p5 = plt.figure(5)
    dataplot = zip(hr_np,rr_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.title('Aggregated Data: Heart Rate vs. Instantaneous Running Rate')
    plt.xlabel('Heart Rate')
    plt.ylabel('Instantaneous Running Rate')

    # show plots
    p0.show()
    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()
    raw_input()




#----------------------------REGRESSION MODULE--------------------------#


# Use scipy.curve_fit for fitting to predefined functions

# hr vs rr: returns rr=function(hr)
# exponential fit done by taking log first
def func1(x, a, b):
    return a*x+b
params = curve_fit(func1, hr_np, np.log(rr_np))
[a1,b1]=params[0]
print params[0]

# rr vs ar: returns ar=function(rr)
def func2(x, a, b):
    return a*x**2+b
params = curve_fit(func2, rr_np, ar_np)
[a2,b2]=params[0]
print params[0]

# hr vs ar: returns ar=function(hr)
# exponential fit done by taking log first
def func3(x, a, b):
    return a*x+b
params = curve_fit(func3, hr_np, np.log(ar_np))
[a3,b3]=params[0]
print params[0]

# ti vs ar: returns ar=function(ti)
def func4(x, a, b):
    return a*x+b
params = curve_fit(func4, ti_np, ar_np)
[a4,b4]=params[0]
print params[0]





#-----------------------REGRESSION PLOTTING MODULE--------------------------#

if regressionplots == 1:
    # plot all of the regressions above
    # hr vs rr
    x = np.linspace(min(hr),max(hr),100)
    y = func1(x, a1, b1)
    p7 = plt.figure(7)
    dataplot = zip(hr_np,rr_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.plot(x,np.exp(y))
    plt.title('Fitted Data: Heart Rate vs. Instantaneous Running Rate')
    plt.xlabel('Heart Rate')
    plt.ylabel('Instantaneous Running Rate')

    # rr vs ar
    x = np.linspace(min(rr),max(rr),100)
    y = func2(x, a2, b2)
    p8 = plt.figure(8)
    dataplot = zip(rr_np,ar_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.plot(x,y)
    plt.title('Fitted Data: Instantaneous Running Rate vs. Average Running Rate')
    plt.xlabel('Instantaneous Running Rate')
    plt.ylabel('Average Running Rate')

    # hr vs ar
    x = np.linspace(min(hr),max(hr),100)
    y = func3(x, a3, b3)
    p9 = plt.figure(9)
    dataplot = zip(hr_np,ar_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.plot(x,np.exp(y))
    plt.title('Fitted Data: Heart Rate vs. Average Running Rate')
    plt.xlabel('Heart Rate')
    plt.ylabel('Average Running Rate')

    # ti vs ar
    x = np.linspace(min(ti),max(ti),100)
    y = func4(x, a4, b4)
    p10 = plt.figure(10)
    dataplot = zip(ti_np,ar_np)
    plt.scatter(*zip(*dataplot),s=2)
    plt.plot(x,y)
    plt.title('Fitted Data: Time vs. Average Running Rate')
    plt.xlabel('Time')
    plt.ylabel('Average Running Rate')

    # show plots
    plt.close(0)
    plt.close(1)
    plt.close(2)
    plt.close(3)
    plt.close(4)
    plt.close(5)
    plt.close(6)
    p7.show()
    p8.show()
    p9.show()
    p10.show()
    raw_input()




#--------------------LEAST SQUARES OPTIMIZATION MODULE-----------------------#

# set up energy function
def LS_energy(t,h,w1,w2,w3,a1,a2,a3,a4,b1,b2,b3,b4):
    return w3*func2(np.exp(func1(h,a1,b1)),a2,b2)+w2*np.exp(func3(h,a3,b3))+w1*func4(t,a4,b4)

def constraint1(h,havg):
    return abs(h-havg)
           
def constraint2(h,ravg):
    return abs(np.exp(func1(h,a1,b1)-ravg))

def total_energy(t,h,objA,c1,c2,c3,havg,ravg,w1,w2,w3,a1,a2,a3,a4,b1,b2,b3,b4):
    return c1*abs(objA-LS_energy(t,h,w1,w2,w3,a1,a2,a3,a4,b1,b2,b3,b4))**2+c2*constraint1(h,havg)+c3*constraint2(h,ravg)

# real parameters
objA = 10
havg = np.mean(hr_np)
ravg = np.mean(rr_np)

# weights
w1 = 1/3
w2 = 1/3
w3 = 1/3
c1 = 1
c2 = 1
c3 = 1

#print LS_energy(100,100,w1,w2,w3,a1,a2,a3,a4,b1,b2,b3,b4)
#print LS_energy(100,200,w1,w2,w3,a1,a2,a3,a4,b1,b2,b3,b4)
print total_energy(10,100,objA,c1,c2,c3,havg,ravg,w1,w2,w3,a1,a2,a3,a4,b1,b2,b3,b4)

# print out solutions to linear equation (heart rate)
for time in range(1,1000):
    f = lambda h:total_energy(time,h,objA,c1,c2,c3,havg,ravg,w1,w2,w3,a1,a2,a3,a4,b1,b2,b3,b4)
    opth = fsolve(f, 50.0)[0]
    # (optimal heart rate, optimal running rate) pair
    print opth,np.exp(func1(opth,a1,b1))



