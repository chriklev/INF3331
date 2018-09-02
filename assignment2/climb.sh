#!/bin/bash
path="../"
for (( i=0; i < $1-1; i++ )); do
    path+="../"
done
cd $path || exit
