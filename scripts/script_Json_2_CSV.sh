#!/usr/bin/env bash

# Install npm package json2csv
# Run script in the folder contaning the json files

for file in $(ls | grep json)
do
    echo $file
    # filecsv=echo ${sed 's/json/csv/' $file}
    filecsv=${file/json/csv}
    echo $filecsv
    json2csv -i $file -o $filecsv
done
#EOS