import requests
import datetime

# Date before the last 30 days

date_full_version = datetime.datetime.now() - datetime.timedelta(days=30)
date = date_full_version.strftime("%Y-%m-%d")
print("[INFO] Starting Date: {}".format(date))

# Make request and get Trending Repos from Github
url  = "https://api.github.com/search/repositories?q=created:>{}&sort=stars&order=desc".format(date)

response = requests.get(url)
json_data = response.json()

repos_items = json_data["items"]

## getting languages from each repository
lang_dict = dict()
for repository in repos_items:
    lang_url  = repository["languages_url"]
    lang_data = requests.get(lang_url).json()
    lang_list = list(lang_data.keys())
    for language in lang_list:
        lang_data = dict()
        if language in lang_dict:
            lang_data = lang_dict[language]
            lang_data["count"] += 1
            lang_data["repositories"].append(repository["full_name"])
        else:
            lang_data["count"] = 1
            lang_data["repositories"] = [repository["full_name"]]
            lang_dict[language] = lang_data

print(lang_dict)

#languages = [requests.get(lang_url).json() for lang_url in repos_utems]
#print(repos_items[0].keys())
#print(repos_items.keys())
