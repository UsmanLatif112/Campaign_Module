class LoginResources:
    USERNAME = "//*[@id='name']"
    PASSWORD = "//*[@id='password']"
    LOGIN_BTN = "//*[@id='submitSigninLogin']"


class CreateCampaignModuleResource:
    Campaign_btn = "//*[@id='campaignbuttonfordisablenavbar']"
    Create_Campaign = "//*[@class='createusercamapignid-1']"
    # Select_client_btn = "//*[@id='select2-selectClient-container']"
    Select_client_btn = "//select[@name='client']"
    Enter_campaign_name = "//*[@id='campaign']"
    copy_Camp_name_popup = "//*[@class='my-3 text-danger warning-text']"
    Enter_GMB_Cid = "//*[@id='autocomplete']"
    Check_GMB_CID = "//*[@id='business_check']"
    copy_GMB_popup = (
        "//*[@class='mt-2 text-danger warning-text-create-camapaign-gmbcid']"
    )
    Hit_Submit_Analysis = "//*[@id='btnSubmit']"
    update_Bussiness = "//*[@id='submit-analysis']"
    Edit_camapaign = "//*[@id='campaignbtnresubmit']"
    keyword_list = "//*[@class='potential-keyword-list']"
    Keyword_Box = "//*[@class='bootstrap-tagsinput']"
    live_btn = "//*[@id='campaign-tab02']"
    Cam_name_liv = "//*[@id='campaign']"
    liv_upd_btn = "//*[@id='submit-analysis']"
    key_ad_liv = "//*[@id='campaign_form_id_resubmit']/div[5]/div/div[2]/ul/li[5]/a"
    cam_re_btn = "//*[@id='campaignbtnresubmit']"
    Assign_user = "//select[@name='agent_id']"
    assign_btn1 = "//*[@id='assign-employee-button']"
    bussiness_loct = "//*[@id='business-location']"


class KeywordsResource:
    keyword_1 = "//*[@id='salons']"
    keyword_2 = "//*[@id='open']"
    keyword_3 = "//*[@id='barber']"


class InAnalaysisTabResource:
    In_Analaysis_btn = "//*[@id='campaign-tab01']"
    search_cam = (
        "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div[2]/label/div/div/input"
    )
    copy_cam_name = (
        "/html/body/div[3]/div/div/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/h6"
    )


class AnalaysisTabResource:
    Analaysis_btn = "//*[@id='campaign-tab03']"
    search_cam1 = (
        "/html/body/div[3]/div/div/div/div[3]/div[3]/div/div[2]/label/div/div/input"
    )
    copy_cam_name1 = (
        "/html/body/div[3]/div/div/div/div[3]/div[3]/div/table/tbody/tr/td[2]/div/h6"
    )
    camp_edit_ana = "/html/body/div[3]/div/div/div/div[3]/div[3]/div/table/tbody/tr/td[5]/div/div[1]"
    camp_edit_del = "//*[@id='delete-campaign-listing-button-live']"
    camp_del_ok = "//*[@id='delete-confirm-campaign-yes-button']"


class EditCamapaignResource:
    Edit_camapaign_btn1 = "/html/body/div[3]/div/div/div/div[3]/div[3]/div/table/tbody/tr/td[5]/div/div[1]"
    Edit_camapaign_btn2 = "/html/body/div[3]/div/div/div/div[3]/div[3]/div/table/tbody/tr/td[5]/div/div[2]/ul/li[3]/a"
    Remove_Keyword = (
        "//*[@id='campaign_form_id_resubmit']/div[5]/div/div[1]/div[1]/span/span"
    )
    add_keyword1 = "//*[@id='campaign_form_id_resubmit']/div[5]/div/div[2]/ul/li[8]/a"
    live_Camp_btn = "//*[@id='start-campaign-listing-button']"
    ed_live_1 = "//*[@id='campaignListingLive']/tbody/tr/td[8]/div/div[1]"
    ed_live_2 = "//*[@id='campaignListingLive']/tbody/tr/td[8]/div/div[2]/ul/li[3]/a"
    ed_live_2 = "//*[@id='campaignListingLive']/tbody/tr/td[8]/div/div[2]/ul/li[3]/a"
    ed_live_3 = "//*[@id='campaignListingLive']/tbody/tr/td[8]/div/div[2]/ul/li[2]/a"
    ed_live_4 = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[8]/div/div[2]/ul/li[4]/a"
    ed_cam_report = "//*[@id='campaign_btn']"


class SeachCamapignResource:
    search_cam_live = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/label/div/div/input"
    search_cam_inAna = (
        "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div[2]/label/div/div/input"
    )
    search_cam_Ana_ = (
        "/html/body/div[3]/div/div/div/div[3]/div[3]/div/div[2]/label/div/div/input"
    )
    search_cam_pen_apr = (
        "/html/body/div[3]/div/div/div/div[4]/div[2]/div/div[2]/label/div/div/input"
    )


class DeleteCamapigninANAResource:
    Delete_camapaign1 = "/html/body/div[3]/div/div/div/div[3]/div[3]/div/table/tbody/tr/td[5]/div/div[1]"
    Delete_camapaign2 = "/html/body/div[3]/div/div/div/div[3]/div[3]/div/table/tbody/tr/td[5]/div/div[2]/ul/li[4]/a"
    Delete_camapaign3 = "//*[@id='delete-confirm-campaign-yes-button']"


class DeleteCamapigninDELResource:
    Delete_camapaign1 = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[8]/div/div[1]"
    Delete_camapaign2 = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[8]/div/div[2]/ul/li[5]/a"
    Delete_camapaign3 = "//*[@id='delete-confirm-campaign-yes-button']"


class CamPlayPauseLiveResource:
    CamPlayPauseLive_btn = "//*[@class='checkbox1']"
    CamPlayPauseLive_btn1 = "//*[@id='button-1']"


class CamPlayPauseAnaResource:
    CamPlayPauseana_btn = "//*[@class='checkbox3']"
    CamPlayPauseana_btn1 = "//*[@id='button-3']"


class CamAssignResource:
    CamAssign_btn = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[8]/div/div[1]"
    CamAssign_btn1 = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[8]/div/div[2]/ul/li[2]/a"
    CamAssign_btn2 = "//*[@class='dd-select-field']"
    CamAssign_btn3 = "//*[@id='assign-employee-button']"


class LogoutBtnResource:
    logout_1_2 = "//*[@class='user-icon-default dropbtn']"
    logout_2_2 = "//*[@id='logoutbuttonfordisable']"


class AssignUserResource:

    campaign_btn = "//*[@id='campaignbuttonfordisablenavbar']"
    live_search = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/label/div/div/input"


class RoleIdResources:
    campaign_btn = "//*[@id='campaignbuttonfordisablenavbar']"
    create_campaign = "//*[@class='createusercamapignid-1']"
    client_nam = "//*[@id='select2-selectClient-container']"
    campaign_name = "//*[@id='campaign']"
    gmb_cid = "//*[@id='autocomplete']"
    check_gmb_cid = "//*[@id='business_check']"
    enter_keyword = "//*[@class='bootstrap-tagsinput']"
    submit_cam = "//*[@id='btnSubmit']"
    Bus_loc = "//*[@id='business-location']"
    Ana_com = (
        "/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/label/div/div/input"
    )
    ana_edit_1 = "//*[@id='queriesDataCompleted']/tbody/tr/td[5]/div"
    ana_edit_2 = "/html/body/div[3]/div/div/div/div[3]/div[2]/div/table/tbody/tr/td[5]/div/div[2]/ul/li[3]/a"
    sub_apr = "/html/body/div[3]/div/div/div/div[3]/div[2]/div/table/tbody/tr/td[5]/div/div[2]/ul/li[2]/a"
    Pen_app = "//*[@id='campaign-tab04']"
    Pen_app_s = (
        "/html/body/div[3]/div/div/div/div[4]/div[2]/div/div[2]/label/div/div/input"
    )

    penn_app_s2 = (
        "/html/body/div[3]/div/div/div/div[4]/div[3]/div/div[2]/label/div/div/input"
    )

    apr_cam = "/html/body/div[3]/div/div/div/div[4]/div[3]/div/table/tbody/tr/td[5]/div/div[1]"
    apr_camp2 = "/html/body/div[3]/div/div/div/div[4]/div[3]/div/table/tbody/tr/td[5]/div/div[2]/ul/li[2]/a"
    liv_btn1 = "//*[@id='campaign-tab02']"
    live_search2 = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/label/div/div/input"
    del_cam = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/table/tbody/tr/td[8]/div/div[1]"
    del_cam1 = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div/table/tbody/tr/td[8]/div/div[2]/ul/li[5]/a"
    del_cam_ok1 = "//*[@id='delete-confirm-campaign-yes-button']"
    search_cam12 = (
        "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div[2]/label/div/div/input"
    )
    live_searccccchh = "/html/body/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/label/div/div/input"
