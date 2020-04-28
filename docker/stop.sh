#!/usr/bin/env bash

seleniumContainers="docker ps -qa
                              -f name=chrome
                              -f name=firefox
                              -f name=opera
"
sh="docker stop $($seleniumContainers)"
echo "$sh"
eval $sh

# docker rm -f \$(docker ps -qa) #remove all when needed
