import requests
from bs4 import BeautifulSoup

year = str(2078)
month = str(11)
day = str(19)
url = "https://ramropatro.com/getAdDate.php?query="+year+"-"+month+"-"+day+"&convert_from=Nepali"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
print(soup.text)
