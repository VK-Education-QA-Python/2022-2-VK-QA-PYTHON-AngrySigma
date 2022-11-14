#!/usr/bin/bash
awk -F'[ "]' '{print $8, $9}' access.log | sort | uniq -c | sort -n -r | head -10 | awk '{print "Adress: " $2 ", requests: " $1}' 
