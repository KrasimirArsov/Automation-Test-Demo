from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


#step 1.
browser = webdriver.Chrome()

browser.get("http://demo.fluxday.io")
step_passing = True
try:
    email_form = browser.find_element_by_xpath("//*[@id=\"user_email\"]")
    pass_form = browser.find_element_by_xpath("//*[@id=\"user_password\"]")
    login_button = browser.find_element_by_xpath("//*[@id=\"new_user\"]/div[2]/div[3]/button")
except NoSuchElementException:
    step_passing = False

expected = step_passing
assert expected == True, "Step 1. failed! Not navigated to correct site."

#step 2.
email_form.send_keys("lead@fluxday.io")
pass_form.send_keys("password")
email_form.get_attribute("value")

expected = email_form.get_attribute("value") == "lead@fluxday.io" and pass_form.get_attribute("value") == "password"
assert expected == True, "Step 2. failed! Credentials not entered successfuly."

#step 3. final
login_button.click()
sleep(0.5)
user_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/ul[3]/li[1]/a")
expected = user_button.text == "Team Lead"
assert expected == True, "Step 3. failed! Not logged in as Team Lead."
sleep(1)

browser.close()
