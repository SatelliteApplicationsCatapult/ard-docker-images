#!/bin/bash

# From: https://stackoverflow.com/a/49997119

git submodule update 
git submodule foreach git checkout master 
git submodule foreach git pull origin master 