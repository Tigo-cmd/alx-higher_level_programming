#!/bin/bash
# automates directory creation.
echo "dir >"
read dir
mkdir $dir
cp dirmain.sh $dir
cp bashcreate.sh $dir
cp dirgit.sh $dir
cp filecreate.sh $dir
cp pyfxn.sh $dir
cp cfxn.sh $dir
cp pycreate.sh $dir
cd $dir
echo $dir > README.md
bash dirgit.sh
