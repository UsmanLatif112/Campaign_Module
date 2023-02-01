import time, csv
from uuid import uuid1
from typing import List
import pyautogui
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from lib.page import (
    LoginPage,
    Click,
    SendKeys,
    get_selection_list,
    get_key_word,
    get_key_words,
    get_selection_lists,
    get_selection_listss,
    get_key_wordsss,
)
from lib.resources import (
    LoginResources,
    CreateCampaignModuleResource,
    KeywordsResource,
    InAnalaysisTabResource,
    AnalaysisTabResource,
    EditCamapaignResource,
    SeachCamapignResource,
    DeleteCamapigninANAResource,
    DeleteCamapigninDELResource,
    CamPlayPauseLiveResource,
    CamPlayPauseAnaResource,
    CamAssignResource,
    LogoutBtnResource,
    AssignUserResource,
    RoleIdResources,
)

# Credentials===

USER_NAME = "Aimal_M18"
PASS_WORD = "Aimal@11"
USER_NAME_4 = "1Aimal_4"
pass_word_1 = "Aimal@11"

# Camapign Names===

NAME_CAMPAIGN = "Aimalraza054"
NAME_CAMPAIGN_EDIT_ANA = "Aimalraza083"
NAME_CAMPAIGN_EDIT_LIV = "Aimalraza349"
NAME_CAMPAIGN_EDIT_V_RE = "Aimalraza782"
NAME_CAMPAIGN_4 = "Aimalraza649"
NAME_CAMPAIGN_4_edit = "Aimalraza3467"

# GMBCID===

GMB_CID = "6867010774265153825"
GMB_CID_4 = "9941505210792148792"

# input==


# make CSV file===


def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = "w" if new else "a"
    with open(filename, mode, newline="") as f:
        f.writelines(data)


# Driver on login on webapp=====


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    # Login With role id2 to create campaign===

    login_page = LoginPage(driver)
    login_page.enter_username(LoginResources.USERNAME, USER_NAME)
    login_page.enter_password(LoginResources.PASSWORD, PASS_WORD)
    url_a = driver.current_url
    success = login_page.click_login_btn(LoginResources.LOGIN_BTN)
    make_csv("Campaign Report.csv", "Campaign Module\n")
    today = date.today()
    make_csv(
        "Campaign Report.csv",
        "Test Case,Scenario,Detailed Result,Urls,Result\n",
        new=False,
    )
    make_csv("Campaign Report.csv", '\n', new=False)
    make_csv("Campaign Report.csv", f'Date: {today}\n', new=False)

    if success:
        make_csv(
            "Campaign Report.csv",
            f"Login Credentials,Login With Correct Username & Password,Login Successful,{url_a}\n",
            new=False,
        )
    else:
        make_csv(
            "Campaign Report.csv",
            f"Login Credentials,Login With Correct Username & Password,Invalid Credentials,{url_a}n",
            new=False,
        )

    # Click on campaign button====

    Cam_Page = Click(driver)
    Cam_Page.Click_button(CreateCampaignModuleResource.Campaign_btn)
    url_b = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Campaign Module,Click on Campaign Button,Successful,{url_b}\n",
        new=False,
    )

    # Create Campaign====
    # select client====

    Cam_Page1 = Click(driver)
    Cam_Page1.Click_button(CreateCampaignModuleResource.Create_Campaign)
    url_c = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Click on Create Campaign Button,Successful,{url_c}\n",
        new=False,
    )
    time.sleep(1)
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Click select Client,Successful,{url_c}\n",
        new=False,
    )
    options_list = get_selection_list(
        driver, CreateCampaignModuleResource.Select_client_btn
    )
    time.sleep(1)

    # Check campain name validateion=====

    Cam_page3 = SendKeys(driver)
    Cam_page3.send_keys(CreateCampaignModuleResource.Enter_campaign_name, "@#!$%^&*")
    pop_nam = driver.find_element(
        By.XPATH, "//*[@class='my-3 text-danger warning-text']"
    ).text
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Check Special Characters are not allowed,{pop_nam},{url_c}\n",
        new=False,
    )

    time.sleep(1)

    cam_name = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page4 = SendKeys(driver)
    Cam_page4.send_keys(
        CreateCampaignModuleResource.Enter_campaign_name,
        "sdaffasdbkdfvgigouhfdoghodfhgodfhgfdhgdflhdflghldfhgldfghldfghldfhkldfhgldfghhldfkhgdflghldfkhggldfgf",
    )
    pop_nam1 = driver.find_element(
        By.XPATH, "//*[@class='my-3 text-danger warning-text']"
    ).text
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Check 100 Characters limitation are not allowed,{pop_nam1},{url_c}\n",
        new=False,
    )

    time.sleep(1)

    cam_name1 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page5 = SendKeys(driver)
    Cam_page5.send_keys(CreateCampaignModuleResource.Enter_campaign_name, NAME_CAMPAIGN)
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Enter Correct Campaign Name,Successful,{url_c}\n",
        new=False,
    )
    time.sleep(1)

    Cam_page6 = SendKeys(driver)
    Cam_page6.send_keys(
        CreateCampaignModuleResource.Enter_GMB_Cid, "275091129056086617511"
    )
    pop_nam2 = driver.find_element(
        By.XPATH, "//*[@class='mt-2 text-danger warning-text-create-camapaign-gmbcid']"
    ).text
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Check GMB Cid limit,{pop_nam2},{url_c}\n",
        new=False,
    )

    time.sleep(1)

    cam_name2 = driver.find_element(By.XPATH, "//*[@id='autocomplete']").clear()
    time.sleep(1)

    Cam_page6 = SendKeys(driver)
    Cam_page6.send_keys(CreateCampaignModuleResource.Enter_GMB_Cid, GMB_CID)
    time.sleep(2)

    Cam_Page7 = Click(driver)
    Cam_Page7.Click_button(CreateCampaignModuleResource.Check_GMB_CID)
    time.sleep(2)

    try:

        Business = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[@class='alert alert-success alert-dismissible fade show']",
                )
            )
        )

        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Enter Correct GMB CID,{Business.text},{url_c}\n",
            new=False,
        )

    except:

        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Enter Correct GMB CID,Successful,{url_c}\n",
            new=False,
        )

    time.sleep(1)
    driver.execute_script("window.scrollTo(0,100)")
    time.sleep(1)
    try:
        keyword = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='business-location']"))
        )
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        
    except:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(3)
    get_key_word(driver)

    time.sleep(3)

    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Add keywords,Successful,{url_c}\n",
        new=False,
    )
    time.sleep(3)
    

    Cam_Page10 = Click(driver)
    Cam_Page10.Click_button(CreateCampaignModuleResource.Hit_Submit_Analysis)
    try:
        pop_name4 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.ID,
                    "popUpMessage",
                )
            )
        )

        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Click on Submit for Analysis,{pop_name4.text},{url_c}\n",
            new=False,
        )
        
    except:
        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Click on Submit for Analysis,,{url_c}\n",
            new=False,
        )
    time.sleep(2)

    # Click on in analysis button and search camoaign======

    Cam_Page11 = Click(driver)
    Cam_Page11.Click_button(InAnalaysisTabResource.In_Analaysis_btn)
    url_d = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"In Analysis,Click on In Analysis Button,Successful,{url_d}\n",
        new=False,
    )
    time.sleep(5)

    Cam_page12 = SendKeys(driver)
    Cam_page12.send_keys(InAnalaysisTabResource.search_cam, NAME_CAMPAIGN)

    time.sleep(5)
    try:
        Cam_page12 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN}']",
                )
            )
        )
        pop_naam = driver.find_element(
            By.XPATH,
            f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN}']",
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "IN Analysis Tab",{pop_naam.text},{url_d}\n',
            new=False,
        )

    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "IN Analysis Tab",,{url_d}\n',
            new=False,
        )
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(5)

    # Click on analysis button and search camoaign=======

    Cam_Page12 = Click(driver)
    Cam_Page12.Click_button(AnalaysisTabResource.Analaysis_btn)
    make_csv(
        "Campaign Report.csv",
        f"Analysis Completed,Click on Analysis Button,Successful,{url_d}\n",
        new=False,
    )
    time.sleep(5)

    Cam_page13 = SendKeys(driver)
    Cam_page13.send_keys(AnalaysisTabResource.search_cam1, NAME_CAMPAIGN)

    try:
        Cam_page13 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN}']")
            )
        )
        pop_nam6 = driver.find_element(
            By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN}']"
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Analysis Completed Tab",{pop_nam6.text},{url_d}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Analysis Completed Tab",,{url_d}\n',
            new=False,
        )
    time.sleep(3)

    # Edit camapign from analysis completed======

    Cam_Page14 = Click(driver)
    Cam_Page14.Click_button(EditCamapaignResource.Edit_camapaign_btn1)
    time.sleep(1)

    Cam_Page15 = Click(driver)
    Cam_Page15.Click_button(EditCamapaignResource.Edit_camapaign_btn2)
    time.sleep(1)
    url_e = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f'Edit Campign,Click on Edit Campign in "Analaysis Completed",Successful,{url_e}\n',
        new=False,
    )
    time.sleep(5)

    # Check campaign name valiation while editing campaign======

    cam_name2 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page16 = SendKeys(driver)
    Cam_page16.send_keys(
        CreateCampaignModuleResource.Enter_campaign_name, "@##$!%^&*()_+="
    )
    time.sleep(1)
    pop_nam7 = driver.find_element(By.XPATH, "//*[@id='warning-text-id-cam']")
    make_csv(
        "Campaign Report.csv",
        f"Edit Campign,Check Special Characters while editing Campaign,{pop_nam7.text},{url_e}\n",
        new=False,
    )
    time.sleep(1)

    cam_name2 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()

    time.sleep(1)
    Cam_page17 = SendKeys(driver)
    Cam_page17.send_keys(
        CreateCampaignModuleResource.Enter_campaign_name,
        "sdaffasdbkdfvgigouhfdoghodfhgodfhgfdhgdflhdflghldfhgldfghldfghldfhkldfhgldfghhldfkhgdflghldfkhggldfgf",
    )
    time.sleep(1)
    pop_nam8 = driver.find_element(By.XPATH, "//*[@id='warning-text-id-cam']")
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Check 100 Characters limitation while editing Campaign,{pop_nam8.text},{url_e}\n",
        new=False,
    )
    time.sleep(1)

    cam_name2 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()

    time.sleep(1)
    Cam_page18 = SendKeys(driver)
    Cam_page18.send_keys(
        CreateCampaignModuleResource.Enter_campaign_name, NAME_CAMPAIGN_EDIT_ANA
    )
    time.sleep(1)
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Enter Correct Campaign Name,Successful,{url_e}\n",
        new=False,
    )
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,90)")

    try:

        Cam_Page19 = Click(driver)
        Cam_Page19.Click_button(CreateCampaignModuleResource.update_Bussiness)
        time.sleep(3)
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Click On Update Bussiness,Bussiness Updated Successfully!,{url_e}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Click On Update Bussiness,Bussiness Updated Successfully!,{url_e}\n",
            new=False,
        )
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,600)")

    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".tagsinputfield").send_keys(Keys.BACKSPACE)

    time.sleep(2)

    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Remove Keyword,Successful,{url_e}\n",
        new=False,
    )

    time.sleep(3)

    get_key_words(driver)

    time.sleep(3)
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Add New Keyword,Successful,{url_e}\n",
        new=False,
    )
    time.sleep(3)

    Cam_Page22 = Click(driver)
    Cam_Page22.Click_button(CreateCampaignModuleResource.Edit_camapaign)
    try:
        pop_name10 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "popUpMessage"))
        )
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Hit Resubmit for analysis,{pop_name10.text},{url_e}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Hit Resubmit for analysis,,{url_e}\n",
            new=False,
        )
    time.sleep(4)

    # Click on campaign Button======

    Cam_Page23 = Click(driver)
    Cam_Page23.Click_button(CreateCampaignModuleResource.Campaign_btn)
    url_f = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Campaign Module,Click on Campaign Button,Successful,{url_f}\n",
        new=False,
    )
    time.sleep(1)

    # Click on in analysis button after edit campaign======

    Cam_Page24 = Click(driver)
    Cam_Page24.Click_button(InAnalaysisTabResource.In_Analaysis_btn)
    make_csv(
        "Campaign Report.csv",
        f"In Analysis,Click on In Analysis Button,Successful,{url_f}\n",
        new=False,
    )
    time.sleep(5)

    Cam_page25 = SendKeys(driver)
    Cam_page25.send_keys(InAnalaysisTabResource.search_cam, NAME_CAMPAIGN_EDIT_ANA)

    try:
        Cam_page25 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN_EDIT_ANA}']",
                )
            )
        )
        pop_naem = driver.find_element(
            By.XPATH,
            f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN_EDIT_ANA}']",
        )

        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "IN Analysis Tab",{pop_naem.text},{url_f}\n',
            new=False,
        )

    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "IN Analysis Tab",,{url_f}\n',
            new=False,
        )
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(5)

    # Click on  analysis completed button after edit campaign=====

    Cam_Page26 = Click(driver)
    Cam_Page26.Click_button(AnalaysisTabResource.Analaysis_btn)
    make_csv(
        "Campaign Report.csv",
        f"Analysis Completed,Click on Analysis Button,Successful,{url_f}\n",
        new=False,
    )
    time.sleep(5)

    Cam_page27 = SendKeys(driver)
    Cam_page27.send_keys(AnalaysisTabResource.search_cam1, NAME_CAMPAIGN_EDIT_ANA)
    try:
        Cam_page27 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_EDIT_ANA}']")
            )
        )
        pop_nam12 = driver.find_element(
            By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_EDIT_ANA}']"
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Analysis Completed Tab",{pop_nam12.text},{url_f}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Analysis Completed Tab",,{url_f}\n',
            new=False,
        )
    time.sleep(3)

    # start campign from three dots from analysis completed tab====

    Cam_Page28 = Click(driver)
    Cam_Page28.Click_button(EditCamapaignResource.Edit_camapaign_btn1)
    time.sleep(3)

    Cam_Page29 = Click(driver)
    Cam_Page29.Click_button(EditCamapaignResource.live_Camp_btn)
    make_csv(
        "Campaign Report.csv",
        f"Start Campaign,Start Campaign OR Live Campaign,Successful,{url_f}\n",
        new=False,
    )
    time.sleep(5)

    # Click on live button=====

    Cam_Page2142 = Click(driver)
    Cam_Page2142.Click_button(CreateCampaignModuleResource.live_btn)
    time.sleep(5)

    # Seach camoaign in live tab=====

    Cam_page30 = SendKeys(driver)
    Cam_page30.send_keys(SeachCamapignResource.search_cam_live, NAME_CAMPAIGN_EDIT_ANA)

    try:
        Cam_page30 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='campaignListingLive']/tbody/tr/td[2]/div/a/h6[@title='{NAME_CAMPAIGN_EDIT_ANA}']")
            )
        )
        pop_nam13 = driver.find_element(
            By.XPATH, f"//*[@id='campaignListingLive']/tbody/tr/td[2]/div/a/h6[@title='{NAME_CAMPAIGN_EDIT_ANA}']"
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Live Tab",{pop_nam13.text},{url_f}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Live Tab",,{url_f}\n',
            new=False,
        )

    # Edit camapign from live=====

    Cam_Page31 = Click(driver)
    Cam_Page31.Click_button(EditCamapaignResource.ed_live_1)
    time.sleep(1)

    Cam_Page32 = Click(driver)
    Cam_Page32.Click_button(EditCamapaignResource.ed_live_2)
    url_g = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Edit Campaign from Live,Successful,{url_g}\n",
        new=False,
    )
    time.sleep(1)

    # check campaign name validation while editing campaign from live=====

    cam_nam12 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page33 = SendKeys(driver)
    Cam_page33.send_keys(CreateCampaignModuleResource.Cam_name_liv, "@##$%^&*()_+!")
    time.sleep(1)
    pop_nam14 = driver.find_element(By.XPATH, "//*[@id='warning-text-id-cam']").text
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Check Special Characters While Edit campaign from live,{pop_nam14},{url_g}\n",
        new=False,
    )
    time.sleep(1)

    cam_nam12 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page34 = SendKeys(driver)
    Cam_page34.send_keys(
        CreateCampaignModuleResource.Cam_name_liv,
        "sdaffasdbkdfvgigouhfdoghodfhgodfhgfdhgdflhdflghldfhgldfghldfghldfhkldfhgldfghhldfkhgdflghldfkhggldfgf",
    )
    time.sleep(1)
    pop_nam15 = driver.find_element(By.XPATH, "//*[@id='warning-text-id-cam']").text
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Check 100 Characters limitation  While Edit campaign from live,{pop_nam15},{url_g}\n",
        new=False,
    )
    time.sleep(1)

    cam_nam13 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page35 = SendKeys(driver)
    Cam_page35.send_keys(
        CreateCampaignModuleResource.Cam_name_liv, NAME_CAMPAIGN_EDIT_LIV
    )
    time.sleep(2)
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Enter Correct Campaign Name,Successful,{url_g}\n",
        new=False,
    )

    time.sleep(3)

    driver.execute_script("window.scrollTo(0,600)")

    time.sleep(2)
    try:
        Cam_Page36 = Click(driver)
        Cam_Page36.Click_button(CreateCampaignModuleResource.liv_upd_btn)
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Click on Update Bussiness,Bussiness Updated Successfully!,{url_g}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Click on Update Bussiness,Bussiness Updated Successfully!,{url_g}\n",
            new=False,
        )
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".tagsinputfield").send_keys(Keys.BACKSPACE)
    time.sleep(1)
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Remove Keyword while Editing Campaign from Live,Successful,{url_g}\n",
        new=False,
    )
    time.sleep(2)

    get_key_words(driver)

    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Add keyword while editing campaign from live ,Successful,{url_g}\n",
        new=False,
    )
    time.sleep(2)

    Cam_Page38 = Click(driver)
    Cam_Page38.Click_button(CreateCampaignModuleResource.cam_re_btn)
    time.sleep(1)

    try:
        pop_name16 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "popUpMessage"))
        )
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Hit Resubmit for analysis after edit campaign from live,{pop_name16.text},{url_g}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Hit Resubmit for analysis after edit campaign from live,,{url_g}\n",
            new=False,
        )
    time.sleep(1)

    Cam_Page39 = Click(driver)
    Cam_Page39.Click_button(CreateCampaignModuleResource.Campaign_btn)
    url_h = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Campaign Module,Click on Campaign Button,Successful,{url_h}\n",
        new=False,
    )
    time.sleep(2)

    # check campaign in analysis after edit from live=====

    Cam_Page40 = Click(driver)
    Cam_Page40.Click_button(InAnalaysisTabResource.In_Analaysis_btn)
    make_csv(
        "Campaign Report.csv",
        f"In Analysis,Click on In Analysis Button,Successful,{url_h}\n",
        new=False,
    )
    time.sleep(3)

    Cam_page41 = SendKeys(driver)
    Cam_page41.send_keys(InAnalaysisTabResource.search_cam, NAME_CAMPAIGN_EDIT_LIV)
    try:
        Cam_page41 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN_EDIT_LIV}']",
                )
            )
        )
        pop_nadm = driver.find_element(
            By.XPATH,
            f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN_EDIT_LIV}']",
        )

        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "IN Analysis Tab",{pop_nadm.text},{url_h}\n',
            new=False,
        )

    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "IN Analysis Tab",,{url_h}\n',
            new=False,
        )
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(5)

    # check campaign analysis completed after edit from live======

    Cam_Page42 = Click(driver)
    Cam_Page42.Click_button(AnalaysisTabResource.Analaysis_btn)
    make_csv(
        "Campaign Report.csv",
        f"Analysis Completed,Click on Analysis Button,Successful,{url_h}\n",
        new=False,
    )
    time.sleep(5)

    Cam_page43 = SendKeys(driver)
    Cam_page43.send_keys(AnalaysisTabResource.search_cam1, NAME_CAMPAIGN_EDIT_LIV)
    try:
        Cam_page43 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_EDIT_LIV}']")
            )
        )
        pop_nam18 = driver.find_element(
            By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_EDIT_LIV}']"
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Analysis Completed Tab",{pop_nam18.text},{url_h}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Created Campaign in "Analysis Completed Tab",,{url_h}\n',
            new=False,
        )
    time.sleep(3)

    #  live campaign from analysis completed with play pause button=====

    Cam_Page44 = Click(driver)
    Cam_Page44.Click_button(CamPlayPauseAnaResource.CamPlayPauseana_btn)
    time.sleep(1)
    Cam_Page45 = Click(driver)
    Cam_Page45.Click_button(CamPlayPauseAnaResource.CamPlayPauseana_btn1)
    make_csv(
        "Campaign Report.csv",
        f"Start Campaign,Campaign Live from Play Button from Analysis completed,Successful,{url_h}\n",
        new=False,
    )
    time.sleep(1)

    Cam_Page46 = Click(driver)
    Cam_Page46.Click_button(CreateCampaignModuleResource.live_btn)
    time.sleep(3)

    # search camapign in live after strat campaign fom play button====

    Cam_page47 = SendKeys(driver)
    Cam_page47.send_keys(SeachCamapignResource.search_cam_live, NAME_CAMPAIGN_EDIT_LIV)

    try:
        Cam_page47 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='campaignListingLive']/tbody/tr/td[2]/div/a/h6[@title='{NAME_CAMPAIGN_EDIT_LIV}']")
            )
        )
        pop_nam19 = driver.find_element(
            By.XPATH, f"//*[@id='campaignListingLive']/tbody/tr/td[2]/div/a/h6[@title='{NAME_CAMPAIGN_EDIT_LIV}']"
        )
        make_csv(
            "Campaign Report.csv",
            f'Search campaign,Search Created Campaign in "Live Tab",{pop_nam19.text},{url_h}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search campaign,Search Created Campaign in "Live Tab",,{url_h}\n',
            new=False,
        )

    # Assign Campaign campaign to user=====
    time.sleep(5)
    Cam_Page48 = Click(driver)
    Cam_Page48.Click_button(EditCamapaignResource.ed_live_1)
    time.sleep(2)

    Cam_Page49 = Click(driver)
    Cam_Page49.Click_button(EditCamapaignResource.ed_live_3)
    time.sleep(2)

    options_lists = get_selection_lists(
        driver, CreateCampaignModuleResource.Assign_user
    )
    time.sleep(2)

    user_name = driver.find_element(
        By.XPATH, f"//option[@value='{options_lists}']"
    ).text
    make_csv(
        "Campaign Report.csv",
        f"Assign Campaign,Assign camopaign To user(User Selected ),{user_name},{url_h}\n",
        new=False,
    )
    time.sleep(3)

    Cam_Page50 = Click(driver)
    Cam_Page50.Click_button(CreateCampaignModuleResource.assign_btn1)

    try:
        pop_name20 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "popUpMessage"))
        )

        make_csv(
            "Campaign Report.csv",
            f"Assign Campaign,Assign User to Campaign,{pop_name20.text},{url_h}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Assign Campaign,Assign User to Campaign,,{url_h}\n",
            new=False,
        )
    time.sleep(5)

    #  Logout from Current User====

    Cam_Page69 = Click(driver)
    Cam_Page69.Click_button(LogoutBtnResource.logout_1_2)
    time.sleep(1)
    Cam_Page70 = Click(driver)
    Cam_Page70.Click_button(LogoutBtnResource.logout_2_2)
    time.sleep(3)
    url_k = driver.current_url

    make_csv(
        "Campaign Report.csv",
        f"Logout,Log out from current User,Successful,{url_k}\n",
        new=False,
    )

    #  Login with that user to whom campaign is assigned
    try:
        login_page1 = LoginPage(driver)
        login_page1.enter_username(LoginResources.USERNAME, user_name)
        login_page1.enter_password(LoginResources.PASSWORD, PASS_WORD)
        success = login_page.click_login_btn(LoginResources.LOGIN_BTN)

        make_csv(
        "Campaign Report.csv",
        f"Login,Login with correct username & password to which campaign is assigned,Successful,{url_k}\n",
        new=False,
        )
        make_csv(
        "Campaign Report.csv",
        f"login Credentials,User Name:{user_name},Password:{PASS_WORD}\n",
        new=False,
        )
    except:
        login_page1 = LoginPage(driver)
        login_page1.enter_username(LoginResources.USERNAME, user_name)
        login_page1.enter_password(LoginResources.PASSWORD, pass_word_1)
        success = login_page.click_login_btn(LoginResources.LOGIN_BTN)

        make_csv(
        "Campaign Report.csv",
        f"Login,Login with correct username & password to which campaign is assigned,Successful,{url_k}\n",
        new=False,
        )
        make_csv(
        "Campaign Report.csv",
        f"login Credentials,User Name:{user_name},Password:{pass_word_1}\n",
        new=False,
        )
        
    Cam_Page103 = Click(driver)
    Cam_Page103.Click_button(AssignUserResource.campaign_btn)
    url_l = driver.current_url
    time.sleep(4)

    Cam_page104 = SendKeys(driver)
    Cam_page104.send_keys(AssignUserResource.live_search, NAME_CAMPAIGN_EDIT_LIV)
    try:
        Cam_page104 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='campaignListingLive']//*[@class='compaign-name']//*[@title='{NAME_CAMPAIGN_EDIT_LIV}']",
                )
            )
        )
        pop_nam356 = driver.find_element(
            By.XPATH,
            f"//*[@id='campaignListingLive']//*[@class='compaign-name']//*[@title='{NAME_CAMPAIGN_EDIT_LIV}']",
        )
        pop_name356 = driver.find_element(By.XPATH, f"//*[@id='campaignListingLive']//*[@class='compaign-name']//*[@title='{NAME_CAMPAIGN_EDIT_LIV}']").text
        make_csv(
            "Campaign Report.csv",
            f"Assigned Campaign,Search Campaign that assign to User by login this user,{pop_name356},{url_l}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Assigned Campaign,Search Campaign that assign to User by login this user,,{url_l}\n",
            new=False,
        )

    #  Logout from Current User====

    time.sleep(2)
    Cam_Page349 = Click(driver)
    Cam_Page349.Click_button(LogoutBtnResource.logout_1_2)
    time.sleep(1)
    Cam_Page167 = Click(driver)
    Cam_Page167.Click_button(LogoutBtnResource.logout_2_2)
    url_m = driver.current_url
    time.sleep(3)

    make_csv(
        "Campaign Report.csv",
        f"Logout,Log out from current User,Successful,{url_m}\n",
        new=False,
    )

    # again login with role id 2

    login_page2 = LoginPage(driver)
    login_page2.enter_username(LoginResources.USERNAME, USER_NAME)
    login_page2.enter_password(LoginResources.PASSWORD, PASS_WORD)
    success = login_page.click_login_btn(LoginResources.LOGIN_BTN)

    make_csv(
        "Campaign Report.csv",
        f"Login,Login with correct username & password,Successful,{url_m}\n",
        new=False,
    )

    # clcik on camapign button and go to live tab===

    Cam_Page101 = Click(driver)
    Cam_Page101.Click_button(CreateCampaignModuleResource.Campaign_btn)
    time.sleep(3)
    Cam_Page102 = Click(driver)
    Cam_Page102.Click_button(CreateCampaignModuleResource.live_btn)
    time.sleep(3)

    # Search campaign in live tab===

    Cam_page51 = SendKeys(driver)
    Cam_page51.send_keys(SeachCamapignResource.search_cam_live, NAME_CAMPAIGN_EDIT_LIV)
    Cam_page51 = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//*[@id='campaignListingLive']/tbody/tr/td[2]/div/a/h6[@title='{NAME_CAMPAIGN_EDIT_LIV}']")
        )
    )

    # Click on campaign view report from three dots====

    Cam_Page52 = Click(driver)
    Cam_Page52.Click_button(EditCamapaignResource.ed_live_1)
    time.sleep(1)

    Cam_Page53 = Click(driver)
    Cam_Page53.Click_button(EditCamapaignResource.ed_live_4)
    time.sleep(1)

    Cam_Page54 = Click(driver)
    Cam_Page54.Click_button(EditCamapaignResource.ed_cam_report)
    url_i = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Click on edit campaign From view report,Successful,{url_i}\n",
        new=False,
    )
    time.sleep(2)

    # Check campaign name validation and keywords to edit campaign===

    cam_nam12 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page55 = SendKeys(driver)
    Cam_page55.send_keys(CreateCampaignModuleResource.Cam_name_liv, "@##$%^&*()_+!")
    time.sleep(2)
    pop_nam21 = driver.find_element(By.XPATH, "//*[@id='warning-text-id-cam']").text
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Check Special Characters While Editing camp from live,{pop_nam21},{url_i}\n",
        new=False,
    )
    time.sleep(1)

    cam_nam12 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page56 = SendKeys(driver)
    Cam_page56.send_keys(
        CreateCampaignModuleResource.Cam_name_liv,
        "sdaffasdbkdfvgigouhfdoghodfhgodfhgfdhgdflhdflghldfhgldfghldfghldfhkldfhgldfghhldfkhgdflghldfkhggldfgf",
    )
    time.sleep(2)
    pop_nam22 = driver.find_element(By.XPATH, "//*[@id='warning-text-id-cam']")
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Check 100 Characters limitation  While Editing campaign from live,{pop_nam22.text},{url_i}\n",
        new=False,
    )
    time.sleep(1)

    cam_nam13 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page57 = SendKeys(driver)
    Cam_page57.send_keys(
        CreateCampaignModuleResource.Cam_name_liv, NAME_CAMPAIGN_EDIT_V_RE
    )
    time.sleep(2)
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Enter Correct Campaign Name,Successful,{url_i}\n",
        new=False,
    )
    time.sleep(3)

    driver.execute_script("window.scrollTo(0,700)")
    time.sleep(2)
    try:
        Cam_Page58 = Click(driver)
        Cam_Page58.Click_button(CreateCampaignModuleResource.liv_upd_btn)
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Click on Update Bussiness,Bussiness Updated Successfully!,{url_i}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Click on Update Bussiness,Bussiness Updated Successfully!,{url_i}\n",
            new=False,
        )
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".tagsinputfield").send_keys(Keys.BACKSPACE)
    time.sleep(1)
    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Remove Keyword while Editing Campaign from view report,Successful,{url_i}\n",
        new=False,
    )
    time.sleep(3)

    get_key_words(driver)

    make_csv(
        "Campaign Report.csv",
        f"Edit Campaign,Add key word while editing campaign from view report ,Successful,{url_i}\n",
        new=False,
    )
    time.sleep(3)

    Cam_Page60 = Click(driver)
    Cam_Page60.Click_button(CreateCampaignModuleResource.cam_re_btn)

    try:
        pop_name23 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "popUpMessage"))
        )
        time.sleep(1)
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Hit Resubmit for anaLysis after edit campaign from view report,{pop_name23.text},{url_i}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Edit Campaign,Hit Resubmit for anaLysis after edit campaign from view report,,{url_i}\n",
            new=False,
        )
    time.sleep(1)

    Cam_Page61 = Click(driver)
    Cam_Page61.Click_button(CreateCampaignModuleResource.Campaign_btn)
    url_j = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Campaign Moduel,Click on Campaign Button,Successful,{url_j}\n",
        new=False,
    )
    time.sleep(2)

    # Click on in analysis tab====

    Cam_Page62 = Click(driver)
    Cam_Page62.Click_button(InAnalaysisTabResource.In_Analaysis_btn)
    make_csv(
        "Campaign Report.csv",
        f"In Analysis,Click on In Analysis Button,Successful,{url_j}\n",
        new=False,
    )
    time.sleep(3)

    # Search campaign in analysis after edit from view report edit button=====

    Cam_page63 = SendKeys(driver)
    Cam_page63.send_keys(InAnalaysisTabResource.search_cam, NAME_CAMPAIGN_EDIT_V_RE)

    try:
        Cam_page63 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN_EDIT_V_RE}']"
                )
            )
        )
        pop_namdd = driver.find_element(
            By.XPATH,
            f"//*[@id='queriesSourceAnalysis']/tbody/tr/td[1]/div/h6[@title='{NAME_CAMPAIGN_EDIT_V_RE}']",
        )
        time.sleep(1)
        make_csv(
            "Campaign Report.csv",
            f'Campaign Moduel,Search Campaign in "IN Analysis Tab" after edit campaign from view report,{pop_namdd.text},{url_j}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Campaign Moduel,Search Campaign in "IN Analysis Tab" after edit campaign from view report,,{url_j}\n',
            new=False,
        )

    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(5)

    # Search camaoign analysis completed after edit from view report edit button=====

    Cam_Page64 = Click(driver)
    Cam_Page64.Click_button(AnalaysisTabResource.Analaysis_btn)
    make_csv(
        "Campaign Report.csv",
        f"Analysis Completed,Click on Analysis Button,Successful,{url_j}\n",
        new=False,
    )
    time.sleep(5)

    Cam_page65 = SendKeys(driver)
    Cam_page65.send_keys(AnalaysisTabResource.search_cam1, NAME_CAMPAIGN_EDIT_V_RE)

    try:
        Cam_page65 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_EDIT_V_RE}']")
            )
        )
        pop_nam25 = driver.find_element(
            By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_EDIT_V_RE}']"
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in "Analysis Completed Tab" after edit campaign from view report",{pop_nam25.text},{url_j}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in "Analysis Completed Tab" after edit campaign from view report",,{url_j}\n',
            new=False,
        )
    time.sleep(3)

    # Delete campaign from Analysis completed tab====

    Cam_Page66 = Click(driver)
    Cam_Page66.Click_button(AnalaysisTabResource.camp_edit_ana)
    time.sleep(1)
    Cam_Page67 = Click(driver)
    Cam_Page67.Click_button(AnalaysisTabResource.camp_edit_del)
    time.sleep(1)
    Cam_Page68 = Click(driver)
    Cam_Page68.Click_button(AnalaysisTabResource.camp_del_ok)

    try:
        pop_name26 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "popUpMessage"))
        )
        make_csv(
            "Campaign Report.csv",
            f"Delete Campaign,Delete Campaign from Analysis Completed,{pop_name26.text},{url_j}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Delete Campaign,Delete Campaign from Analysis Completed,,{url_j}\n",
            new=False,
        )

    #  Logout from Current User====

    time.sleep(2)
    Cam_Page69 = Click(driver)
    Cam_Page69.Click_button(LogoutBtnResource.logout_1_2)
    time.sleep(1)
    Cam_Page70 = Click(driver)
    Cam_Page70.Click_button(LogoutBtnResource.logout_2_2)
    time.sleep(3)
    url_q = driver.current_url

    make_csv(
        "Campaign Report.csv",
        f"Delete Campaign,Log out from current User,Successful,{url_q}\n",
        new=False,
    )

    make_csv(
        "Campaign Report.csv",
        f"login Credentials,User Name:{USER_NAME},Password:{PASS_WORD}\n",
        new=False,
    )

    # login with Role id 4==

    login_page3 = LoginPage(driver)
    login_page3.enter_username(LoginResources.USERNAME, USER_NAME_4)
    login_page3.enter_password(LoginResources.PASSWORD, PASS_WORD)
    url_r = driver.current_url
    login_page3.click_login_btn(LoginResources.LOGIN_BTN)

    make_csv(
        "Campaign Report.csv",
        f"Login,Login with correct username & password,Successful,{url_r}\n",
        new=False,
    )

    # Click on campaign button==

    time.sleep(2)
    Cam_Page600 = Click(driver)
    Cam_Page600.Click_button(RoleIdResources.campaign_btn)
    url_s = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Campaign Module,Click on Campaign Button,Successful,{url_s}\n",
        new=False,
    )

    # click on create campaign button ==
    time.sleep(2)
    Cam_Page601 = Click(driver)
    Cam_Page601.Click_button(RoleIdResources.create_campaign)
    url_t = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Campaign Module,Click on Create Campaign Button,Successful,{url_t}\n",
        new=False,
    )
    time.sleep(2)

    # Select Client=

    options_listss = get_selection_listss(
        driver, CreateCampaignModuleResource.Select_client_btn
    )
    # option = (options_listss).text

    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Select Client while creating campaign,Successful,{url_t}\n",
        new=False,
    )

    # CHeck Speacial Chracter and 100 Chracter limitation While creating Campaign==
    time.sleep(1)
    Cam_page602 = SendKeys(driver)
    Cam_page602.send_keys(RoleIdResources.campaign_name, "@##$$&^%$$@#%$^%&*^%$#%^")
    pop_602 = driver.find_element(
        By.XPATH, "//*[@class='my-3 text-danger warning-text']"
    ).text
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Check Special Characters while Create Campaign,{pop_602},{url_t}\n",
        new=False,
    )

    time.sleep(1)
    campagn_name602 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page603 = SendKeys(driver)
    Cam_page603.send_keys(
        RoleIdResources.campaign_name,
        "lhdgvaklvbdlkhvbdlkvhlkhvbksdhvbkdhvbsdlvklhdgvaklvbdlkhvbdlkvhlkhvbksdhvbkdhvbsdlvklhdgvaklvbdlkhvbdlkvhlkhvbksdhvbkdhvbsdlvklhdgvaklvbdlkhvbdlkvhlkhvbksdhvbkdhvbsdlvklhdgvaklvbdlkhvbdlkvhlkhvbksdhvbkdhvbsdlvk",
    )
    pop_603 = driver.find_element(
        By.XPATH, "//*[@class='my-3 text-danger warning-text']"
    ).text
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Check 100 Characters limitation while Create Campaign,{pop_603},{url_t}\n",
        new=False,
    )

    time.sleep(1)
    campagn_name603 = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()
    time.sleep(1)

    Cam_page604 = SendKeys(driver)
    Cam_page604.send_keys(RoleIdResources.campaign_name, NAME_CAMPAIGN_4)

    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Enter Correct Campaign Name while Create Campaign,Successful,{url_t}\n",
        new=False,
    )

    time.sleep(1)
    Cam_page605 = SendKeys(driver)
    Cam_page605.send_keys(RoleIdResources.gmb_cid, "275091129056086617545")
    pop_605 = driver.find_element(
        By.XPATH, "//*[@class='mt-2 text-danger warning-text-create-camapaign-gmbcid']"
    ).text
    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Check GMB_CID limitation while Create Campaign,{pop_605},{url_t}\n",
        new=False,
    )

    time.sleep(1)
    Campagn_name605 = driver.find_element(By.XPATH, "//*[@id='autocomplete']").clear()
    time.sleep(1)

    Cam_page606 = SendKeys(driver)
    Cam_page606.send_keys(RoleIdResources.gmb_cid, GMB_CID_4)

    time.sleep(1)
    Cam_Page6066 = Click(driver)
    Cam_Page6066.Click_button(RoleIdResources.check_gmb_cid)

    try:
        Business_606 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[@class='alert alert-success alert-dismissible fade show']",
                )
            )
        )
        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Enter Correct GMB CID,{Business_606.text},{url_t}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Enter Correct GMB CID,Successful,{url_t}\n",
            new=False,
        )
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,2000)")

    try:
        keyword1 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, RoleIdResources.Bus_loc))
        )
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    except:
        driver.execute_script("window.scrollTo(0,20000)")

    time.sleep(3)

    get_key_wordsss(driver)

    make_csv(
        "Campaign Report.csv",
        f"Create Campaign,Add keywords while creating Campaign,Successful,{url_t}\n",
        new=False,
    )

    time.sleep(1)
    Cam_Page607 = Click(driver)
    Cam_Page607.Click_button(RoleIdResources.submit_cam)

    try:
        pop_name607 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "popUpMessage"))
        )
        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Click on Submit for Analysis after enter correct data in all fields,{pop_name607.text},{url_t}\n",
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f"Create Campaign,Click on Submit for Analysis after enter correct data in all fields,,{url_t}\n",
            new=False,
        )

    # Search campaign in analysis after Create Camapign From Role id4 =====

    # Click on in analysis tab====

    Cam_Page611 = Click(driver)
    Cam_Page611.Click_button(InAnalaysisTabResource.In_Analaysis_btn)
    url_u = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"In Analysis,Click on In Analysis Button,Successful,{url_u}\n",
        new=False,
    )
    time.sleep(5)
    Cam_page608 = SendKeys(driver)
    Cam_page608.send_keys(RoleIdResources.search_cam12, NAME_CAMPAIGN_4)
    try:
        Cam_page608 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[3]/div/div/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/h6",
                )
            )
        )
        pop_nam608 = driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/h6",
        )

        make_csv(
            "Campaign Report.csv",
            f'Campaign Moduel,Search Campaign in "IN Analysis Tab" after Create campaign from role id 4,{pop_nam608.text},{url_u}\n',
            new=False,
        )

    except:
        make_csv(
            "Campaign Report.csv",
            f'Campaign Moduel,Search Campaign in "IN Analysis Tab" after Create campaign from role id 4,,{url_u}\n',
            new=False,
        )
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    driver.refresh()
    time.sleep(5)

    # Search campaign analysis completed after after Create Camapign From Role id4 =====

    Cam_Page609 = Click(driver)
    Cam_Page609.Click_button(AnalaysisTabResource.Analaysis_btn)
    url_v = driver.current_url
    make_csv(
        "Campaign Report.csv",
        f"Analysis Completed,Click on Analysis Button,Successful,{url_v}\n",
        new=False,
    )
    time.sleep(5)

    Cam_page610 = SendKeys(driver)
    Cam_page610.send_keys(RoleIdResources.Ana_com, NAME_CAMPAIGN_4)

    try:
        Cam_page610 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_4}']")
            )
        )
        pop_nam610 = driver.find_element(
            By.XPATH, f"//*[@id='queriesDataCompleted']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_4}']"
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in "Analysis Completed Tab" after Create campaign from role id 4",{pop_nam610.text},{url_v}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in "Analysis Completed Tab" after Create campaign from role id 4",,{url_v}\n',
            new=False,
        )
    time.sleep(3)

    # send for approval campaign from ana completed role id 4

    Cam_Page612 = Click(driver)
    Cam_Page612.Click_button(RoleIdResources.ana_edit_1)
    time.sleep(1)

    Cam_Page612 = Click(driver)
    Cam_Page612.Click_button(RoleIdResources.sub_apr)
    url_w = driver.current_url

    make_csv(
        "Campaign Report.csv",
        f'Submit for approval,Submit campaign for approval from role id 4",Successful,{url_w}\n',
        new=False,
    )
    time.sleep(3)

    # Search Campaign in pending for approval

    Cam_Page613 = Click(driver)
    Cam_Page613.Click_button(RoleIdResources.campaign_btn)
    time.sleep(1)
    Cam_Page614 = Click(driver)
    Cam_Page614.Click_button(RoleIdResources.Pen_app)
    time.sleep(5)

    Cam_page615 = SendKeys(driver)
    Cam_page615.send_keys(RoleIdResources.Pen_app_s, NAME_CAMPAIGN_4)

    try:
        Cam_page615 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='queriesDataPending']/tbody/tr[1]/td[2]/div/h6[@title='{NAME_CAMPAIGN_4}']",
                )
            )
        )
        pop_nam615 = driver.find_element(
            By.XPATH,
            f"//*[@id='queriesDataPending']/tbody/tr[1]/td[2]/div/h6[@title='{NAME_CAMPAIGN_4}']",
        ).text
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in Pending for approval in role id 4",{pop_nam615},{url_w}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in Pending for approval in role id 4",,{url_w}\n',
            new=False,
        )
    time.sleep(3)

    #  Logout from Current User====

    time.sleep(2)
    Cam_Page616 = Click(driver)
    Cam_Page616.Click_button(LogoutBtnResource.logout_1_2)
    time.sleep(1)
    Cam_Page617 = Click(driver)
    Cam_Page617.Click_button(LogoutBtnResource.logout_2_2)
    time.sleep(3)
    url_x = driver.current_url

    make_csv(
        "Campaign Report.csv",
        f"Delete Campaign,Log out from current User,Successful,{url_x}\n",
        new=False,
    )

    make_csv(
        "Campaign Report.csv",
        f"login Credentials,User Name:{USER_NAME_4},Password:{PASS_WORD}\n",
        new=False,
    )

    # login with Role id 2==

    login_page3 = LoginPage(driver)
    login_page3.enter_username(LoginResources.USERNAME, USER_NAME)
    login_page3.enter_password(LoginResources.PASSWORD, PASS_WORD)
    url_y = driver.current_url
    login_page3.click_login_btn(LoginResources.LOGIN_BTN)

    make_csv(
        "Campaign Report.csv",
        f"Login,Login with correct username & password,Successful,{url_y}\n",
        new=False,
    )

    # Search Campaign in pending approval from role id 2

    time.sleep(2)
    Cam_Page618 = Click(driver)
    Cam_Page618.Click_button(RoleIdResources.Pen_app)
    url_z = driver.current_url

    time.sleep(4)
    Cam_page619 = SendKeys(driver)
    Cam_page619.send_keys(RoleIdResources.penn_app_s2, NAME_CAMPAIGN_4)

    try:
        Cam_page619 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='queriesDataPending']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_4}']",
                )
            )
        )
        pop_nam619 = driver.find_element(
            By.XPATH,
            f"//*[@id='queriesDataPending']/tbody/tr/td[2]/div/h6[@title='{NAME_CAMPAIGN_4}']",
        ).text
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in Pending for approval in role id 2",{pop_nam619},{url_z}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in Pending for approval in role id 2",,{url_z}\n',
            new=False,
        )
    time.sleep(3)

    Cam_Page620 = Click(driver)
    Cam_Page620.Click_button(RoleIdResources.apr_cam)
    time.sleep(2)

    Cam_Page621 = Click(driver)
    Cam_Page621.Click_button(RoleIdResources.apr_camp2)

    make_csv(
        "Campaign Report.csv",
        f"Approve Campaign,Approve campaign of role id 4 from role id 2,Successful,{url_z}\n",
        new=False,
    )

    # Search campaign in live after aprrove campaign=====
    time.sleep(1)
    Cam_Page622 = Click(driver)
    Cam_Page622.Click_button(RoleIdResources.liv_btn1)
    time.sleep(3)

    Cam_page623 = SendKeys(driver)
    Cam_page623.send_keys(RoleIdResources.live_searccccchh, NAME_CAMPAIGN_4)

    try:
        Cam_page623 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[@id='campaignListingLive']/tbody/tr/td[2]/div/a/h6[@title='{NAME_CAMPAIGN_4}']",
                )
            )
        )
        pop_nam623 = driver.find_element(
            By.XPATH,
            f"//*[@id='campaignListingLive']/tbody/tr/td[2]/div/a/h6[@title='{NAME_CAMPAIGN_4}']",
        )
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in "Live Tab" after Approve campaign from pending approval",{pop_nam623.text},{url_z}\n',
            new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
            f'Search Campaign,Search Campaign in "Live Tab" after Approve campaign from pending approval",,{url_z}\n',
            new=False,
        )
    time.sleep(5)

    # Delete campaign from live tab====

    # Cam_Page624 = Click(driver)
    # Cam_Page624.Click_button(RoleIdResources.del_cam)
    # time.sleep(3)
    # Cam_Page625 = Click(driver)
    # Cam_Page625.Click_button(RoleIdResources.del_cam1)
    # time.sleep(3)
    # Cam_Page626 = Click(driver)
    # Cam_Page626.Click_button(RoleIdResources.del_cam_ok1)

    try:
        pop_name626 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "popUpMessage"))
        )
        pop_nam626 = driver.find_element(By.ID, "popUpMessage").text
        make_csv(
            "Campaign Report.csv",
                f"Delete Campaign,Delete Campaign from Analysis Completed,{pop_nam626},{url_z}\n",
                new=False,
        )
    except:
        make_csv(
            "Campaign Report.csv",
                f"Delete Campaign,Delete Campaign from Analysis Completed,,{url_z}\n",
                new=False,
        )
    #  Logout from Current User====

    time.sleep(2)
    Cam_Page69 = Click(driver)
    Cam_Page69.Click_button(LogoutBtnResource.logout_1_2)
    time.sleep(1)
    Cam_Page70 = Click(driver)
    Cam_Page70.Click_button(LogoutBtnResource.logout_2_2)
    time.sleep(2)
    url_q = driver.current_url

    make_csv(
        "Campaign Report.csv",
            f"Delete Campaign,Log out from current User,Successful,{url_q}\n",
            new=False,
    )

    make_csv(
        "Campaign Report.csv",
            f"login Credentials,User Name:{USER_NAME},Password:{PASS_WORD}\n",
            new=False,
    )

    time.sleep(5)


if __name__ == "__main__":
    main()
