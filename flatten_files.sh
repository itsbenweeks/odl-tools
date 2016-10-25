#!/bin/bash
# Ben Weeks
# Script to flatten and sanitize filenames. This way they'll play nicely with the MITr system.
# Just run this script in the static directory.
# Hasn't been tested with static folders that are more than 1 directory deep.
for FOLDER in $(ls -d */)
do
    for FILE in $FOLDER*
    do
        mv $FILE ${FOLDER%%/}_$(basename $FILE)
    done
    rmdir ${FOLDER%%/}
done
rename -z *
exit
