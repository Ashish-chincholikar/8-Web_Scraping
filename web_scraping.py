# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:12:56 2023

@author: Ashish
web scraping 
-for static webpages
-
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("C:/Data_Set/sample_doc.html"),'html.parser')
print(soup)
# it is going to show all the html contents extracted
soup.text
#it will show only text

soup.contents
#it is going to show all the html contents extracted

soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table = soup.find('table')
table

for row in table.find_all('tr'):
    columns = row.find_all('td')
    print(columns)
    
#it will show all the rows except first row
#now we want to display M.Tech which is located in third row and second column
    #i need to five [3][2]
    table.find_all('tr')[3].find_all('td')[2]
    

"""
Created on Sat Oct 28 08:57:30 2023

@author: Ashish
-online website webscraping
"""

from bs4 import BeautifulSoup as bs
import requests
link = "https://sanjivanicoe.org.in/index.php/contact"
page = requests.get(link)
page

#<Response [200]> means connection is successfully established
page.content

#you will get all the html sourece code but very crowdy text
#let us apply html parser
soup = bs(page.content , 'html.parser')
soup

#Now the text is clean but not upto the expectations
#Now Let us apply prettify method
print(soup.prettify())
#The text is neat and clean
list(soup.children)
#finding all the contents using tab
soup.find_all('p')
#suppose you want to extract contents from 
#first row
soup.find_all('p')[1].get_text()
#contents from second row
soup.find_all('p')[2].get_text()
#finding text using class
soup.find_all('div' , class_ = 'table')

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:57:08 2023

@author: Ashish Chincholikar
Sentiment Analysis
"""

from bs4 import BeautifulSoup as bs
import requests
link = "https://www.flipkart.com/motorola-edge-40-neo-caneel-bay-256-gb/p/itm55813a9671489?pid=MOBGQFX6APUFAPMS&lid=LSTMOBGQFX6APUFAPMSO5N7CJ&marketplace=FLIPKART&q=mobile&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=6a034a79-d4d8-4961-bcc6-a543880ca510.MOBGQFX6APUFAPMS.SEARCH&ppt=hp&ppn=homepage&ssid=lh1c0f9tio0000001701746929438&qH=532c28d5412dd75b"
page = requests.get(link)
page
page.content
soup = bs(page.content, 'html.parser')
print(soup.prettify())
#title = soup.find_all('div' , class_ = "_1mXcCf RmoJUa")
title = soup.find_all('p' , class_ = '_2-N8zT')
title
review_title = []
for i in range(0 , len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)

#we got 10 review titles
#Now let us scrap rating

rating = soup.find_all('div' , class_ = '_3LWZlK _1BLPMq')
rating
rate = []
for i in range(0 , len(rating)):
    rate.append(rating[i].get_text())

rate
len(rate)
rate.append('')
rate.append('')
#rate.append('')
len(rate)
#------------------------------------------------------------------------------
#Now let us scrap the review body
review = soup.find_all('div' , class_ = 't-ZTKy')
review
review_body = []

for i in range(0 , len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)
#we got 10 review_body
#Now we have to save the data in .csv file

import pandas as pd
df = pd.DataFrame()
df['Review_Title'] = review_title
df['Rate'] = rate
df['Review'] = review_body

#To create .csv file
df.to_csv('C:/13-Web Scraping/flipkart_reviews.csv' , index = True)

#Sentiment Analysis
import pandas as pd
from textblob import TextBlob

sent = "This is very excellent garden"
pol = TextBlob(sent).sentiment.polarity
pol

df = pd.read_csv('C:/13-Web Scraping/flipkart_reviews.csv')
df.head()
df['polarity'] = df['Review'].apply(lambda x : TextBlob(str(x)).sentiment.polarity)
df['polarity']
