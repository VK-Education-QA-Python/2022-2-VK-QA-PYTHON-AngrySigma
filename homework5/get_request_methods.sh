#!/usr/bin/bash
for query in GET HEAD POST PUT DELETE CONNECT OPTIONS TRACE PATCH
do
echo $query requests:
grep "\<$query" access.log | wc -l
done
