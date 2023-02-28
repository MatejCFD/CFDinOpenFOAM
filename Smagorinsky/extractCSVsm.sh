#!/bin/bash

for i in {1..4}; do
    (
    cd Smagorinsky_config$i;
    for j in 019 023 029 055; do
        (
        awk -F',' -v OFS=, 'NR>1 {print $2}' Smagorinsky_config${i}_${j}.csv >> ../forOctave_Smagorinsky1095_${i}_${j}.ods;
        )
    done
    )
done

paste *.ods >> forOctave_Smagorinsky1095.ods
sleep 2 && find . -maxdepth 1 -type f -name '*.ods' ! -name 'forOctave_Smagorinsky1095.ods' -exec rm {} +
