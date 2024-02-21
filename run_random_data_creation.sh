#!/bin/bash

for i in {1..100}; do
    # Generate a random number between 0 and 4000
    index=$(($RANDOM % 56687))

    # Execute your script with the random index
    python scripts/datacube.py \
        --sample "scripts/mgrs_full.fgb" \
        --bucket "cc-dataocean/clay-model-training-data" \
        --index $index
done
