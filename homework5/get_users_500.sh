#!/usr/bin/bash
grep '[1-9\.]* - - \[.*\] ".*" 5' access.log | awk '{print $1}' | sort | uniq -c | sort -n -r | head -5 | awk '{print "IP:" $2, "server errors:" $1}'
