import argparse
from src.bam.bam import Bam
from src.index.index_factory import IndexFactory
from src.contamination_finder.contamination_finder import Contamination_Finder
import logging

def parse_args():
    parser = argparse.ArgumentParser(description='Find if there are contamination in your unmapped reads of your bam file.')
    parser.add_argument('bam', type=str, help='The bam file')
    parser.add_argument('-sp', type=str, help='The species of the bam file.', default="Homo sapiens")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO)

    # setup
    bam = Bam(args.bam)
    index = IndexFactory.create_index()
    contamination_finder = Contamination_Finder(bam, index, args.sp)

    # get the report
    report = contamination_finder.get_contamination_report()

    # print the report
    print (f"Explanation: {report.explanation.value}")
    print (f"Species: {report.species}")

if __name__=="__main__":
    main()