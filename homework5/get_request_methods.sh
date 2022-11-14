#!/usr/bin/bash
for method in GET HEAD POST PUT DELETE CONNECT OPTIONS TRACE PATCH
do
echo $method requests:
grep "\<$method" access.log | wc -l
done
