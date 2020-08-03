#!/bin/bash
source_folder=$1
destination_folder=$2

echo "source_folder=$source_folder"
echo "destination_folder=$destination_folder"

if [ ! -d  $destination_folder ]; then
    mkdir -p $destination_folder
fi

cd $source_folder

for f in *.csv
do 
   echo "f=$f"
   cp -v "$f" $destination_folder
done

exit 0