#!/usr/bin/env bash
set -eux

reference=$1
reads=$2

bwa index $reference
bwa mem $reference $reads | samtools view -S -b > ${reads}.bam