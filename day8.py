import os
import csv
import requests
from bs4 import BeautifulSoup

# code by jichang kim
# URL 을 타고 들어갔을때 채용공고가 여러페이지 인경우 해결 못함 ex 노랑통닭
# 채용공고가 없는 사이트는 try exception 으로 해놨는데,,, 어떤 사이트인지 name 띄워주고 싶은데 이거 아직 못함

os.system("clear")
alba_url = "http://www.alba.co.kr"
companies = []

def get_companies():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  super_brand = soup.find("div" ,{"id" : "MainSuperBrand"}).find("ul", {"class" : "goodsBox"})
  company_list = super_brand.find_all("li")

  for a in company_list:
    link = a.find("a")["href"]
    name = a.find("span", {"class" : "company"}).text.replace("/", " ")
    company = {
      "name" : name,
      "link" : link
    }
    companies.append(company)
  return companies

def detail_jobs_save(input_name, input_url):
  detail_info = []
  file_name = input_name
  url = input_url
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  trs = soup.find("div" ,{"id" : "NormalInfo"}).find("tbody").find_all("tr", {"class" : ""})

  for tr in trs :
    try :
      name = tr.find("td", {"class" : "title"}).find("span", {"class" : "company"}).text
      location = tr.find("td", {"class" : "local"}).text
      working_hour = tr.find("td", {"class" : "data"}).text
      pay = tr.find("td", {"class" : "pay"}).text
      regDate = tr.find("td", {"class" : "regDate"}).text
    except AttributeError:
      print("No data")
      continue
    
    detail = {
      "location" : location,
      "name" : name,
      "working_hour" : working_hour,
      "pay" : pay,
      "regDate" : regDate
    }
    detail_info.append(detail)

  file = open(f"{file_name}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["Place", "Title", "Time", "Pay", "Date"])
  for a in detail_info:
    writer.writerow(list(a.values()))  


def main():
  get_companies()
  num_of_com = len(companies)
  for i in range(num_of_com):
    company_name, url = list(companies[i].values())
    detail_jobs_save(company_name, url)

main()