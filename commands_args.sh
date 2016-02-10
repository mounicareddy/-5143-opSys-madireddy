#!/bin/bash
#taking an array to store arguements
args={"$@"}
#getting number of elements
ELEMENTS=${#args[@]}
#echo each element in array
# by using for loop
for((i=0;i<$ELEMENTS;i++));
do
printf "%s\n" ${args[${i}]}
done
