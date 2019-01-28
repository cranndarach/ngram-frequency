#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filter out words without a normal POS tag.
"""

import csv

# The unnecessary ones are commented out.
pos_tags = [
    "NOUN",
    "VERB",
    "ADJ",
    "ADV",
    "PRON",
    "DET",
    "ADP",  # Prepositions and postpositions
    # "NUM",  # Numerals
    "PRT",  # Particles
    # ".",    # Punctuation
    # "X",    # Catch-all
    "CONJ"
]


def check_row(row):
    if row["pos"] not in pos_tags:
        return False
    else:
        return True


def main(input_path, output_path):
    headers = ["word", "pos", "freq"]
    filtered = []
    with open(input_path, "r", newline="") as f:
        reader = csv.DictReader(f, fieldnames=headers)
        for row in reader:
            if check_row(row):
                filtered.append(row)
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in filtered:
            writer.writerow(row)
