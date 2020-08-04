#!/bin/bash

set -e

destination_bucket=$1
folder_s3=$2
folder_local=$3
file_local=$4

destination_path="s3://${destination_bucket}/${folder_s3}/${file_local}"

echo "destination_path=$destination_path"
echo "folder_s3=$folder_s3"
echo "folder_local=$folder_local"
echo "file_local=$file_local"
echo "destination_path=$destination_path"

cd ${folder_local} || exit 1
aws s3 cp ${file_local} ${destination_path}



