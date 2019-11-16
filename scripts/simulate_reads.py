import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Simulate perfect reads.')
    parser.add_argument('fasta', type=str, help='Single-record fasta file.')
    parser.add_argument('-l', type=int, help='Length of each simulated reads.', default=100)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    read_length = args.l

    with open(args.fasta) as fasta_file:
        fasta_lines = fasta_file.readlines()
    header, seq = fasta_lines[0:2]
    header = header.strip()
    seq = seq.strip()

    for i in range(len(seq)-read_length):
        print(f"{header}_simulated_read_{i}\n{seq[i:i+read_length]}")

if __name__=="__main__":
    main()