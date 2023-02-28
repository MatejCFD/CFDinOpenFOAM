#!/bin/bash

for i in {1..4}; do
    (
    cd kOme_config$i || continue
    awk -F',' -v OFS=, 'NR>1 {print $2}'
    for j in 019 023 029 055; do 
        kOme_config$i_$j.csv >> ../forOctave_kOme1095$i.ods
    done
    )
done

paste *.ods >> forOctave_kOme1095.ods
sleep 2 && find . -maxdepth 1 -type f -name '*.ods' ! -name 'forOctave_kEps1095.ods' -exec rm {} + 
