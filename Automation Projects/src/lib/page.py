from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random, time


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    url = "https://staging.brandsignals.io//"

    def enter_username(self, xpath: str, username: str):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, xpath).send_keys(username)

    def enter_password(self, xpath: str, password: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(password)

    def click_login_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        return "Invalid Credentials" not in self.driver.page_source


class Click(BasePage):
    def Click_button(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()


class SendKeys(BasePage):
    def send_keys(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)


def get_selection_list(driver, xpath):
    select_options = driver.find_elements(By.XPATH, f"{xpath}/option")
    options = []
    # getting option
    for option in select_options:
        options.append(option.get_attribute("value"))
    rand_option = random.choice(options[1:])
    # selection
    select = Select(driver.find_element(By.XPATH, xpath))
    select.select_by_value(rand_option)
    return rand_option


def get_selection_lists(driver, xpath):
    select_options = driver.find_elements(By.XPATH, f"{xpath}/option")
    options = []
    # getting option
    for option in select_options:
        options.append(option.get_attribute("value"))
    rand_option = random.choice(options[1:])
    # selection
    select = Select(driver.find_element(By.XPATH, xpath))
    select.select_by_value(rand_option)
    return rand_option


def get_selection_listss(driver, xpath):
    select_options = driver.find_elements(By.XPATH, f"{xpath}/option")
    options = []
    # getting option
    for option in select_options:
        options.append(option.get_attribute("value"))
    rand_option = random.choice(options[1:])
    # selection
    select = Select(driver.find_element(By.XPATH, xpath))
    select.select_by_value(rand_option)
    return rand_option


def get_key_word(
    driver,
    xpath="div.potential-keywords:not(.Local-keywords)  ul.potential-keyword-list li",
):
    select_Keyword = driver.find_elements(By.CSS_SELECTOR, xpath)
    rand_option = random.choice(select_Keyword)
    try:
        rand_option.click()
        time.sleep(1)
        rand_option = random.choice(select_Keyword)
        rand_option.click()
        time.sleep(1)
        rand_option = random.choice(select_Keyword)
        rand_option.click()
        return rand_option
        time.sleep(1)
    except:
        pass


def get_key_wordsss(
    driver,
    xpath="div.potential-keywords:not(.Local-keywords)  ul.potential-keyword-list li",
):
    select_Keyword = driver.find_elements(By.CSS_SELECTOR, xpath)
    rand_option = random.choice(select_Keyword)
    try:
        rand_option.click()
        time.sleep(1)
        rand_option = random.choice(select_Keyword)
        rand_option.click()
        time.sleep(1)
        rand_option = random.choice(select_Keyword)
        rand_option.click()
        return rand_option
        time.sleep(1)
    except:
        pass


def get_key_words(
    driver,
    xpath="div.potential-keywords:not(.Local-keywords)  ul.potential-keyword-list li",
):
    select_Keyword = driver.find_elements(By.CSS_SELECTOR, xpath)
    rand_option = random.choice(select_Keyword)
    try:
        rand_option.click()
        return rand_option
        time.sleep(0.5)
    except:
        pass


# def get_selection_listname(driver, xpath):
#     # select_options = driver.find_elements(By.XPATH, f"{xpath}/option")
#     # options = []
#     # # getting option
#     # for option in select_options:
#     #     options.append(option.get_attribute('value'))
#     # rand_option = random.choice(options)
#     # selection
#     select = Select(driver.find_element(By.XPATH, xpath))
#     select.select_by_value("Agent Name or 4")
