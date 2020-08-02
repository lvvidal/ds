#!/bin/bash
local_file=$1

echo "local_file=$local_file"

file_name=$(basename $local_file | cut -d'.' -f1)
echo "file_name=$file_name"

dir_local=$(dirname $local_file)
echo "dir_local=$dirname"

if [ ! -d  "$(dirname $local_file)" ]; then
    mkdir -p "$(dirname $local_file)"
fi

exit 0