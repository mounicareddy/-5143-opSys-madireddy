#!/bin/sh
File_name=$1
DATE=`date +%Y-%m-%d`
echo"Date is:"$DATE
Dated_File_name="$DATE"_"$File_name"
echo "File Name is:"$Dated_File_name
echo $Dated_File_name
echo "copying the file to dated file"
cp $File_name $Dated_File_name
