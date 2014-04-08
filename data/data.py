#!/usr/bin/env python
# data.py - for python 2.7+
# Version 1.0
# MET project by Chih-Yu (Andy) Liu, Tracy Lu, and Felix Wong

# Usage: 'python data.py data.txt' at the command line
# Output: random testing numbers
#-----------------------------------------------------------------------------#

# packages
from __future__ import print_function
import sys
import random

numberofdatafiles = 10
for i in range(1,numberofdatafiles+1):
    log = open(str(i)+'.txt', 'w')
    
    # parameters
    init_time = 0
    end_time = 10

    heartrate = 130
    var_heartrate = 5
    hr_high = 200
    hr_low = 50

    pedo = 0
    var_pedo = 7

    temperature = 95
    var_temperature = .1
    t_high = 110
    t_low = 80

    # printing
    for k in range(init_time,end_time):
        heartrate = heartrate+random.randint(-var_heartrate,var_heartrate)
        pedo = pedo+random.randint(0,var_pedo)
        temperature = temperature+random.uniform(-var_temperature,var_temperature)
        if heartrate < hr_low:
            heartrate=hr_low
        if heartrate > hr_high:
            heartrate=hr_high
        if temperature < t_low:
            temperature=t_low
        if temperature > t_high:
            temperature = t_high
        print (str(k+1)+'\t'+str(heartrate)+'\t'+str(pedo)+'\t'+str(temperature),file=log)