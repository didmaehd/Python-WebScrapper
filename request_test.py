import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text
soup = BeautifulSoup(html, "html.parser")
word = soup.select_one("#NM_set_home_btn")
print(word.text)



#NM_NEWSSTAND_data_buttons > #NM_NEWSSTAND_data_buttons > a:nth-child(1)