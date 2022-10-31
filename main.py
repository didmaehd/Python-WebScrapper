
from unittest import result
from bs4 import BeautifulSoup
from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"

reponse = get(f"{base_url}{search_term}")
if reponse.status_code != 200:
    print ("We could not find website")
else :
    soup = BeautifulSoup(reponse.text, "html.parser")
    jobs = (soup.find_all("section", class_="jobs"))
    for job_selction in jobs:
        job_post = job_selction.find_all("li")
        job_post.pop(-1)
        # for job_title in job_post:
        #     title = job_title.find_all(class_="title")
        #     print(title)
        for post in job_post:
            # print (post)
            # print(".......................................................")
            title = post.find(class_="title")
            company = post.find(class_="company")
            print ("Company name :", company.text, "/","Job Title :",title.text)
