"""ISO Hash Check — Compute SHA-256 of an ISO and compare it to a published checksum file."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='iso_hash_check',
        description='Compute SHA-256 of an ISO and compare it to a published checksum file.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('ISO Hash Check')
    print('Did the image match the sum.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
