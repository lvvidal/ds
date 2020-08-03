#!/bin/bash

set -e

destination_bucket=$1
folder_s3=$2
folder_local=$3

destination_path="s3://${destination_bucket}/${folder_s3}"

echo "uploading ddl processed"
cd ${folder_local} || exit 1
aws s3 sync . "${destination_path}" --delete



