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
    ele = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "search-icon-legacy")))
except:
    print("Timeout Exception: Page did not load within 10 seconds.")

Search_Box = driver.find_element(By.TAG_NAME, "ytd-searchbox")
query = 'spider man ps4 theme'
Search_Box.send_keys(query)



try:
    ele = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "search-icon-legacy")))
except:
    print("Timeout Exception: Page did not load within 10 seconds.")



Search_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "search-icon-legacy")))
# Search_Button = driver.find_element(By.ID, "search-icon-legacy")

Search_Button.click()
Search_Button.click()

# assert "results?search_query=" in driver.current_url

try:
    ele = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//ytd-video-renderer")))
except:
    print("Timeout Exception: Page did not load within 10 seconds.")
    raise Exception



select_video1=driver.find_element(By.XPATH, "//ytd-video-renderer").click()

mute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-mute-button ytp-button']")))
mute_btn.click()
# mute_btn.click()

#-----------------------pegar tempo-----------------------------------
# 1
# player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
# print(player_status)

# while player_status:
#     print(player_status)

# 2
# WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/div[1]/span[2]/span[3]")))
# WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/div[1]/span[2]/span[1]")))

tempo_total = driver.find_element(By.XPATH, "//span[@class='ytp-time-duration']")
tempo_atual = driver.find_element(By.XPATH, "//span[@class='ytp-time-current']")

print(tempo_atual.text)
print(tempo_total.text)

# while tempo_total.text != tempo_atual.text:
#     tempo_atual = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[25]/div[2]/div[1]/div[1]/span[2]/span[1]")
#     tempo_atual = tempo_atual.text
#     print(tempo_atual)



# Ad = driver.find_element(By.XPATH, "//div[@class='video-ads ytp-ad-module']")
#-----------------------1 modo para skip--------------------------------
try:
    while WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ytp-ad-text ytp-ad-preview-text']"))):
        try:
            Ad_Skip= WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")))
            Ad_Skip = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")
            Ad_Skip.click()
        except Exception as e:
            print('não tem ad para pular')
            # print(f'Erro {e}')
            # raise Exception
            # break
except:
    print('Acabou os ads.')



# -------------------------2 modo para skip---------------------------------









# WebDriverWait(driver, 2).until_not(EC.presence_of_element_located((By.CLASS_NAME, "ytp-ad-player-overlay")))

print('sai')










mute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-mute-button ytp-button']")))
mute_btn.click()

pause_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-play-button ytp-button']")))
# input()
pause_btn.click()
pause_btn.click()