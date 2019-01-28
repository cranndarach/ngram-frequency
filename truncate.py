#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Get the log frequency and the n most frequent words.
"""

import pandas as pd
import numpy as np


def main(input_file, output_file, top_n):
    df = pd.read_csv(input_file, low_memory=False)
    df = df.assign(log_freq=df.freq.apply(np.log))
    df = df.sort_values(by=["log_freq"], ascending=True)
    df_trunc = df.tail(top_n)
    df_trunc.to_csv(output_file, index=False)
