#!/bin/bash

for i in kEps_config1 kEps_config2 kEps_config3 kEps_config4; do
	(
	cd $i;
	sh run.sh;
	cd ..;
	)
done	
