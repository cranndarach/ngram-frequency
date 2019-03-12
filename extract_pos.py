#!/usr/bin/env python3

"""
Extract word forms and frequencies and separate into lists by part of
speech. Save each PoS as a separate file.
"""

import pandas as pd


def extract(corpus, pos):
    # return list(set(corpus.word.loc[corpus.pos == pos]))
    return corpus.loc[corpus.pos == pos, ["word", "freq"]]


def extract_and_save(corpus, pos_code, pos_string):
    words = extract(corpus, pos_code)
    # with open("pos_lists/" + pos_string + ".txt", "w") as f:
    #     for word in words:
    #         f.write(str(word) + "\n")
    words.to_csv("pos_lists/" + pos_string + ".csv", index=False)


def main(input_path):
    df = pd.read_csv(input_path, low_memory=False)
    extract_and_save(df, "DET", "determiners")
    extract_and_save(df, "CONJ", "conjunctions")
    extract_and_save(df, "ADP", "prepositions")
    extract_and_save(df, "ADJ", "adjectives")
    extract_and_save(df, "NOUN", "nouns")
    extract_and_save(df, "ADV", "adverbs")
    extract_and_save(df, "VERB", "verbs")
    # extract_and_save(df, "PRON", "pronouns")
    # extract_and_save(df, "PRT", "particles")


if __name__ == "__main__":
    main("./aggregated/1999_50k.csv")
