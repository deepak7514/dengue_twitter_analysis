##
#
# Output data in the form:
# time.interval, hash.tag, count
#
##

import sys, csv, re

top_tags = ['dengue', 'ondox', 'brazil', 'ebola', 'health', 'mosquito', 'pakistan', 'saopaulo', 'news', 'karachi', 'chikungunya', 'pmln', 'malaysia', 'ptihas', 'changepenang', 'justice4saiful', 'india', 'malaria', 'peru', 'pharma']

def reset_tag_counts():
	tag_counts = dict()
	for tag in top_tags:
		tag_counts[tag] = 0;
	return tag_counts


tablefilename = '/home/deepak/nltk_data/dengue_fuzzy/data/tweets.csv'
outfilename = '/home/deepak/nltk_data/dengue_fuzzy/data/hashtags_over_time_factor_cumul.csv'


tablereader = csv.reader(open(tablefilename), delimiter=',', quotechar='"')
#tweetreader = csv.reader(open(tweetfilename), delimiter=',', quotechar='"')

# read the headers in the table
"""
headers = tablereader.next()
d = dict()
for index, item in enumerate(headers):
	d[item] = index
"""
d={'interval': 0, 'tweet_id': 1, 'text': 2, 'user.screen_name': 3}
# open the output file and write headers
writer = csv.writer(open(outfilename, 'w'), delimiter=',')
writer.writerow(['time.interval', 'hash.tag', 'count'])

# read through the table and for each interval calculate counts for each of the top tags
hash_regex = re.compile(r'#[0-9a-zA-Z+_]*',re.IGNORECASE)
current_interval = ''
counts = reset_tag_counts()
for row in tablereader:
	row_interval = row[d['interval']]
	if row_interval != current_interval:
		# write the row and reset the counters and current interval
		if current_interval != '' and current_interval != 'NA':
			for key in top_tags:
				writer.writerow([current_interval, key, counts[key]])
			#writer.writerow([current_interval] + [counts[key] for key in top_tags])
		current_interval = row_interval
		#counts = reset_tag_counts()
	# loop through the hashtags and count up the top tags 		
	for ht in hash_regex.findall(row[d['text']]):
		tag = ht.lstrip('#').lower()
		if tag in top_tags:
			counts[tag] += 1

# write the last row
#writer.writerow([current_interval] + [counts[key] for key in top_tags])
for key in top_tags:
	writer.writerow([current_interval, key, counts[key]])
