#!/bin/bash

INVOKE_URL="https://uq5k4byzp8.execute-api.ap-southeast-1.amazonaws.com"

for i in $(seq 2001 2050); do
    json=$(jq -n --arg year "$i" --arg title "MovieTitle$i" '{year: $year, title: $title}')
    curl --header "Content-Type: application/json" --data "$json" "$INVOKE_URL/movies"
done

