#!/bin/bash

for i in {1..4}; do
    (
    cd kOme_config$i || continue
    awk -F',' -v OFS=, 'NR>1 {print $2,$5,$6,$8}'
    for j in 019 023 029 055; do 
        kOme_config$i_$j.csv >> ../forOctave_kOme1095$i.ods
    done
    )
done

paste *.ods >> forOctave_kOme1095.ods

