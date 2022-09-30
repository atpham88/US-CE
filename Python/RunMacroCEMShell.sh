#!/bin/sh

for interconn in "EI" "WECC" "ERCOT" ; do
for co2cap in "0.1" "0.5"; do
     sbatch RunMacroCEMJob.sbat $interconn $co2cap
done
