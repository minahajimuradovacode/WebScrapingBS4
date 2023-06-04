# Ensure that you have both beautifulsoup and requests installed
import requests  #pip install requests
from bs4 import BeautifulSoup  #pip install beautifulsoup4

# Using the requests module, we use the "get" function 
# provided to access the webpage provided as an argument to this function
result = requests.get("https://www.soliton.az/az/telefon/mobil-telefonlar/")

# To make sure that the website is accessible, we can ensure that 
# we obtain a 200 OK response to indicate that the page is indeed present
# print(result.status_code)

# Now, let us store the page content of the website accessed from requests to a variable
result = result.content

# Now that we have the page source stored, we will use 
# the BeautifulSoup module to parse and process the source. 
# To do so, we create a BeautifulSoup object based on the source variable we created above.
soup = BeautifulSoup(result, "lxml")

# Now that the page source has been processed via Beautifulsoup 
# we can access specific information directly from it.
names = [] #We have created an empty list so that we can collect the phone names.
for tag in soup.find_all("a", class_="title"): #This will give us all the a tags with title class in the html code in a list.
    names.append(tag.string) #Here, we take the string inside the tags and add it to the list.

credit_prices = [] # We have created an empty list so that we can collect the credit prices.
real_prices = [] # We have created an empty list so that we can collect the real prices.
tags = soup.find_all("div", class_="price") # This will give us all the div tags with price class in the html code in a list.

import numpy as np # pip install numpy (for NaN)
for prices in tags:
    # Here, each "prices" will be a list with one or two prices (credit price and real price)
    if len(prices.find_all("strong")) == 1:
        real_prices.append(prices.find_all("strong")[0].string) # Here, we take the string inside the tags and add it to the list.
        credit_prices.append(np.nan) # Here, we append NaN value to create clean data

    else:
        credit_prices.append(prices.find_all("strong")[0].string)
        real_prices.append(prices.find_all("strong")[1].string)


import pandas as pd # pip install pandas (for create data frame)
# Create the DataFrame with Series because we have null values.
data = pd.DataFrame({"Names": pd.Series(names),
                   "Real prices": pd.Series(real_prices),
                   "Credit prices": pd.Series(credit_prices)})

print(data) 

# Save DataFrame to a CSV file
data.to_csv('data.csv', index=False)
