#!/bin/bash
# git commands.
echo "commit >"
read commit
git add . 
git commit -m "$commit"
git push
