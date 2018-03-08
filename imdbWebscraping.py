# Importing all required libraries
from bs4 import BeautifulSoup
import time as timer
from selenium import webdriver
import codecs
import lxml
from lxml import etree
from io import StringIO
from urllib.request import urlopen
# Custom module to do sentiment analysis on Celebrity tweets
import twitter_sentiment


# WebScrapingCelbes() is for WebScraping of 'http://m.imdb.com/feature/bornondate' url to fetch celebrity details
def WebScrapingCelbes():
    count = 0
    celebrities_name = []
    celebrityKeyValue = {}
    url = "http://m.imdb.com/feature/bornondate"  # url for WebScraping as given in problem statement
    driver = webdriver.Firefox(executable_path='C:\geckodriver-v0.16.1-win64\geckodriver.exe')
    timer.sleep(2)
    # The driver.get method will navigate to a page given by the URL.
    # WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control to your test or script.
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    boccat = soup.find("section", "posters list")
    bornDate = boccat.findChild("h1").text
    celebrityNameList = []
    for i in boccat.findAll("a", "poster "):
        celebrityKeyValue[count] = {}
        celebrityName = i.find("span", "title").text
        celebrityNameList.append(celebrityName)
        celebrityKeyValue[count]["celebrityName"] = celebrityName
        celebrityKeyValue[count]["celebrityImg"] = i.img["src"]
        # Limit the splits to 1, in case the right-hand side contains an ','.
        # (key, value) = line.split(",", 1)
        profession, bestMovie = i.find("div", "detail").text.split(",", 1)
        celebrityKeyValue[count]["profession"] = profession
        celebrityKeyValue[count]["bestMovie"] = bestMovie
        count += 1
    return celebrities_name, celebrityKeyValue


if __name__ == '__main__':
    # Intially delete previous data from 'CelebTweets.txt' and 'TweetDetails.txt'
    outFile = codecs.open("CelebTweets.txt", 'w', "utf-8")
    outFile.truncate()
    outFile1 = codecs.open("TweetDetails.txt", 'w', "utf-8")
    outFile1.truncate()
    # Scrape the website and celevrity details (as a key-value dict)
    nameOfCelebrities, celebrityKeyValue = WebScrapingCelbes()

    # Create a object for class "twitter_sentiment" . This object will be used for obtaining the twitter sentiment by the celebrity names
    celebrity = twitter_sentiment.twitter_sentiment()

    # Final output will be stored at "finalSentiment.txt"
    outputFile = codecs.open("finalSentiment.txt", 'w', "utf-8")
    for i in range(10):
        celebrityName = celebrityKeyValue[i]["celebrityName"]
        celebrity.tweetSearch(celebrityName)
        celebrityKeyValue[i]["tSentiment"] = celebrity.tweetSentimentAnalysis()
        outputFile.write("Name of the celebrity: " + celebrityKeyValue[i]["celebrityName"] + "\n")
        outputFile.write("Celebrity Image: " + celebrityKeyValue[i]["celebrityImg"] + "\n")
        outputFile.write("Profession: " + celebrityKeyValue[i]["profession"] + "\n")
        outputFile.write("Best Work: " + celebrityKeyValue[i]["bestMovie"] + "\n")
        outputFile.write("Overall Sentiment on Twitter: " + celebrityKeyValue[i]["tSentiment"] + "\n")
        outputFile.write("\n")
    outputFile.close()






