#!/bin/bash
a=2
b=2
c=$((a + b))
echo "Bash says: Hello, World!"
echo "$a + $b = $c"
for ((i = 1; i <= 2; i++))
do
       printf "User$i, "
done
echo "User2"
