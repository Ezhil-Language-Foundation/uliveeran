# (C) 2018 Ezhil Language Foundation
# This file can be used or distributed under MIT License
import os
import sys
import glob

from ngram.Corpus import Corpus
from ngram.LetterModels import Unigram

def run(parent,outputfile):
    x=None
    for filename in glob.glob(os.path.join(parent,"*.word")):
        if not x:
            x = Unigram(filename)
        else:
            x.corpus = Corpus(filename) #update file
        x.frequency_model()
    x.save(outputfile)
    return

if __name__ == "__main__":
    run("plain_text",outputfile="unigram.txt")
