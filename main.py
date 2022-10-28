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
        result[website] = "FAILED"
    # print(reponse.status_code)
print(results)
