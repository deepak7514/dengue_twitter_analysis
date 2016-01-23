#!usr/bin/python
import tweepy
import csv
#removes warnings(required in case of python<2.7.9)
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

#twitter authentication
auth= tweepy.auth.OAuthHandler('Consumer Key','Consumer Secret')
auth.set_access_token('Access Token','Access Secret')

api=tweepy.API(auth)
#Open/create a file to append data
csvFile=open('result.csv','a')
#Use csv writer
csvWriter=csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q='dengue',lang='en').items(10000):
    #Write a row to the csv  file/ I use encode utf-8
    csvWriter.writerow([tweet.created_at,tweet.id,tweet.text.encode('utf-8'),tweet.user.screen_name])
    print tweet.created_at,tweet.id,tweet.text.encode('utf-8'),tweet.user.screen_name
csvFile.close()
