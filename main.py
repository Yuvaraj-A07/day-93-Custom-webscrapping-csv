import requests
from bs4 import BeautifulSoup

steam_db_url = "https://rcdb.com/"

response = requests.get(url=steam_db_url)
# print(response.status_code)
steam_web = response.text
# print(steam_web)

soup = BeautifulSoup(steam_web, "html.parser")

roller_coast = soup.find(id='rrc_text').select(selector="p")
# title = roller_coast[2].find('span').text
# content = roller_coast[2].get_text()
#
# print(title)
# print(content)
#
# if title in content:
#     print(content.split(title))

roller_coast_dict = {}

for roller in roller_coast:
    title = roller.find('span').text
    content = roller.get_text().split(title)[1]
    roller_coast_dict[title] = f"{content}"


with open("roller_coast.csv", mode="a", encoding='utf-8') as csv_file:
    for key, value in roller_coast_dict.items():
        csv_file.write(f"{value},")
    csv_file.write("\n")

print(roller_coast_dict)

for i in roller_coast_dict:
    print(i)

