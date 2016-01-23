"""
Extracting Tokens from tweets and filtering stopwords in tokenized sentences
"""

outfilename = '/home/deepak/nltk_data/dengue_fuzzy/data/tweet.text.txt'

### Open the output file ###
outputfile=open(outfilename)

### NLTK Regexp Tokenizer ###
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\s+', gaps=True)
tokens=[]

### Read through the output_file ###
for row in outputfile:
    tokens+=tokenizer.tokenize(row)
outputfile.close()

### Filtering Stopwords ###
from nltk.corpus import stopwords
import string
english_stops = set( stopwords.words('english') + list(string.punctuation) )
tokens=[str.lower(word) for word in tokens if str.lower(word) not in english_stops]

from nltk.probability import FreqDist, ConditionalFreqDist
fd = FreqDist(tokens)
#cfd = ConditionalFreqDist(tagged_words)
most_freq = (word for word, count in fd.most_common(50))
#return dict((word, cfd[word].max()) for word in most_freq)

import csv
outfilename = '/home/deepak/nltk_data/dengue_fuzzy/data/hash.tag.count.csv'
# open the output file and write headers
csvfile=open(outfilename, 'w')
writer = csv.writer(csvfile, delimiter=',')
writer.writerow(['hash.tag','count'])
for word,count in fd.most_common():
    writer.writerow([word,count])
csvfile.close()
