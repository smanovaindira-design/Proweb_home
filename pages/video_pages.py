from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class VideoPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_groups = (By.CSS_SELECTOR,"#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2) > div.home-card__bot > div > div.avatar.baseavatar_go.home-card__bot-content-btn.baseavatar > span")
        self.btn_lessons = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.btn_new_video = (By.CSS_SELECTOR,"#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(3) > div.lesson-card")
        self.btn_play = (By.CSS_SELECTOR,"#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.btn_fullscreen = (By.CSS_SELECTOR,"#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen")
        self.btn_fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen-exit")
        self.btn_stars = (By.CSS_SELECTOR,"#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mb10 > div > div > div > span:nth-child(5)")
        self.btn_stars_press = (By.CSS_SELECTOR, "#dialog > div > div > div > div > div > button")

    def click_btn_groups(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_groups)).click()

    def click_btn_lessons(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_lessons)).click()

    def click_btn_new_video(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_new_video)).click()

    def click_btn_play(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_play)).click()

    def click_btn_fulscreen(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_btn_fullscreen_exit(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen_exit)).click()

    def click_btn_stars(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_stars)).click()

    def click_btn_stars_press(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_stars_press)).click()