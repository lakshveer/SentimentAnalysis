# SentimentAnalysis
Twitter Sentiment Analysis
# Project Documentation

## Problem Statement 
IMDB provides a list of celebrities born on the current date. Below is the link:
http://m.imdb.com/feature/bornondate
Get the list of these celebrities from this webpage using web scraping (the ones that are displayed i.e top 10).

You have to extract the below information:

1.	Name of the celebrity

2.	Celebrity Image

3.	Profession

4.	Best Work


Once you have this list, run a sentiment analysis on twitter for each celebrity and finally the output should be in the below format

1.	Name of the celebrity:

2.	Celebrity Image:

3.	Profession:

4.	Best Work:

5.	Overall Sentiment on Twitter: Positive, Negative or Neutral
Hint: 

Use IMDB scrapping sample example as reference for scraping the mentioned web page. 

Tools and Packages Used
 - Python version:Python 3.5.2
 - Tweepy:Tweepy is an open-sourced and enables Python to communicate with the Twitter platform and use its API
 - Twitter API:The API class provides access to the entire twitter RESTful API methods. Each method can accept various parameters and return responses.
 - Codecs:The codecs module provides stream and file interfaces for transcoding data in your program. In this project I use the module for storing the tweets as Unicode text.
 - String(punctuation):To strip the tweets of all punctuations.
 - BeautifulSoup:Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree using Python parsers like lxml and html5lib.
   It automatically converts incoming documents to Unicode and outgoing documents to UTF-8.
 - Selenium webdriver:Selenium WebDriver Client Library for Python enables us to utilize all the features available with Selenium WebDriver
   and interact with Selenium Standalone Server to perform Automated testing (both remote and distributed testing) of browser-based applications.



# Solution:
 Python Script with proper commenting
 - imdbWebscraping.py



## Challenges Faced during the project
 - profession, bestMovie = i.find("div", "detail").text.split(",")
  "ValueError: need more than 1 value to unpack"
  - Here I tried separate a list of values into keys and values.But it gave following error.So i modified as following,
   #Limit the splits to 1, in case the right-hand side contains an ','.
    
#(key, value) = line.split(",", 1)
    profession, bestMovie = i.find("div", "detail").text.split(",",1)

 - When we run twitter_sentiment.py.It should remove previous data from file 'CelebTweets.txt' and TweetDetails.txt.
   But in my case,It was appending new data to old contents,And also It was loading data for last celebrity only as it was removing previous celebrity contents.
  
#To delete data from past sentiment anlysis,
   outFile = codecs.open("CelebTweets.txt", 'w', "utf-8")
   outFile.truncate()
   outFile1 = codecs.open("TweetDetails.txt", 'w', "utf-8")
   outFile1.truncate()
   #To load data for each celebrity,
   outFile = codecs.open("CelebTweets.txt", 'a', "utf-8")
   outFile1 = codecs.open("TweetDetails.txt", 'a', "utf-8")




