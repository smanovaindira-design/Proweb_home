from pygments.styles.dracula import comment
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class CommentPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_homework = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-homework.home__education-homework-works > div.tab-content.home__homeworks-tabview > div > div.home__works > div > div > div:nth-child(2) > div.avatar.baseavatar.baseavatar_go.baseavatar-small.home__homework-go")
        self.comment = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label")
        self.btn_send = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > button")


    def click_btn_homework(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_homework)).click()

    def input_comment(self, comment):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.presence_of_element_located(self.comment)).send_keys(comment)

    def click_btn_send(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_send)).click()
