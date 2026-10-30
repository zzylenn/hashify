import argparse
import sys

from .algorithms import ALGORITHMS
from .core import compare_files, hash_file, verify_file


def add_algorithm_argument(parser):
    parser.add_argument(
        "-a",
        "--algorithm",
        default="SHA256",
        type=str.upper,
        choices=ALGORITHMS,
        help="Hashing algorithm (default: SHA256)",
    )


def create_parser():
    parser = argparse.ArgumentParser(
        prog="hashify",
        description="Generate, compare and verify file hashes.",
    )
    commands = parser.add_subparsers(dest="command")

    hash_parser = commands.add_parser("hash", help="Generate a file hash")
    hash_parser.add_argument("file", help="File to hash")
    add_algorithm_argument(hash_parser)

    verify_parser = commands.add_parser("verify", help="Verify a file against a hash")
    verify_parser.add_argument("file", help="File to verify")
    verify_parser.add_argument("hash", help="Expected hash")
    add_algorithm_argument(verify_parser)

    compare_parser = commands.add_parser("compare", help="Compare two files")
    compare_parser.add_argument("file1", help="First file")
    compare_parser.add_argument("file2", help="Second file")
    add_algorithm_argument(compare_parser)

    commands.add_parser("help", help="Display available commands")
    return parser


def run(args, parser):
    if args.command == "hash":
        digest = hash_file(args.file, args.algorithm)
        print(f"{args.algorithm}  {args.file}")
        print(digest)
        return 0

    if args.command == "verify":
        matches, actual_hash = verify_file(args.file, args.hash, args.algorithm)
        print(f"{args.algorithm}  {args.file}")
        print(f"Expected: {args.hash.strip()}")
        print(f"Actual:   {actual_hash}")
        print("Match" if matches else "Mismatch")
        return 0 if matches else 1

    if args.command == "compare":
        matches, first_hash, second_hash = compare_files(
            args.file1, args.file2, args.algorithm
        )
        print(f"{args.algorithm} comparison")
        print(f"{args.file1}: {first_hash}")
        print(f"{args.file2}: {second_hash}")
        print("Files are identical" if matches else "Files are different")
        return 0 if matches else 1

    if args.command == "help":
        parser.print_help()
        return 0

    parser.print_help()
    return 0


def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        return run(args, parser)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
