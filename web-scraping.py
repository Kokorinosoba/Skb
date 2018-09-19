from selenium import webdriver
import pandas

# Settings
browser = webdriver.Chrome()
df = pandas.read_csv("default.csv", index_col=0)
url = "https://wav.tv/actresses/"

# CSS Selector Settings
PAGER_NEXT = "a.m-pagination--next.is-last.step"
POSTS = "div.m-actress-wrap"
ACTRESS_NAME = ".m-actress--title"
IMAGE = ".m-actress--thumbnail-img img"

# Execution Part

browser.get(url)

while True:
    if len(browser.find_elements_by_css_selector(PAGER_NEXT)) > 0:
        print("Starting to get posts...")
        posts = browser.find_elements_by_css_selector(POSTS)
        print(len(posts))
        for post in posts:
            try:
                name = post.find_element_by_css_selector(ACTRESS_NAME).text
                print(name)
                thumbnailURL = post.find_element_by_css_selector(IMAGE).get_attribute("src")
                print(thumbnailURL)
                se = pandas.Series([name, thumbnailURL], ["name", "image"])
                df = df.append(se, ignore_index=True)
            except Exception as e:
                print(e)

        btn = browser.find_element_by_css_selector(PAGER_NEXT).get_attribute("href")
        print("next url:{}".format(btn))
        browser.get(btn)
        print("Moving to next page......")
    else:
        print("No pager exist anymore")
        break

print("Finished Scraping. Writing CSV......")
df.to_csv("output.csv")
print("DONE")