from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_schedule = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(3)")
        self.btn_see_lesson = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div > div.home__calendar-body > div.home__calendar-body-content > div:nth-child(31)")
        self.btn_time_lesson = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div > div.home__calendar-detail-content > div.home__calendar-detail-content-box > div:nth-child(2) > div")
        self.btn_group = (By.CSS_SELECTOR,"#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2)")
        self.btn_homework = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(4)")
        self.btn_new_homework = (By.CSS_SELECTOR,"#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div.lazyscroll > div > div:nth-child(1) > div.work-dropdown.homework-card_drop.grow > div")

    def click_btn_schedule(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_schedule)).click()

    def click_btn_see_lesson(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_see_lesson)).click()

    def click_btn_time_lesson(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_time_lesson)).click()

    def click_btn_group(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_group)).click()

    def click_btn_homework(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_homework)).click()

    def click_btn_new_homework(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(self.btn_new_homework)).click()
