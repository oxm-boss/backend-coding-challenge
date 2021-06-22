import requests
import datetime

def get_languages_data():
    # Date before the last 30 days

    date_full_version = datetime.datetime.now() - datetime.timedelta(days=30)
    date_ = date_full_version.strftime("%Y-%m-%d")
    print("[INFO] Starting Date: {}".format(date_))

    # Make request and get Trending Repos from Github
    url  = "https://api.github.com/search/repositories?q=created:>{}&sort=stars&order=desc".format(date_)
    print("[INFO] url: {}".format(url))

    response = requests.get(url)
    json_data = response.json()
    
    repos_items = json_data["items"]

    ## getting languages from each repository
    lang_dict = dict()
    for repository in repos_items:
        lang_url  = repository["languages_url"]
        lang_data_api = requests.get(lang_url).json()
        lang_list = list(lang_data_api.keys())
        for language in lang_list:
            lang_data = dict()
            if language in lang_dict:
                lang_data = lang_dict[language]
                lang_data["count"] += 1
                lang_data["repositories"].append(repository["full_name"])
            else:
                lang_data["name"]  = language
                lang_data["count"] = 1
                lang_data["repositories"] = [repository["full_name"]]
                lang_dict[language] = lang_data
            del lang_data
    return [lang_data for _, lang_data in lang_dict.items()]

if __name__ == "__main__":
    lang_dict = get_languages_data()
    print(lang_dict)

