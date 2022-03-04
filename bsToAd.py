import requests
from bs4 import BeautifulSoup

# Websites which actually converts the date
url = "https://www.ashesh.com.np/nepali-date-converter.php"

# Function to change the month variable to website readable string
def monthSelect(arg):
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
    # Returns the argument specific month; If it fails, returns Baishakh
    return months.get(arg, "Baishakh")

year = input("Year: ")
month = input("Month: ")
day = input("Day: ")

month = str(monthSelect(int(month)))

# Post request attributes for the website
attributes = {
    "year": year,
    "month" : month,
    "day" : day,
    "submit" : "Convert"        
}

# Making a post request with the specified attributes and getting the data
response = requests.post(url, data=attributes)

# Parsing the data using the BeautifulSoup library
soup = BeautifulSoup(response.content, "lxml")

# Formatting the data to display only the date
print(soup.find_all("div", class_="inner")[1].text[3:])
