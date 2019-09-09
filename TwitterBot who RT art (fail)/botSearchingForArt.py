#By Eliott Gandiolle
import tweepy
import time

consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'

key = 'your_key'
secret = 'your secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag1 = "drawing"
hashtag2 = "art"
hashtag3 = "fanart"
hashtag4 = "digitaldrawing"
tweetNumber = 20

def searchbot(hash,ap):
    tweets = tweepy.Cursor(ap.search,hash).pages(20)
    for tweet in tweets:
        try:
            if tweet.favorite_count > tweet.user.screen_name.followers_count * 0.5 and tweet.retweet_count < tweet.favorite_count:
                tweet.retweet()
            print("retweet Done")
			return
        except tweepy.TweepError as e:
            print(e.reason)


while(true):
	searchbot(hashtag1,api)
	searchbot(hashtag2,api)
	searchbot(hashtag3,api)
	searchbot(hashtag4,api)
	time.sleep(80)
