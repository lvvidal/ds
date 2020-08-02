#!/bin/bash
local_file=$1

echo "local_file=$local_file"

file_name=$(basename $local_file | cut -d'.' -f1)
echo "file_name=$file_name"

dir_local=$(dirname $local_file)
echo "dir_local=$dir_local"

if [ ! -d  "$(dirname $local_file)" ]; then
    mkdir -p "$(dirname $local_file)"
fi

exit 0

file_name=$(basename $local_file | cut -d'.' -f1)

dir_local=$(dirname $local_file)

checksum_local_file="${dir_local}/${file_name}_checksum_local.txt"
checksum_remote_file="${dir_local}/${file_name}_checksum_remote.txt"

chmod 600 "$HOME"/.ssh/id_rsa*

ssh_opts="-o StrictHostKeyChecking=no -i $HOME/.ssh/id_rsa ${ssh_user}@${ssh_server}"

echo "home=$HOME"

function test_exit_status() {
    if [ $1 -ne 0 ]; then
        exit $1
    fi
}

if [ ! -d  "$(dirname $local_file)" ]; then
    mkdir -p "$(dirname $local_file)"
fi