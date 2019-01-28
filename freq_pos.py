#!/usr/bin/env python3

"""
Separate out the part of speech and sum the frequencies across years.
"""

import pandas as pd


def load_corpus(path):
    headers = ["ngram", "year", "count", "volume_count"]
    return pd.read_csv(path, sep="\t", low_memory=False, header=None,
                       names=headers)


def truncate_years(df, cutoff):
    return df.where(df.year >= cutoff)


def sum_frequencies(df):
    grouped = df.groupby(["ngram"]).sum()
    return grouped.reset_index()


def split_pos(df):
    df.pos = df.ngram.apply(lambda word: word.split("_")[-1])
    df.ngram = df.ngram.apply(lambda word: word.split("_")[0])
    return df


def select_relevant(df):
    return df.loc[:, ["ngram", "pos", "count"]]


def main():
    # file_path = "./googlebooks-eng-all-1gram-20120701-a"
    file_path = "./parts/a_1.txt"
    df = load_corpus(file_path)
    print("Corpus loaded.")
    df = truncate_years(df, 1999)
    print("Truncated years.")
    df = sum_frequencies(df)
    print("Summed frequencies.")
    df = split_pos(df)
    print("Split POS.")
    df = select_relevant(df)
    print("Selected relevant columns.")
    df.to_csv("aggregated/a_1.csv", index=False)
    print("Saved to file.")
    return df
