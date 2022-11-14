from bs4 import BeautifulSoup
from requests import get

base_url = "https://www.gamemeca.com/news.php"

reponse = get(base_url)
print (reponse)

# if reponse != 200:
#     print ("Sorry. We could not find website")
# else :
soup = BeautifulSoup(reponse.text, "html.parser")
news_list = soup.find("ul", class_="list_news")
head_line = news_list.find_all("li", class_="item_headline")
for news in head_line:
     print(news)