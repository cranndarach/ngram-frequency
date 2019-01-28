#!/usr/bin/env python3

"""
Separate out the part of speech and sum the frequencies across years.
"""

import csv


def write_csv(output_path, freqs):
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["word", "pos", "freq"])
        for row in freqs.values():
            writer.writeheader()
            writer.writerow(row)


def main(input_path, output_path, cutoff):
    freqs = {}
    headers = ["ngram", "year", "count", "volume_count"]
    with open(input_path, "r", newline="") as f:
        reader = csv.DictReader(f, fieldnames=headers, delimiter="\t")
        for row in reader:
            if int(row["year"]) >= cutoff:
                if row["ngram"] in freqs:
                    freqs[row["ngram"]]["freq"] += int(row["count"])
                else:
                    freqs[row["ngram"]] = {
                        "freq": int(row["count"]),
                        "word": row["ngram"].split("_")[0],
                        "pos": row["ngram"].split("_")[-1]
                    }
    print("Calculated frequencies.")
    write_csv(output_path, freqs)
    print("Saved to file.")
    return freqs
