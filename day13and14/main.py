"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import requests
from bs4 import BeautifulSoup

def get_job(job):
  URL = f"https://remoteok.io/remote-dev+{job}-jobs"
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  jobs_table = soup.find("body")
  # jobs = jobs_table.find_all("tbody")
  # .find("tr", {"data-url" : "remote"})
  print(soup)

get_job("python")