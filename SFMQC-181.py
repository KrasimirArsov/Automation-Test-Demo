from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


browser = webdriver.Chrome()

site_url = "http://demo.fluxday.io"
login_elements_present = True
task_form_present = True
login_email_data = "lead@fluxday.io"
login_pass_data = "password"
task_title_data = "Regression test the fix of bug BJH-214"
task_description_data = "Run the regression tests for the recently fixed BJH-214"
task_team_data = "Testing"
task_start_date_data = "2018/03/13 08:00"
task_end_date_data = "2018/03/20 18:00"
task_priority_data = "Medium"

xp_email_form = "//*[@id=\"user_email\"]"
xp_pass_form = "//*[@id=\"user_password\"]"
xp_login_button = "//*[@id=\"new_user\"]/div[2]/div[3]/button"
xp_user_button = "//body/div[2]/div[1]/ul[3]/li[1]/a"
xp_new_task_button = "//body/div[1]/nav/section/ul[1]/li/a"
xp_task_title_form = "//*[@id=\"task_name\"]"
xp_task_description_form = "//*[@id=\"task_description\"]"
xp_task_team_form = "//*[@id=\"task_team_id\"]"
xp_task_start_date_form = "//*[@id=\"task_start_date\"]"
xp_task_end_date_form = "//*[@id=\"task_end_date\"]"
xp_task_priority_form = "//*[@id=\"task_priority\"]"
xp_task_save_button = "//*[@id=\"new_task\"]/div[3]/div[2]/input"
xp_created_task_title = "//*[@id=\"paginator\"]/a[1]/div/div[1]"


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
login_button.click()
sleep(1)

user_button = browser.find_element_by_xpath(xp_user_button)

expected = user_button.text == "Team Lead"
assert expected, "Step 2. failed! Not logged in correctly."


#step 3.

new_task_button = browser.find_element_by_xpath(xp_new_task_button)
new_task_button.click()
sleep(1)

try:
    task_title_form = browser.find_element_by_xpath(xp_task_title_form)
    task_description_form = browser.find_element_by_xpath(xp_task_description_form)
    task_team_form = browser.find_element_by_xpath(xp_task_team_form)
    task_start_date_form = browser.find_element_by_xpath(xp_task_start_date_form)
    task_end_date_form = browser.find_element_by_xpath(xp_task_end_date_form)
    task_priority_form = browser.find_element_by_xpath(xp_task_priority_form)
except NoSuchElementException:
    task_form_present = False

expected = task_form_present
assert expected, "Step 3. failed! New task form haven't loaded corectly."


#step 4. final

task_title_form.send_keys(task_title_data)
task_description_form.send_keys(task_description_data)
task_team_form.send_keys(task_description_data)
task_start_date_form.clear()
task_start_date_form.send_keys(task_start_date_data)
task_end_date_form.clear()
task_end_date_form.send_keys(task_end_date_data)
task_priority_form.send_keys(task_priority_data)

task_save_button = browser.find_element_by_xpath(xp_task_save_button)
task_save_button.click()

created_task_title = browser.find_element_by_xpath(xp_created_task_title)

expected = created_task_title.text == task_title_data
assert expected, "Step 4. failed! The task hasn't been created successfully"


browser.close()