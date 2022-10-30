# player = {
#     "given name" : "Ty",
#     "first name" : "Kim",
#     "age" : 12 , 
#     "Born" : "Korea",
#     "favor_food" : ["Kimchi","Meat","pizza","hanburger"]
# }

# player["job"] = "Teacher"
# player["favor_food"].append("Noodle")
# print (player)



mydata = {}
def add_dic(a,b):
    mydata[a] = b

add_dic("age",12)
print (mydata)



from requests import get
#Change URL
websites =(
    "https://google.com",
    "naver.com",
    "facebook.com",
    "twitter.com",
    "amazon.jp"
)

results = {

}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    reponse = get(website)
    if reponse.status_code == 200:
        results[website] = "OK"
    else :
        results[website] = "FAILED"
    # print(reponse.status_code)
print(results)
