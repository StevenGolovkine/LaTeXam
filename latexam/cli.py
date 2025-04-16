#!/usr/bin/env python
# -*- coding:utf-8 *-


import argparse


def run_cli() -> argparse.Namespace:
    """Command-Line Interface"""
    parser = argparse.ArgumentParser(
        prog="LaTeXam", description="Generate LaTeX exams from JSON."
    )

    parser.add_argument("input_file", help="Path to the input JSON file.")
    parser.add_argument("-o", "--output", default="output/", help="Output folder")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = run_cli()
    print(f"Input: {args.input_file}")
    print(f"Output: {args.output}")
