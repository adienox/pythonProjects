import requests
from bs4 import BeautifulSoup
import subprocess as sp

year = str(sp.getoutput('date +%Y'))
month = str(sp.getoutput('date +%m'))
day = str(sp.getoutput('date +%d'))
url = "https://ramropatro.com/getAdDate.php?query="+year+"-"+month+"-"+day+"&convert_from=English"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
print(soup.text)
