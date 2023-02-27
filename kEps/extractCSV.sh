#!/bin/bash

for i in {1..4}; do                         
    (
    cd kEps_config$i;                                                       # Access different folders                    
    for j in 019 023 029 055; do                                            # These numbers symbolize the locations at which velocity 
                                                                            # is sampled and exported from ParaView. 
        (
        awk -F',' -v OFS=, 'NR>1 {print $2}' \                              # From the ParaView .csv exported files, ignore the 
                                                                            # first row and export only the 2nd column, 
                                                                            # column containing velocity values.
        kEps_config${i}_${j}.csv >> ../forOctave_kEps1095_${i}_${j}.ods;    # Save each column into a new file .ods format
        )
    done
    )
done

paste *.ods >> forOctave_kEps1095.ods                                       # Merge the files containing 1 column into one file,
                                                                            # containing 16 velocities (4 for 4 different meshes).

find . -maxdepth 1 -type f -name '*.ods' ! -name 'forOctave_kEps1095.ods' -exec rm {} + # Keep only the final file

