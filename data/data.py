#!/usr/bin/env python
# data.py - for python 2.7+
# Version 1.0
# MET project by Chih-Yu (Andy) Liu, Tracy Lu, and Felix Wong

# Usage: 'python data.py data.txt' at the command line
# Output: random testing numbers
#-----------------------------------------------------------------------------#

# packages
from __future__ import print_function
from __future__ import division
import sys
import random
import math

numberofdatafiles = 10
for i in range(1,numberofdatafiles+1):
    log = open(str(i)+'.txt', 'w')
    
    # parameters
    init_time = 0
    end_time = random.randint(720,8640)

    heartrate = 130
    var_heartrate = 3
    hr_high = 200
    hr_low = 50

    pedo = 0
    var_pedo = 3


    # printing
    for k in range(init_time,end_time):
        heartrate = heartrate+random.randint(-var_heartrate,var_heartrate)
        if heartrate < hr_low:
            heartrate=hr_low
        if heartrate > hr_high:
            heartrate=hr_high
        
        avgrate = -k/10000+math.exp(heartrate/60)/10+math.exp(heartrate/30)/20+random.uniform(0,1)
        rate = math.sqrt(math.exp(heartrate/30)/20)+random.uniform(0,1)
        # rate = random.uniform(0,var_pedo)
        #           pedo = pedo+rate
        
        print (str(k+1)+'\t'+str(heartrate)+'\t'+str("{0:.2f}".format(rate))+'\t'+str("{0:.3f}".format(avgrate)),file=log)




