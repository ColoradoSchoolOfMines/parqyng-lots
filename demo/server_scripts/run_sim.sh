#! /bin/bash

keys[0]=$(curl $1/register\?lot=2 | jq -r '.key')
keys[1]=$(curl $1/register\?lot=2 | jq -r '.key')
keys[2]=$(curl $1/register\?lot=3 | jq -r '.key')
keys[3]=$(curl $1/register\?lot=1 | jq -r '.key')

t=1

while true; do
    for i in 0 1 2 3; do
        in=$((RANDOM % (20 - t)))
        out=$((RANDOM % t))
        curl -d '{"key":'${keys[i]}',"enter":'$in',"exit":'$out'}' "$1/report"
    done

    if [ $t -lt 10 ]; then
        t=$((t + 1))
    fi

    sleep 2
done
