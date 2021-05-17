import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")


code_url = "https://www.iban.com/currency-codes"
currency_url = "https://transferwise.com/gb/currency-converter/"


countries = []

codes_request = requests.get(code_url)
codes_soup = BeautifulSoup(codes_request.text, "html.parser")

table = codes_soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)


def ask_country(text):
  print(text)
  try:
    choice = int(input("#: "))
    if choice >= len(countries) or choice < 0:
      print("Choose a number from the list.")
      return ask_country(text)
    else:
      print(f"{countries[choice]['name']}")
      return countries[choice]
  except ValueError:
    print("That wasn't a number.")
    return ask_country(text)


def ask_amount(a_country, b_country):
  try:
    print(f"\nHow many {a_country['code']} do you want to convert to {b_country['code']}?")
    amount = int(input())
    return amount
  except ValueError:
    print("That wasn't a number.")
    return ask_amount(a_country, b_country)