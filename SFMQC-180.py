from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


browser = webdriver.Chrome()

site_url = "http://demo.fluxday.io"
login_elements_present = True
user_button_present = True
login_email_data = "lead@fluxday.io"
login_pass_data = "password"

xp_email_form = "//*[@id=\"user_email\"]"
xp_pass_form = "//*[@id=\"user_password\"]"
xp_login_button = "//*[@id=\"new_user\"]/div[2]/div[3]/button"
xp_user_button = "/html/body/div[2]/div[1]/ul[3]/li[1]/a"
xp_remember_me_checkbox = "//*[@id=\"user_remember_me\"]"


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


#step 3.

remember_me_checkbox = browser.find_element_by_xpath(xp_remember_me_checkbox)
remember_me_checkbox.click()
sleep(1)
login_button.click()
sleep(1)

user_button = browser.find_element_by_xpath(xp_user_button)
expected = user_button.text == "Team Lead"
assert expected, "Step 3. failed! Not logged in as Team Lead."



#step 4. final
browser.close()
browser = webdriver.Chrome()
browser.get("http://demo.fluxday.io")

try:
    user_button = browser.find_element_by_xpath(xp_user_button)
except NoSuchElementException:
    user_button_present = False

expected = user_button_present and user_button.text == "Team Lead"
assert expected, "Step 4. failed! Not logged in as Team Lead after re-loading the site."


browser.close()
