"""
Extract tweets and write tweet.text in  text file for futher processing
"""

import sys, csv, re

tablefilename = '/home/deepak/nltk_data/dengue_fuzzy/data/tweets.csv'
outfilename = '/home/deepak/nltk_data/dengue_fuzzy/data/tweet.text1.txt'

tablereader = csv.reader(open(tablefilename), delimiter=',', quotechar='"')

### Read the headers in the table ###
"""headers = tablereader.next()
d = dict()
for index, item in enumerate(headers):
	d[item] = index"""

### Open the output file ###
output=open(outfilename, 'w')

### Read through the table ###
for row in tablereader:
    #output.write(row[d['text']])
    output.write(row[0]+' '+row[1]+' '+row[2]+' '+row[3])
    
output.close()
