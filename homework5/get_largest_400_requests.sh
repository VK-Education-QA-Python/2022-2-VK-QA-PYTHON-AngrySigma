#!/usr/bin/bash
#sort -r -k 10 access.log | head -5
cat access.log | grep '[1-9\.]* - - \[.*\] ".*" 4' | sort -r -k 10 | head -5 | awk -F'[ "]' '{print "Adress:" $8, $9, "\nStatus code:" $11,  "\nSize:" $12 , "\nIP:" $1 "\n"}'
