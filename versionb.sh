#!/bin/bash
File_name=$(basename "$1" .txt)
File_extension=`echo $1|cut -d'.' -f2`
DATE=`date +%Y-%m-%d`
File_Dated_name="$File_name"_"$DATE"."$File_extension"
echo "File name is:"$File_Dated_name
echo "copying the file file to dated file"
cp $1 $File_Dated_name

