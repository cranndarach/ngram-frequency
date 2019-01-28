#!/bin/bash

for i in {a..z}
do
  echo "Downloading $i..."
  curl -L http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-$i.gz -o googlebooks-eng-all-1gram-20120701-$i.gz
  echo "Downloaded $i."
  gzip -d googlebooks-eng-all-1gram-20120701-$i.gz
  echo "Decompressed $i."
done
