#!/bin/bash

for i in Smagorinsky_config1 Smagorinsky_config2 Smagorinsky_config3 Smagorinsky_config4; do
	(
	cd $i;
	sh run.sh;
	cd ..;
	)
done	
