import tweepy
from tweepy import OAuthHandler
import codecs
from string import punctuation


class twitter_sentiment():
    # Credentials for Twitter API:consumer key, consumer secret, access token, access secret.
    ckey = 'aPYVp5sxc5fMsW9u4hESZvz1w'
    csecret = 'SS7sGETRbMy2Vc5n7fPHHkjTun28Jo43wu4HjdORsABVWc8yr9'
    atoken = '775363073561419776-UiS5wZHH4y7AJ1RNIAGwVBPQXxcQmtj'
    asecret = 'MVQFYTQ3lwIzPfiwJiSDjlYOEUOFExMxfib3799M5jMfW'
    # OAuth Authentication
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    # Twitter API wrapper
    api = tweepy.API(auth)
    pos_sent = open("positive_words.txt").read()  # Load contents from positive.txt file into pos_sent list
    positive_words = pos_sent.split('\n')
    neg_sent = open('negative_words.txt').read()  # Load contents from negative.txt file into neg_sent list
    negative_words = neg_sent.split('\n')

    # tweetSearch(self, celebrityName) searches for 50 tweets containing the "Celebrity name" and saves them to "CelebTweets.txt" for sentiment analysis at tweetSentimentAnalysis
    def tweetSearch(self, celebrityName):
        outFile = codecs.open("CelebTweets.txt", 'a', "utf-8")
        outFile1 = codecs.open("TweetDetails.txt", 'a', "utf-8")
        results = self.api.search(q=celebrityName, lang="en", locale="en", count=50)
        outFile.write('\n*******************************************************************************\n')
        outFile.write('\nTweets for celebrity %s \n' %celebrityName)
        outFile.write('\n*******************************************************************************\n')

        outFile1.write('\n*******************************************************************************\n')
        outFile1.write('\nTweets for celebrity %s \n' %celebrityName)
        outFile1.write('\n*******************************************************************************\n')

        for result in results:
            outFile.write(result.text + '\n')
            print(result)
            # Do Need not to Load following contents in 'TweetDetails.txt',I am just loading them to get more information about tweets and users.
            outFile1.write('\n---------------------------------NEW TWEET ARRIVED!---------------------------------\n')
            outFile1.write("Tweet Text:" + result.text + '\n')  # Print Tweet Text
            outFile1.write("Author's screen name:" + str(result.user.screen_name) + '\n')  # Print Screenname of user
            outFile1.write("Time Of Creation:" + str(result.created_at) + '\n')  # Print Time at which tweet created
            outFile1.write("Source of Tweet:" + result.source + '\n')  # Print Source of tweet
        outFile1.close()
        outFile.close()

    def posNegCount(self, tweet):  # Count number of positive and negative words are present in tweet
        pos = 0
        neg = 0
        for p in list(punctuation):
            tweet = tweet.replace(p, '')
            tweet = tweet.lower()
            words = tweet.split(' ')
            word_count = len(words)
            for word in words:
                if word in self.positive_words:
                    pos = pos + 1  # increase pos count if words in positive_words.txt matched with words tweet words
                elif word in self.negative_words:
                    neg = neg + 1  # increase neg count if words in negative_words.txt matched with words tweet words
        return pos, neg

    def tweetSentimentAnalysis(self):
        # Read all the tweets from 'CelebTweets.txt' and
        # split + store them to tweets_list
        tweets = codecs.open("CelebTweets.txt", 'r', "utf-8").read()
        tweets_list = tweets.split('\n')
        # Call posNegCount() on each tweet stored in tweets_list and
        # increment positive_counter and negative_counter accordingly
        positive_counter = 0
        negative_counter = 0
        for tweet in tweets_list:
            if (len(tweet)):
                p, n = self.posNegCount(tweet)
                positive_counter += p
                negative_counter += n
            #print("positive_counter:", positive_counter, "negative_counter:", negative_counter)
        if positive_counter > negative_counter:  # POSITIVE
            return "POSITIVE"
        elif positive_counter < negative_counter:  # NEGATIVE
            return "NEGATIVE"
        else:
            return "NEUTRAL"  # NEUTRAL



