from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import urllib.request

img_folder = os.path.abspath("Crawling_images")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
driver.maximize_window()
elem = driver.find_element(By.NAME, "q")
elem.send_keys("QA")
elem.send_keys(Keys.RETURN)

images = driver.find_elements(By.CSS_SELECTOR, ".wXeWr.islib.nfEiy")
count = 1
for image in images:
    image.click()
    time.sleep(3)
    imgUrl = driver.find_element(By.CSS_SELECTOR,
                                 ".r48jcc.pT0Scc.iPVvYb").get_attribute("src")
    image_path = os.path.join(
        img_folder, "crawling" + str(count) + ".jpg")
    urllib.request.urlretrieve(imgUrl, image_path)
    count = count + 1
