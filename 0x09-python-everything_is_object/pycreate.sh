#!/bin/bash
echo "file >"
read file
touch $file
echo "#!/usr/bin/python3" > $file
chmod 764 $file
gedit $file
git add $file
bash dirgit.sh
