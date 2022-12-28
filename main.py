import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

KEYWORDS = ['что', 'дизайн', 'фото', 'web', 'python']
ua = UserAgent()
url = 'https://habr.com/ru/all/'
HEADERS = {
  "User-Agent": ua.chrome
}

response = requests.get(url, headers=HEADERS)
text = response.text
soup = BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    preview = article.find_all("p")
    preview = [hub.text.lower() for hub in preview]
    preview_edit = re.findall(r'\w+', str(preview))
    for wd in KEYWORDS:
        if wd.lower() in preview_edit:
            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            full_href = f"https://habr.com{href}"
            title = article.find("h2").find("span").text
            datapost = article.find("time").attrs["title"]
            print(f"{datapost} ==> {title} ==> {full_href}")
            break
