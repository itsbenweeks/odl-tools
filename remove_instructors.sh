#!/bin/bash
# Ben Weeks
# One-Off Script to remove instructors from a list, and then adding them from a file.
# Depends on blanche, a command line utility written for MIT's athena cluster.
# SSH into the athena cluster in order to run this script.
echo 'mitx-residential' >> $2
echo 'odl-tech-request' >> $2
echo 'sherylb' >> $2
echo 'ichuang' >> $2
blanche -m $1 > .members_remove.swp~
blanche $1 -dl .members_remove.swp~
blanche $1 -al $2
rm .members_remove.swp~
