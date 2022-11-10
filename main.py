from bs4 import BeautifulSoup
from requests import get
from extractors.wwr import extract_wwr_job
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Options = Options()
# Options.add_argument("--no-sandbox")
# Options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=Options)
browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(browser.page_source,"html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)

