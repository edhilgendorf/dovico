from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import yaml

# TODO check for vacation hours, if 8 then remove all cells for that day
# TODO update to be from sunday to saturday
# TODO refactor


def switch_to_time_frame():
    for frame in [1, 0, 2, 1, 1]:
        driver.switch_to.frame(frame)


def switch_to_desc_frame():
    driver.switch_to.default_content()
    for frame in [1, 0, 2, 1, 2]:
        driver.switch_to.frame(frame)


def update_cell(day, row, text, hours):
    driver.find_element(
        By.XPATH, "//tr["
        + row + "]/td["
        + day + "]/div/div/table/tbody/tr/td/div").click()

    driver.find_element(
        By.XPATH, "//table[@id=\'tblCSG\']/tbody/tr["
        + row + "]/td["
        + day + "]/div/div/table/tbody/tr/td/div/input").send_keys(hours)


def update_desc(text):
    description_box = driver.find_element(By.CSS_SELECTOR, "textarea")
    description_box.click()
    description_box.clear()
    description_box.send_keys(text)


def login(company, user, password):
    driver.find_element_by_id("txtCompanyName").send_keys(
        str(company))
    driver.find_element_by_id("txtUserName").send_keys(
        str(user))
    driver.find_element_by_id("txtPassword").send_keys(
        str(password))
    driver.find_element_by_id("txtPassword").send_keys(Keys.RETURN)
    print("Go to correct week")
    sleep(15)  # TODO replace this with an EC to wait for element load


def init_driver():
    driver = webdriver.Firefox()
    driver.get("https://login.dovico.com/#Login")
    return driver


def set_default_hours():
    update_cell(day, str(cat["row"]),
                str(cat["text"]),
                str(cat["hours"]["default"]))


def set_hours_explicit():
    if day == "3":
        if "mon" in cat["hours"]:
            update_cell(day, str(cat["row"]),
                        str(cat["text"]),
                        str(cat["hours"]["mon"]))
        else:
            if "default" in cat["hours"]:
                set_default_hours()
    elif day == "4":
        if "tue" in cat["hours"]:
            update_cell(day, str(cat["row"]),
                        str(cat["text"]),
                        str(cat["hours"]["tue"]))
        else:
            if "default" in cat["hours"]:
                set_default_hours()
    elif day == "5":
        if "wed" in cat["hours"]:
            update_cell(day, str(cat["row"]),
                        str(cat["text"]),
                        str(cat["hours"]["wed"]))
        else:
            if "default" in cat["hours"]:
                set_default_hours()
    elif day == "6":
        if "thu" in cat["hours"]:
            update_cell(day, str(cat["row"]),
                        str(cat["text"]),
                        str(cat["hours"]["thu"]))
        else:
            if "default" in cat["hours"]:
                set_default_hours()
    elif day == "7":
        if "fri" in cat["hours"]:
            update_cell(day, str(cat["row"]),
                        str(cat["text"]),
                        str(cat["hours"]["fri"]))
        else:
            if "default" in cat["hours"]:
                set_default_hours()
    switch_to_desc_frame()
    update_desc(str(cat["text"]))
    driver.switch_to.default_content()


with open("dovico.yml", 'r') as stream:
    driver = init_driver()
    do_yml = yaml.safe_load(stream)
    login(do_yml["company"], do_yml["user"], do_yml["pass"])
    for day in ["3", "4", "5", "6", "7"]:  # Monday through friday:
        for cat in do_yml["rows"]:
            driver.switch_to.default_content()
            switch_to_time_frame()
            hours = cat["hours"]
            if type(hours) is dict:
                set_hours_explicit()
            else:
                update_cell(day, str(cat["row"]),
                            str(cat["text"]),
                            str(cat["hours"]))
                switch_to_desc_frame()
                update_desc(str(cat["text"]))
                driver.switch_to.default_content()
                sleep(1)
