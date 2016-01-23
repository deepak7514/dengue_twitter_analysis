import sys, csv, re

top_tags = ['dengue', 'ondox', 'brazil', 'ebola', 'health', 'mosquito', 'pakistan', 'saopaulo', 'news', 'karachi', 'chikungunya', 'pmln', 'malaysia', 'ptihas', 'changepenang', 'justice4saiful', 'india', 'malaria', 'peru', 'pharma']

tablefilename = '/home/deepak/nltk_data/dengue_fuzzy/data/tweets.csv'
outfilename = '/home/deepak/nltk_data/dengue_fuzzy/data/hash.tag.counts.csv'

tablereader = csv.reader(open(tablefilename), delimiter=',', quotechar='"')

# read the headers in the table
"""
headers = tablereader.next()
d = dict()
for index, item in enumerate(headers):
	d[item] = index
"""
d={'interval': 0, 'tweet_id': 1, 'text': 2, 'user.screen_name': 3}
# open the output file and write headers
csvfile=open(outfilename, 'w')
writer = csv.writer(csvfile, delimiter=',')
writer.writerow(['hash.tag','count'])

counts={}
for i in top_tags:
    counts[i]=0

# read through the table and for each interval calculate counts for each of the top tags
hash_regex = re.compile(r'#[0-9a-zA-Z+_]*',re.IGNORECASE)
for row in tablereader:
    # loop through the hashtags and count up the top tags 		
    for ht in hash_regex.findall(row[d['text']]):
        tag = ht.lstrip('#').lower()
        if tag in top_tags:
            counts[tag]+=1

for i in top_tags:
    writer.writerow([i,counts[i]])
    
csvfile.close()
