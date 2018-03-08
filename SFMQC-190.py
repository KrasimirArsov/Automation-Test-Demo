from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import sys

#step 1.
browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://demo.fluxday.io")
step_passing = True
try:
    email_form = browser.find_element_by_xpath("//*[@id=\"user_email\"]")
    pass_form = browser.find_element_by_xpath("//*[@id=\"user_password\"]")
    login_button = browser.find_element_by_xpath("//*[@id=\"new_user\"]/div[2]/div[3]/button")
except NoSuchElementException:
    #raise AssertionError('..')
    browser.close()
    step_passing = False

expected = step_passing
assert expected == True, "Step 1. failed! Not navigated to correct site."


#step 2.
email_form.send_keys("lead@fluxday.io")
pass_form.send_keys("password")
login_button.click()

user_button = browser.find_element_by_xpath("//body/div[2]/div[1]/ul[3]/li[1]/a")
expected = user_button.text == "Team Lead"
assert expected == True, "Step 2. failed! Credentials not entered successfuly."


#step 3.
users_button = browser.find_element_by_xpath("//body/div[2]/div[1]/ul[2]/li[5]/a")
users_button.click()
sleep(0.5)

users_title = browser.find_element_by_xpath("//*[@id=\"pane2\"]/div[1]/div")
assert users_title.text == "Users", "Step 3. failed! Users menu not present."


#step 4.
okr_button = browser.find_element_by_xpath("//*[@id=\"pane2\"]/div[2]/div[2]/div/div[3]/a")
okr_button.click()
sleep(0.5)

okr_title = browser.find_element_by_xpath("//*[@id=\"pane2\"]/div[1]/div[1]/div")
