#!/usr/bin/env python
# data.py - for python 2.7+
# Version 1.0
# MET project by Chih-Yu (Andy) Liu, Tracy Lu, and Felix Wong

#  Main python script for:
#       1) getting new workout data
#       2) retraining
#       3) pushing out new optimal routine to spark core

# Usage: 'python met.py [spark id] [access code]' at the command line
#-----------------------------------------------------------------------------#


## get new workout data
import sys
import subprocess
p = subprocess.Popen(['curl', "'https://api.spark.io/v1/devices/"+sys.argv[1]+"/temp?access_token="+sys.argv[2]+"'", ">", sys.argv[1]+"/"+str(i)+".txt"], stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
out, err = p.communicate()

print out
print sys.argv[0], sys.argv[1]


#   > sparkid/1.txt


# eliminate redundant data

#_________










#51ff66065067545736270187


## retraining using ALL data


1. read in everyhting from sparkid/*
2. data = [everything]
(time, heart rate, runing, avg)

regression/
function optimization


optimalrun =
[ (30, heart rate, runing, avg)
 (60, heart rate, runing, avg)
 (90, heart rate, runing, avg)
 (time, heart rate, runing, avg)
 (time, heart rate, runing, avg)]


write optimalrun sparkid/optimal.txt

# plot all data,
# visual optimal agaisnt distribution of other runs
















#---==-
# sparkid/optimal.txt

## push out new routine to spark cloud
# put optimal.txt onto spark cloud







