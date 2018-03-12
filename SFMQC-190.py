from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def find_lead_okr_button():
    i = 1
    xp_base_user_entity = "//*[@id=\"pane2\"]/div[2]/div[{}]/div"
    label_xp_extension = "/div[2]/a"
    button_xp_extension = "/div[3]"
    while True:
        xp_current = xp_base_user_entity.format(i)
        current_label = browser.find_element_by_xpath(xp_current + label_xp_extension)
        if current_label.text == "Team Lead":
            xp_lead_button = xp_current + button_xp_extension
            return xp_lead_button
        else:
            i += 1


def check_okr_by_title(okr_title_to_check):
    xp_base_okr_entity_title = "//*[@id=\"pane2\"]/div[2]/a[{}]/div/div[1]"
    i = 2
    while True:
        xp_okr_entity_title = xp_base_okr_entity_title.format(i)
        okr_entity_title = browser.find_element_by_xpath(xp_okr_entity_title)
        if okr_entity_title.text == okr_title_to_check:
            return True
        else:
            i += 1



browser = webdriver.Chrome()

site_url = "http://demo.fluxday.io"
login_elements_present = True
new_ork_elements_present = True
login_email_data = "lead@fluxday.io"
login_pass_data = "password"
okr_name_data = "Test name"
okr_start_date_data = "2018-01-01"
okr_end_date_data = "2018-03-12"
okr_objective_data = "Test objective"
okr_key_resault_1_data = "Test key result 1"
okr_key_resault_2_data = "Test key result 2"


xp_email_form = "//*[@id=\"user_email\"]"
xp_pass_form = "//*[@id=\"user_password\"]"
xp_login_button = "//*[@id=\"new_user\"]/div[2]/div[3]/button"
xp_user_button = "//body/div[2]/div[1]/ul[3]/li[1]/a"
xp_users_button = "//body/div[2]/div[1]/ul[2]/li[5]/a"
xp_section_title = "//*[@id=\"pane2\"]/div[1]/div"
xp_new_okr_button = "//*[@id=\"pane2\"]/div[2]/a[1]"
xp_okr_name_field= "//*[@id=\"okr_name\"]"
xp_okr_start_date_field= "//*[@id=\"okr_start_date\"]"
xp_okr_end_date_field= "//*[@id=\"okr_end_date\"]"
xp_okr_objective_field= "//*[@id=\"okr_objectives_attributes_0_name\"]"
xp_okr_key_resault_1_field= "//*[@id=\"okr_objectives_attributes_0_key_results_attributes_0_name\"]"
xp_ork_key_resault_2_field= "//*[@id=\"okr_objectives_attributes_0_key_results_attributes_1_name\"]"
xp_new_okr_save_button = "//*[@id=\"new_okr\"]/div[3]/div[2]/input"

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

users_button = browser.find_element_by_xpath(xp_users_button)
users_button.click()
sleep(0.5)

section_title = browser.find_element_by_xpath(xp_section_title)

expected = section_title.text == "Users"
assert expected, "Step 3. failed! Not in the Users section."


#step 4.

lead_okr_button = browser.find_element_by_xpath(find_lead_okr_button())
lead_okr_button.click()

section_title = browser.find_element_by_xpath(xp_section_title)

expected = section_title.text == "OKR"
assert expected, "Step 4. failed! Not in the OKR section"


#step 5.

new_okr_button = browser.find_element_by_xpath(xp_new_okr_button)
new_okr_button.click()
sleep(0.5)

try:
    okr_name = browser.find_element_by_xpath(xp_okr_name_field)
    okr_start_date = browser.find_element_by_xpath(xp_okr_start_date_field)
    okr_end_date = browser.find_element_by_xpath(xp_okr_end_date_field)
    okr_objective = browser.find_element_by_xpath(xp_okr_objective_field)
    okr_key_resault_1 = browser.find_element_by_xpath(xp_okr_key_resault_1_field)
    ork_key_resault_2 = browser.find_element_by_xpath(xp_ork_key_resault_2_field)
except NameError:
    new_ork_elements_present = False

expected = new_ork_elements_present
assert expected, "Step 5. failed! New OKR form has not loaded successfully."


#step 6. final

okr_name.send_keys(okr_name_data)
okr_start_date.send_keys(okr_start_date_data)
okr_end_date.send_keys(okr_end_date_data)
okr_objective.send_keys(okr_objective_data)
okr_key_resault_1.send_keys(okr_key_resault_1_data)
ork_key_resault_2.send_keys(okr_key_resault_2_data)

new_okr_save_button = browser.find_element_by_xpath(xp_new_okr_save_button)
new_okr_save_button.click()

expected = check_okr_by_title(okr_name_data)
assert expected, "Step 6. failed! OKR not successfully created."


browser.close()
