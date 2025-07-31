import requests  # used to fetch a web page
from bs4 import BeautifulSoup  # helps us extract information from the HTML of the page

# Step 1: Define the website to scrape
url = 'https://news.ycombinator.com/'  

# Step 2: Fetch the page content
response = requests.get(url)  # this sends a GET request to the website

# Step 3: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')  

# Step 4: Extract all story titles
titles = soup.select('.storylink')  # we’re grabbing all elements with the class "storylink"

# Step 5: Print each headline
print("📰 Top Headlines from Hacker News:\n")
for i, title in enumerate(titles[:10], 1):  # limit to the top 10 headlines
    print(f"{i}. {title.text}")