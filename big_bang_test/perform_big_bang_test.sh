#!/usr/bin/env bash

echo "Testing the case where all reads were mapped to the reference"
echo "python3 main.py big_bang_test/bams/hg38_chr1_subsampled_all_reads.fa.bam"
python3 main.py big_bang_test/bams/hg38_chr1_subsampled_all_reads.fa.bam
read -p "Press enter to next test"

echo "Testing the case where we have unmapped reads, but that BIGSI finds mapping to E. coli"
echo "python3 main.py big_bang_test/bams/hg38_chr1_subsampled_and_MCR1_ten_reads.fa.bam"
python3 main.py big_bang_test/bams/hg38_chr1_subsampled_and_MCR1_ten_reads.fa.bam
read -p "Press enter to next test"

echo "Testing the case where we have unmapped reads, but that BIGSI finds mapping to the same original genome we mapped to"
echo "python3 main.py -sp "Escherichia coli" big_bang_test/bams/hg38_chr1_subsampled_and_MCR1_ten_reads.fa.bam"
python3 main.py -sp "Escherichia coli" big_bang_test/bams/hg38_chr1_subsampled_and_MCR1_ten_reads.fa.bam
echo "Big bang tests are done"