import requests
from bs4 import BeautifulSoup

url = "https://www.ashesh.com.np/nepali-date-converter.php"
def monthSelect(arg):
    print(arg)
    months = {
        1 : "Baishakh",
        2 : "Jestha",
        3 : "Ashadh",
        4 : "Shrawan",
        5 : "Bhadra",
        6 : "Ashwin",
        7 : "Kartik",
        8 : "Mangsir",
        9 : "Poush",
        10 : "Magh",
        11 : "Falgun",
        12 : "Chaitra"
    }
    return months.get(arg, "Baishakh")

year = input("Year: ")
month = input("Month: ")
day = input("Day: ")

month = str(monthSelect(int(month)))

attributes = {
    "year": year,
    "month" : month,
    "day" : day,
    "submit" : "Convert"        
}
response = requests.post(url, data=attributes)
soup = BeautifulSoup(response.content, "lxml")

print(soup.find_all("div", class_="inner")[1].text)
