#! Python 2.7
# Usage: Scraper will pull Profile Header Card
# and the recent tweets from @realDonaldTrump
# Twitter page and save them in a text file
# labeled as donald_trump_tweets.txt

import urllib
from bs4 import BeautifulSoup
import requests
import io

url = 'https://twitter.com/realDonaldTrump'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')



thedonald = io.open('donald_trump_tweets.txt', 'w', encoding='utf8')
thedonald.write(soup.find('div', {'class':'ProfileHeaderCard'}).find('p').text + '\n\n')
thedonald.close()

i = str(1).encode('utf-8').decode('utf-8')
thedonald = io.open('donald_trump_tweets.txt','a', encoding='utf-8')

for tweets in soup.findAll('div', {'class':'content'}):
    thedonald.write(tweets.find('p').text + '\n\n')
    
thedonald.close()
