
from bs4 import BeautifulSoup
from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"

reponse = get(f"{base_url}{search_term}")
if reponse.status_code != 200:
    print ("We could not find website")
else : # 웹사이트가 존재 한다면
    results = [] # 리스트를 만들고
    soup = BeautifulSoup(reponse.text, "html.parser") #웹 사이트의 html을 beautifulsoup를 이용해서 변수에 담고
    jobs = (soup.find_all("section", class_="jobs")) # class가 jobs인 section을 변수에 담고
    for job_selction in jobs:
        job_post = job_selction.find_all("li")
        job_post.pop(-1) # job변수의 li를 job_post에 담는데 마지막 하나는 제외한다
        # for job_title in job_post:
        #     title = job_title.find_all(class_="title")
        #     print(title)
        for post in job_post:
            anchors = post.find_all("a") # job_post 의 a 태그를 변수에 담고
            #anchor.pop(0)
            anchor = anchors[1] #첫번쨰것만 다시 변수에 담고
            link = anchor["href"] #  
            company,kind,region = anchor.find_all("span",class_="company") #각각의 값을 각각의 변수에 넣고
            title = anchor.find("span", class_="title") # title을 변수에 넣고
            job_data = { 
                "company" : company.string,
                "region" : region.string,
                "posion" : title.string,
            } # 필요한 값의 string값만 dictionary에 저장
            results.append(job_data) # add dictionary data to result list 
            for result in results :
                print (result)
                print ("..........................................................")
            # print (company,kind,region)
            #print (company.text,kind.text,region.text)
            #혼자 beautiful soup연습 해 봄
            # title = post.find(class_="title")
            # company = post.find(class_="company")
            # print ("Company name :", company.text, "/","Job Title :",title.text)
