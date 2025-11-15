import time
from time import sleep
from pages.auth_page import AuthPage



from conftest import driver
from pages.auth_page import AuthPage
from pages.comment_page import CommentPage
from pages.home_page import HomePage
from pages.video_pages import VideoPage
from pages.comment_page import CommentPage

def test_auth (driver):
    driver.get ("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage (driver)
    auth_page.input_login("998903185900")
    auth_page.click_btn_next()
    auth_page.input_password("Indira15031968")
    auth_page.click_btn_submit()
    time.sleep(5)
    try:
        auth_page.click_btn_sessions()
        time.sleep(5)
        auth_page.click_btn_browser()
        time.sleep(5)
        auth_page.click_btn_finish()
    except:
        pass

    comment_page = CommentPage (driver)
    comment_page.click_btn_homework()
    time.sleep(5)
    comment_page.input_comment("Hello")
    time.sleep(5)
    # comment_page.click_btn_send()
    # time.sleep(5)


#     auth_page.click_btn_profile()
#     time.sleep(5)
#     auth_page.click_btn_exit()
#     time.sleep(5)
#     auth_page.click_btn_confirmation()
#
#     home_page=HomePage (driver)
#     home_page.click_btn_schedule()
#     time.sleep(10)
#     home_page.click_btn_see_lesson()
#     time.sleep(10)
#     home_page.click_btn_time_lesson()
#
#     home_page=HomePage (driver)
#     home_page.click_btn_group()
#     time.sleep(5)
#     home_page.click_btn_homework()
#     time.sleep(5)
#     home_page.click_btn_new_homework()
#     time.sleep(5)
#
#     video_page=VideoPage (driver)
#     video_page.click_btn_groups()
#     time.sleep(5)
#     video_page.click_btn_lessons()
#     time.sleep(5)
#     video_page.click_btn_new_video()
#     time.sleep(5)
#     video_page.click_btn_play()
#     time.sleep(5)
#     video_page.click_btn_fulscreen()
#     time.sleep(5)
#     video_page.click_btn_fullscreen_exit()
#     time.sleep(5)
#     try:
#         video_page.click_btn_stars()
#         time.sleep(5)
#         video_page.click_btn_stars_press()
#         time.sleep(5)
#     except:
#         pass

# def test_invalid_auth (driver):
#     driver.get ("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage (driver)
#     auth_page.input_login("9989011859000")
#     time.sleep(1)
#     auth_page.click_btn_next()
#     time.sleep(1)
#     auth_page.input_password("Indira10031968")
#     auth_page.click_btn_submit()
#
#

