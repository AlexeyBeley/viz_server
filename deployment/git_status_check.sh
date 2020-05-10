#!/bin/bash -x

#exit 0- no change
#exit 1- new commit found

cd /home/ubuntu/actions-runner/git_checker/viz_server/deployment
git checkout master

git pull
NEW_VERSION=$(git rev-parse --verify HEAD)

RETURN_CODE=0

if [ -f current_hash.txt ]; then
    if [[ $(< current_hash.txt) != "$NEW_VERSION" ]]; then
        python3 trigger_jenkins_job.py
        RETURN_CODE=1
    fi
fi

echo $NEW_VERSION > current_hash.txt;
exit $RETURN_CODE;