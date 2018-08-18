# (C) 2018 Ezhil Language Foundation
# This file can be used or distributed under MIT License

import codecs
import json

# convert txt-file to JSON
def run(filename):
    jsonfile = filename.replace(".txt",".json")
    listA = []
    listB = []
    with codecs.open(filename,"r","utf-8") as fr:
        for line in fr.readlines():
            if line.find("-") == -1:
                continue
            a,b=line.split("-")
            b = float(b)  #frequency
            a = a.strip() #word
            listA.append(a)
            listB.append(b)
    
    with codecs.open(jsonfile,"w","utf-8") as fp:
        fp.write( json.dumps( [listA, listB] ) )
    d = {}
    for a,b in zip(listA,listB):
        d[a] = b
    with codecs.open('v2'+jsonfile,"w","utf-8") as fp:
        fp.write( json.dumps( d ) ) # json file as dictionary format
if __name__ == "__main__":
    run("unigram.txt")

