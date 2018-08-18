#!/bin/bash
for i in `ls *.html`
do
    echo "processing $i"
    k=`echo $i | cut -d'.' -f1`
    /usr/local/bin/python /usr/local/bin/tamilurlfilter.py  file:///Users/muthu/devel/MinMaduraiHTML/$i > $k.word
done
