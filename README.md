Some python utilities for getting more normalized frequency data out of Google Ngrams.

## Workflow

1. ./download_ngrams.sh - Download the 1-gram files
2. ./freq_pos.py - Calculate the frequencies
3. Concatenate the output files by your preferred method, e.g.:

```sh
echo "word,pos,freq" > all.csv
for i in {a..z}; do
  cat $i\_1999.csv >> all.csv
done
```

4. ./clean_aggregated.py - Filter out the ones without normal part-of-speech markers
5. ./truncate.py - Get the log frequency and truncate to the N most frequent
