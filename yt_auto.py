from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

# class element_not_in(object):
#     def __init__(self, locator) -> None:
#         self.locator = locator;

#     def __call__(self, driver) -> Any:
#         element = driver.find_element(*self.locator)
#     pass

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.youtube.com/')

# driver.find_element_by_id()

try:
    ele = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.TAG_NAME, "ytd-searchbox")))
except:
    print("Timeout Exception: Page did not load within 10 seconds.")


Search_Box = driver.find_element(By.TAG_NAME, "ytd-searchbox")
query = 'spider man ps4 theme'
Search_Box.send_keys(query)

Search_Button = driver.find_element(By.ID, "search-icon-legacy")
Search_Button.click()

try:
    ele = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//ytd-video-renderer")))
except:
    print("Timeout Exception: Page did not load within 10 seconds.")

select_video1=driver.find_element(By.XPATH, "//ytd-video-renderer").click()

mute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-mute-button ytp-button']")))
mute_btn.click()

Ad = driver.find_element(By.XPATH, "//div[@class='video-ads ytp-ad-module']")
# while True:
#     try:
#         print('entrei')
#         # Ad.find_element(By.CLASS_NAME, "ytp-ad-player-overlay")
#         WebDriverWait(Ad, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-ad-player-overlay")))
#     except:
#         break
#     pass
# WebDriverWait(driver, 3).until_not(EC.presence_of_element_located((By.CLASS_NAME, "ytp-ad-player-overlay")))
WebDriverWait(driver, 2).until_not(EC.presence_of_element_located((By.CLASS_NAME, "ytp-ad-player-overlay")))

print('sai')
# skipAd = driver.find_element(By.XPATH, "")
mute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-mute-button ytp-button']")))
mute_btn.click()

pause_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-play-button ytp-button']")))
# input()
pause_btn.click()
pause_btn.click()