#!/bin/bash

for i in kOme_config1 kOme_config2 kOme_config3 kOme_config4; do
	(
	cd $i;
	sh run.sh;
	cd ..;
	)
done	
