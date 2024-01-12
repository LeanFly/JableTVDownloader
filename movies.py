# In[0]:
import requests
from config import headers
from bs4 import BeautifulSoup
# from selenium import webdriver
from playwright.sync_api import sync_playwright
import yaml
from easydict import EasyDict


def movieLinks(url="https://jable.tv/hot"):
  with open("app.yaml", "r", encoding="utf-8") as f:
    data = yaml.load(f, yaml.FullLoader)
    data = EasyDict(data)
    browser = data.browser
    # encode_type = data.encode
    # media_path = data.media_path
    type_page = data.type_page
  
  links = []
  # dr = webdriver.Chrome()
  with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(browser) # ws://192.168.1.145:3333

    page = browser.new_page()
  # dr.get(url)
    page.goto(type_page)
    res = page.content()
  bs = BeautifulSoup(res,"html.parser")
  a_tags = bs.select('div.img-box>a')

  for a_tag in a_tags:
    links.append(a_tag['href'])
  print('获取到 {0} 個影片'.format(len(links)))
  print(links)
  return links

# %%
