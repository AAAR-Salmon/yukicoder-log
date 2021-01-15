#! /usr/bin/bash
mkdir $1
cp template/main.py $1/
cd $1/
oj d "https://yukicoder.me/problems/no/$1"
