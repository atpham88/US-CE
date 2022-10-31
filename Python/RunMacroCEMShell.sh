#!/bin/bash

for interconn in "WECC" "ERCOT" "EI" ; do
    for co2cap in "10" "50"; do
	sbatch RunMacroCEMJob.sbat $interconn $co2cap
	sleep 10s
    done
done
