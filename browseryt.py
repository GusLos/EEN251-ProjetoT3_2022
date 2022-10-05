# https://www.askpython.com/python/python-identifiers-rules-best-practices#:~:text=Python%20Identifier%20Naming%20Best%20Practices%20Class%20names%20should,Uppercase%20for%20the%20first%20character%20of%20each%20word.
# https://www.w3schools.com/tags/ref_av_dom.asp

from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

class BrowserYT():

    def __init__(self) -> None:
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.url = 'https://www.youtube.com/'

    def open_youtube(self) -> None:
        self.driver.get(self.url)

    def close_youtube(self) -> None:
        self.driver.get('data:,')

    def quit_youtube(self) -> None:
        self.driver.quit()

    def find_element(self, xpath: str) -> WebElement:
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except Exception as e:
            pass
            # print(f'Error on find_element: {xpath}')
            # print(f'Error raised: {e}')
            # self.close_youtube()
    
    def wait_for_element(self, xpath: str, time_limit: int = 50) -> None:
        try:
            WebDriverWait(self.driver, time_limit).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            pass
            # print(f'Error on wait_for_element: {xpath}')
            # print(f'Error raised: {e}')
            # self.close_youtube()
            
    def wait_for_clickable_element(self, xpath: str, time_limit: int = 50) -> None:
        try:
            WebDriverWait(self.driver, time_limit).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except Exception as e:
            pass
            # print(f'Error on wait_for_clickable_element: {xpath}')
            # self.close_youtube()

    def wait_and_get_element(self, xpath: str, time_limit: int = 50) -> WebElement:
        self.wait_for_element(xpath=xpath, time_limit=time_limit)
        return self.find_element(xpath)

    def wait_and_get_clickable_element(self, xpath: str, time_limit: int = 50) -> WebElement:
        self.wait_for_clickable_element(xpath=xpath, time_limit=time_limit)
        return self.find_element(xpath)

    def search_youtube(self, query: str) -> None:
        search_Box = self.wait_and_get_element('//ytd-searchbox')
        search_Box.send_keys(query)
        search_Button = self.wait_and_get_clickable_element('//button[@id="search-icon-legacy"]')
        search_Button.click()

    def select_youtube_video(self, option:str = '1') -> None:
        video = self.wait_and_get_clickable_element(f'//ytd-video-renderer[{option}]/div[@id="dismissible"]/div/div[@id="meta"]/div/h3/a[@id="video-title"]')
        video.click()

    def yt_fullscreen_button(self) -> WebElement:
        """Não é confiavel = NÃO USAR
        """
        fullscreen_button = self.wait_and_get_clickable_element('//button[@class="ytp-fullscreen-button ytp-button"]')
        fullscreen_button.click()
        return fullscreen_button

    def yt_video_is_paused(self) -> bool:
        video = self.wait_and_get_element('//div[@id="movie_player"]/div[1]/video')#criar elemento video da classe ? self.video?
        return self.driver.execute_script("return arguments[0].paused;", video)

    def yt_play_button(self) -> WebElement:
        """Não é confiavel = NÃO USAR
        """
        play_button = self.wait_and_get_clickable_element('//button[@class="ytp-play-button ytp-button"]',10)
        play_button.click()
        return play_button

    def yt_play_video(self) -> None:
        # Se video acaba, e usa essa função, ele recomeça 
        video = self.wait_and_get_element('//div[@id="movie_player"]/div[1]/video')#criar elemento video da classe ? self.video?
        if self.yt_video_is_paused():
            self.driver.execute_script("arguments[0].play();", video)
        else: 
            self.driver.execute_script("arguments[0].pause();", video)

    def yt_mute_button(self) -> WebElement:
        """Não é confiavel = NÃO USAR
        """
        mute_button = self.wait_and_get_clickable_element('//button[@class="ytp-mute-button ytp-button"]')
        mute_button.click()
        return mute_button

    def yt_mute_video(self) -> None:
        video = self.wait_and_get_element('//div[@id="movie_player"]/div[1]/video') #criar elemento video da classe ? self.video?
        self.driver.execute_script("arguments[0].muted = true;", video) 

    def yt_unmute_video(self) -> None:
        video = self.wait_and_get_element('//div[@id="movie_player"]/div[1]/video')#criar elemento video da classe ? self.video?
        self.driver.execute_script("arguments[0].muted = false;", video) 

    def yt_video_playing(self) -> bool:
        player_status = self.driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        return True if player_status else False

    def yt_ad_skip_button(self) -> WebElement:
        ad_skip_button = self.wait_and_get_clickable_element('//button[@class="ytp-ad-skip-button ytp-button"]',0)
        ad_skip_button.click()
        return ad_skip_button

    #   yt_promo_close ?
    def yt_promo_skip(self) -> None:
        self.wait_and_get_clickable_element('//yt-button-renderer[@id="dismiss-button"]').click()
        pass

    def yt_check_ad(self, time_limit: int = 0) -> bool:
        try:
            WebDriverWait(self.driver, time_limit).until(EC.invisibility_of_element((By.XPATH, '//div[@class="ytp-ad-player-overlay"]')))
            return False
        except:
            return True

    def run_yt_auto(self, query: str) -> None:
        self.open_yt_video(query)
        self.yt_mute_video()
        while self.yt_video_playing():
            if self.yt_check_ad():
                self.skip_yt_ad()
            # x = input('pausar?')
            # if x == 's':
            #     self.yt_play_video()
        self.close_youtube()

    def open_yt_video(self, query: str) -> None:
        self.open_youtube()
        self.search_youtube(query=query)
        self.select_youtube_video()

    def skip_yt_ad(self) -> None:
        while self.yt_video_playing(): # tirar ou deixar?
            if self.yt_check_ad():
                self.yt_mute_video()
                try:
                    self.yt_ad_skip_button()
                except:
                    pass        
            if not self.yt_check_ad():
                self.yt_unmute_video()
                return

    # def yt_video(self) -> WebElement:
    #     yt_video = self.wait_and_get_element('//video[@class="video-stream html5-main-video"]')
    #     return yt_video
    pass

if __name__ == '__main__':
    you_tube = BrowserYT()
    # you_tube.sk
    you_tube.run_yt_auto('marvel spider man theme song')
    you_tube.quit_youtube()
    # you_tube.open_youtube()
    # you_tube.search_youtube('marvel spider man theme')
    # you_tube.select_youtube_video()
    
    # while not you_tube.driver.execute_script('return arguments[0].paused;', video):
    #     you_tube.driver.execute_script('arguments[0].pause();', video)

    # you_tube.driver.execute_script("arguments[0].play();", video)
    # status_p = you_tube.driver.execute_script('return document.readyState;')
    # print(f'Página está: {status_p}')

    # you_tube.yt_mute_video()

    # while you_tube.yt_video_playing:
    #     if you_tube.yt_check_ad():
    #         you_tube.yt_mute_video()
    #         try:
    #             you_tube.yt_ad_skip_button()
    #         except:
    #             pass        
    #     if not you_tube.yt_check_ad():
    #         # you_tube.driver.execute_script('arguments[0].pause();', video)
    #         you_tube.yt_unmute_video()
    #     if not you_tube.yt_video_playing():
    #         you_tube.close_youtube()
    #         break