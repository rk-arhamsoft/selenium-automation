import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

Driver = uc.Chrome()
Driver.get("https://www.youtube.com/")
Driver.maximize_window()
wait = WebDriverWait(Driver, 10)

print(Driver.title)
time.sleep(20)
