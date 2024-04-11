#!/bin/bash
# git commands.
echo "commit >"
read commit
git commit -m "$commit"
git push
