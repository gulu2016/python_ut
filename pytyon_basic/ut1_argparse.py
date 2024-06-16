# description: argparse module quick start
# date: 2024-06-16

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

# q1: how to add argument
parser.add_argument("filename", type=str, help="the file to process")
# q2: how to add option "-v"
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

# q3: how to parse argument
args = parser.parse_args()


print(f"reading file {args.filename}")

if args.verbose:
    print("verbosity turned on")

