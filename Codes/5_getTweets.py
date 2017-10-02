#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys

#Twitter API credentials
consumer_key = "a8bbMbamNmgWXkVqjDRO15kXV"
consumer_secret = "MtYihkUTydjlCUleLMJPjyPFUPztq9lCXmdl6j75YpAvCVTReF"
access_key = "597559262-eSlprETCqloKtG2RNOPaTWCp0aS2BJGBGOzvcTLY"
access_secret = "7PVxcyBoxPUJM2l9EndgpilvfHwpqT5loHcKBuBMxepN4"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	#print(new_tweets.text)
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=100,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		#print(alltweets)
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write in text file
	file = open('narendramodi.txt',"w")
	file.writelines(["%s\n" % item  for item in outtweets])
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		#writer.writerow(["text"])
		writer.writerows(outtweets)
	
	pass
	
	
	



if __name__ == '__main__':
	#pass in the username of the account you want to download
	print(str(sys.argv[1]))
	get_all_tweets(str(sys.argv[1]))
