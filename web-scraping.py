from selenium import webdriver
import pandas

# Settings
browser = webdriver.Chrome()
df = pandas.read_csv("default.csv", index_col=0)
url = "https://wav.tv/actresses/"

# CSS Selector
PAGER_NEXT = ""