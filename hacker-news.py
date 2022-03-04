import requests
from datetime import datetime
from bs4 import BeautifulSoup


def extract(url):
    cnt = ""
    link = ""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    news = soup.find_all("a", attrs={"class": "titlelink"})
    for item, title in enumerate(news):
        link = title.get("href")
        cnt += (
            str(item + 1)
            + ". "
            + "<a href='{0}'>".format(link)
            + title.text
            + "</a>"
            + "<br \>\n"
        )
    return cnt


now = datetime.now()
content = "Hacker News Main Headlines for " + now.strftime("%d/%m %I:%M")
content += extract("https://news.ycombinator.com")
print(content)
