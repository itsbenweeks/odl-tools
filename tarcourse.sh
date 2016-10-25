#!/bin/bash
 tar -cvz --exclude="*~" --exclude=".*" --exclude="Modules" --exclude="src" --exclude="drafts" -f "$1".$(date "+%y%m%d%H%M%S").tar.gz $1
 exit
