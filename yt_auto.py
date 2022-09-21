# https://www.askpython.com/python/python-identifiers-rules-best-practices#:~:text=Python%20Identifier%20Naming%20Best%20Practices%20Class%20names%20should,Uppercase%20for%20the%20first%20character%20of%20each%20word.

from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoYT:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.url = 'https://www.youtube.com/'
        pass

    def open_youtube(self) -> None:
        self.driver.get(self.url)

    def close_youtube(self) -> None:
        self.driver.close()
        pass

    def find_element(self, xpath: str) -> Any:
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except:
            print(f'Error on find_element: {xpath}')
    
    def wait_for_element(self, xpath: str) -> None:
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            print(f'Error on wait_for_element: {xpath}')

    def wait_for_clickable_element(self, xpath: str) -> None:
        try:
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except:
            print(f'Error on wait_for_clickable_element: {xpath}')

    def wait_and_get_element(self, xpath: str) -> Any:
        self.wait_for_element(xpath)
        return self.find_element(xpath)

    def wait_and_get_clickable_element(self, xpath: str) -> Any:
        self.wait_for_clickable_element(xpath)
        return self.find_element(xpath)

    def search_youtube(self, query: str) -> None:
        search_Box = self.wait_and_get_element('//ytd-searchbox')
        search_Box.send_keys(query)
        search_Button = self.wait_and_get_clickable_element('//button[@id="search-icon-legacy"]')
        search_Button.click()

    def select_youtube_video(self, option:str = '1') -> None:
        video = self.wait_and_get_element(f'//ytd-video-renderer[{option}]')
        video.click()

    def yt_mute_button(self) -> None:
        mute_button = self.wait_and_get_clickable_element('//button[@class="ytp-mute-button ytp-button"]')
        mute_button.click()

    def yt_check_ad(self) -> bool:
        try:
            WebDriverWait(self.driver, 0).until(EC.invisibility_of_element((By.XPATH, '//div[@class="ytp-ad-player-overlay"]')))
            return False
        except:
            return True



    def yt_video_time_duration(self) -> str:
        # time_duration = self.wait_and_get_element('//span[@class="ytp-time-duration"]')
        # time_duration = self.find_element('//span[@class="ytp-time-duration"]')
        time_duration = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, '//span[@class="ytp-time-duration"]')))
        time_duration = self.find_element('//span[@class="ytp-time-duration"]')
        return time_duration.text

    def yt_video_time_current(self) -> str:
        # time_current = self.wait_and_get_element('//span[@class="ytp-time-current"]')
        # time_current = self.find_element('//span[@class="ytp-time-current"]')
        time_current = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, '//span[@class="ytp-time-current"]')))
        time_current = self.find_element('//span[@class="ytp-time-current"]')
        return time_current.text


    # def set_url(self, url: str) -> None:
    #     self.url = url
    #     pass

    # def open_url(self) -> None:
    #     self.driver.get(self.url)
    #     pass

    pass
# #-----------------------pegar tempo-----------------------------------
# # 1
# # player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
# # print(player_status)
# # while player_status:
# #     print(player_status)

# # 2
# # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/div[1]/span[2]/span[3]")))
# # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/div[1]/span[2]/span[1]")))
# tempo_total = driver.find_element(By.XPATH, "//span[@class='ytp-time-duration']")
# tempo_atual = driver.find_element(By.XPATH, "//span[@class='ytp-time-current']")

# print(tempo_atual.text)
# print(tempo_total.text)

# # while tempo_total.text != tempo_atual.text:
# #     tempo_atual = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[25]/div[2]/div[1]/div[1]/span[2]/span[1]")
# #     tempo_atual = tempo_atual.text
# #     print(tempo_atual)



# # Ad = driver.find_element(By.XPATH, "//div[@class='video-ads ytp-ad-module']")
# #-----------------------1 modo para skip--------------------------------
# try:
#     while WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ytp-ad-text ytp-ad-preview-text']"))):
#         try:
#             Ad_Skip= WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")))
#             Ad_Skip = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")
#             Ad_Skip.click()
#         except Exception as e:
#             print('não tem ad para pular')
#             # print(f'Erro {e}')
#             # raise Exception
#             # break
# except:
#     print('Acabou os ads.')



# # -------------------------2 modo para skip---------------------------------











# # WebDriverWait(driver, 2).until_not(EC.presence_of_element_located((By.CLASS_NAME, "ytp-ad-player-overlay")))

# print('sai')




# mute_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-mute-button ytp-button']")))
# mute_btn.click()


# # tempo_total = driver.find_element(By.XPATH, "//span[@class='ytp-time-duration']")
# # tempo_atual = driver.find_element(By.XPATH, "//span[@class='ytp-time-current']")

# # print(tempo_atual.text)
# # print(tempo_total.text)


# # while True:
# #     tempo_total = driver.find_element(By.XPATH, "//span[@class='ytp-time-duration']")
# #     tempo_atual = driver.find_element(By.XPATH, "//span[@class='ytp-time-current']")
# #     if (tempo_atual.text == tempo_total.text):
# #         driver.close()
# #         break






# # pause_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-play-button ytp-button']")))
# # # input()
# # pause_btn.click()
# # pause_btn.click()


if __name__ == '__main__':
    you_tube = AutoYT()
    you_tube.open_youtube()
    you_tube.search_youtube('marvel spider man ps4 theme')
    you_tube.select_youtube_video()
    you_tube.yt_mute_button()
    # current_time = you_tube.yt_video_time_current()
    # print(you_tube.yt_video_time_current())
    # print(current_time)
    while True:
        if not you_tube.yt_check_ad():
            # you_tube.yt_mute_button()
            print('sai')
            break
    you_tube.driver.implicitly_wait(1)
    while True:
        if not you_tube.yt_check_ad():
            # you_tube.yt_mute_button()
            print('sai')
            break
    you_tube.yt_mute_button()
    print('fora')
    # you_tube.close_youtube()
    pass