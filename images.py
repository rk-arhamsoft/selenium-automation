import time
import urllib.request
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

Driver = webdriver.Firefox()
celebs = ['Pervez Musharraf', 'Chaudhry Pervaiz Elahi', 'Zulfikar Ali Bhutto']
Driver.maximize_window()
Driver.get('https://www.forbes.com/powerful-people/list/#tab:overall')
time.sleep(3)
Driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
Driver.execute_script("window.scrollTo(500,1000)")
time.sleep(2)
Driver.execute_script("window.scrollTo(1000,1500)")
time.sleep(2)
Driver.execute_script("window.scrollTo(1500,2000)")
time.sleep(2)
Driver.execute_script("window.scrollTo(1500,document.body.scrollHeight)")
time.sleep(2)
input1 = Driver.find_elements(by=By.XPATH, value="//td[@class='name']/a[@class='exit_trigger_set']")

for i in range(len(input1) - 1):
    celebs.append(input1[i].text)

Driver.get('https://www.imdb.com/list/ls027763872/')
actors = Driver.find_elements(by=By.XPATH, value="//h3[@class='lister-item-header']/a")
print(len(actors))
for g in range(len(actors)):
    celebs.append(actors[g].text)

Driver.get('https://www.imdb.com/list/ls068010962/')
actors_bollywood = Driver.find_elements(by=By.XPATH, value="//h3[@class='lister-item-header']/a")
print(len(actors_bollywood))
for h in range(len(actors_bollywood)):
    celebs.append(actors_bollywood[h].text)

for i in range(len(celebs)):
    Driver.get('https://www.google.com/search?channel=fs&client=ubuntu&q=chrome')
    search_box = Driver.find_element(by=By.XPATH, value="//input[@class='gLFyf gsfi']")
    search_box.clear()
    search_box.send_keys(celebs[i])
    time.sleep(2)
    search = Driver.find_element(by=By.XPATH, value="//span[@class='z1asCe MZy1Rb']")
    search.click()
    time.sleep(2)
    images = Driver.find_element(by=By.XPATH, value="/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a")
    images.click()
    images_2 = Driver.find_elements(by=By.XPATH,
                                    value="//div[@class='bRMDJf islir']/img")
    try:
        for j in range(21):
            src = images_2[j].get_attribute('src')
            print(src)
            urllib.request.urlretrieve(src, f"{celebs[i]}{j}.png")
    except:
        pass
print(len(celebs))
