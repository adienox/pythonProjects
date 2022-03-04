import requests
from bs4 import BeautifulSoup


def extractNews(url):
    print("Extracting news...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    news = soup.find_all("div", attrs={"class": "news"})
    for i, item in enumerate(news):
        print(str(i + 1) + "." + item.text + "\n" + "-" * 50)


extractNews("https://artixlinux.org")
