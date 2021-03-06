from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


browser = webdriver.Chrome()

site_url = "http://demo.fluxday.io"
login_elements_present = True
login_email_data = "lead@fluxday.io"
login_pass_data = "password"

xp_email_form = "//*[@id=\"user_email\"]"
xp_pass_form = "//*[@id=\"user_password\"]"
xp_login_button = "//*[@id=\"new_user\"]/div[2]/div[3]/button"
xp_user_button = "/html/body/div[2]/div[1]/ul[3]/li[1]/a"


#step 1.

browser.get(site_url)

try:
    email_form = browser.find_element_by_xpath(xp_email_form)
    pass_form = browser.find_element_by_xpath(xp_pass_form)
    login_button = browser.find_element_by_xpath(xp_login_button)
except NoSuchElementException:
    login_elements_present = False

expected = login_elements_present
assert expected, "Step 1. failed! Not navigated to site correctly / elements missing."


#step 2.

email_form.send_keys(login_email_data)
pass_form.send_keys(login_pass_data)
email_form.get_attribute("value")

expected = email_form.get_attribute("value") == login_email_data and pass_form.get_attribute("value") == login_pass_data
assert expected, "Step 2. failed! Credentials not entered successfully."

email_form
#step 3. final

login_button.click()
sleep(1)

user_button = browser.find_element_by_xpath(xp_user_button)
expected = user_button.text == "Team Lead"
assert expected, "Step 3. failed! Not logged in as Team Lead."

browser.close()
