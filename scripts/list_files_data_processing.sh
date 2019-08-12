#!/usr/bin/env bash

# Purpose
# Script to check if encryt function is applied to the yaml files

path="/Users/parth/Documents/bitbuckets/acm-dp-data-processing/profiles/acm-mm-staging/"
op=""
cnt=1

for file in $(ls $path)
do
    op=$(cat $path/$file | grep "EncryptField" | grep -v "#")
    if [[ ! -z "$op" ]]; then
#        echo "The value is :"$op":"
        cnt=$((cnt + 1)) #`expr $cnt + 1`
        echo "$cnt " "$file"
    fi
done
