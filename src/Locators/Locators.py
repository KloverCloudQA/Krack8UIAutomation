class Locator(object):
    # **************************************Login Page**************************************
    textbox_Email_xpath = "//input[@id='mat-input-0']"  # xpath
    textbox_Password_xpath = "//input[@id='mat-input-1']"  # xpath
    button_ToggleVisibility = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                              "4]/button "  # xpath
    button_SignI_xpath = "//span[normalize-space()='Sign In']"
    alert_LogInAuthenticationError = "//body[1]/kc-toastr[1]/div[1]/div[1]"
    user_profile_Icon_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/kc-toolbar-user/div"
    button_Logout_xpath = "//span[normalize-space()='LOGOUT']"

    Email_box = "//input[@id='mat-input-0']"  # xpath
    Email_box_test = "//input[@id='mat-inpu-0']"  # xpath
    Password_box = "//input[@id='mat-input-1']"  # xpath
    Toggle_Visibility_Button = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                               "4]/button "  # xpath
    Sign_In_button = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"

    LogIn_Authentication_Error = "//body[1]/kc-toastr[1]/div[1]/div[1]"

    # ************************************************** Dashboard page************************************
    button_dashboard_sidebar_xpath = "//span[contains(text(),'Dashboard')]"
    Namespace_button_from_SideBar = "//span[contains(text(),'Namespace')]"  # XPATH
    Dashboard_title = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/h1"

    # ************************************************ header frame **************************************************
    CreateNew_H = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/button[2]"  # XPATH
    CreateNew_H_test = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/buttn[2]"
    Namespace_H = "button[role='menuitem']"  # xpath
    NewApplication_H = "//span[contains(text(),'New Application')]"

    # ******************************Create Application page********************************

    button_webframework_springBoot_xpath = "//span[contains(text(),'Spring Boot')]"
    SpringBoot_Version_box = "//mat-select[@id='mat-select-1']"
    SpringBoot_Version_2_1_11 = "//span[contains(text(),'2.1.11')]"  # XPATH
    Java_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]"
    Java_Version_11 = "//span[contains(text(),'11')]"
    Java_Version_8 = "//span[contains(text(),'8')]"

    button_webframework_ExpressJS_xpath = "//span[contains(text(),'ExpressJS')]"
    ExpressJS = "//mat-tab-body/div[1]/div[1]/div[2]"
    Express_Js_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # Xpath
    ExpressJs_Version_4_17_1 = "//span[contains(text(),'4.17.1')]"

    button_webframework_Django_xpath = "//span[contains(text(),'Django')]"
    Python_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # XPATH
    Python_version_3_7_8 = "//span[contains(text(),'3.7.8')]"  # XPATH
    Python_version_3_6_11 = "//span[contains(text(),'3.6.11')]"  # XPATH
    Django_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"  # XPATH
    Django_Version_2_2_14 = "//span[contains(text(),'2.2.14')]"  # XPATH

    button__JavaScript_xpath = "//mat-tab-body/div[1]/div[1]/div[4]"
    DoNet_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]"
    DontNet_V_3_0 = "//span[contains(text(),'3.0')]"
    DotNet_V_2_2 = "//span[contains(text(),'2.2')]"
    DotNet_V_2_1 = "//span[contains(text(),'2.1')]"

    button_webframework_Laravel_xpath = "//span[contains(text(),'Laravel')]"
    Laravel_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"  # XPATH
    Laravel_version_6_0 = "//span[contains(text(),'6.0')]"
    Laravel_version_5_8 = "//span[contains(text(),'5.8')]"
    Laravel_version_5_7 = "//span[contains(text(),'5.7')]"
    Laravel_version_5_6 = "//span[contains(text(),'5.6')]"

    button_webframework_Dot_Net_xpath = "//span[normalize-space()='Dot Net']"

    # Golang
    button_webframework_Golang_xpath = "//mat-tab-body/div[1]/div[1]/div[6]/div[1]"
    Goecho_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"
    Goecho_V_4_1_14 = "//span[contains(text(),'4.1.14')]"

    Application_Name_bar_xpath = "//input[@id='mat-input-0']"
    dropdown_teamBar_application_creation_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-form/div/div/kc-horizontal-stepper/section/div[2]/div[2]/div[1]/mat-form-field[4]/div/div[1]"
    checkbox_Enable_Persistent_Volume_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'Enable Persistent Volume')]"
    checkbox_Enable_In_Memory_Volume_Non_Persistent_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'Enable In-Memory Volume(Non-Persistent)')]"
    textbox_In_Memory_Volume_Mount_Paths_Non_Persistent_xpath = "//input[@formcontrolname='inMemoryVolumeMountPath']"
    checkbox_Enable_Auto_Scaling_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'Enable Auto Scaling')]"
    checkbox_CPU_Threshold_application_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'CPU Threshold * (percentage)')]"
    checkbox_Enable_Basic_Auth_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'Enable Basic Auth for External Access Url')]"
    textbox_basic_auth_username_application_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-form/div/div/kc-horizontal-stepper/section/div[2]/mat-tab-group/div/mat-tab-body/div/div[2]/div/kc-application-resource-selection-form/div/form/div[7]/div/div/div[2]/div/div[1]/mat-form-field/div/div[1]/div[3]/input"
    textbox_basic_auth_password_application_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-form/div/div/kc-horizontal-stepper/section/div[2]/mat-tab-group/div/mat-tab-body/div/div[2]/div/kc-application-resource-selection-form/div/form/div[7]/div/div/div[2]/div/div[2]/mat-form-field/div/div[1]/div[3]/input"
    Next_button = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/div[3]/button[2]"

    Choose_Namespace_one = "//mat-tab-body/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/div[1]"
    Save_button_A = "//span[contains(text(),'Save')]"
    Create_Application = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/form/div[3]/button[2]"
    check_create_app = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]"
    check_app_status = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[5]/div[2]/div[1]/div[1]/p[2]"

    Overview_button = "//span[contains(text(),'Overview')]"
    PipelineConfig_button = "//span[contains(text(),'Pipeline Config')]"
    Resources_Config_button = "//span[contains(text(),'Resources Config')]"
    External_Endpoints_button = "//span[contains(text(),'External Endpoints')]"
    Environment_Variables_button = "//span[contains(text(),'Environment Variables')]"
    Secrets_button = "//span[contains(text(),'Secrets')]"
    Monitoring_button = "//span[contains(text(),'Monitoring')]"
    Logs_button = "//span[contains(text(),'Logs')]"

    wait_ToCreateApplication = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[2]/ul[1]/li[1]/div[1]/button[1]/span[1]/mat-icon[1]/*[1]"

    git_account_bar_xpath = "//mat-select[@id='mat-select-3']"
    choose_git_account = "//span[contains(text(),'rased')]"
    container_registry_bar_xpath = "//mat-select[@id='mat-select-4']"
    choose_container_registry = "//span[contains(text(),'Quay-rased')]"
    next_button_xpath = "//span[normalize-space()='Next']"
    choose_namespace_xpath = "//h3[normalize-space()='Dynamic']"
    save_button_xpath = "//span[contains(text(),'Save')]"
    create_application_button_xpath = "//button[@type='submit']"

    # ******************** For application create validation ***************************

    New_Git_Commit_Pushed_msg = "//body/div[2]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"
    Application_build_finished_successfully_msg = "//span[contains(text(),'Application build finished successfully!')]"

    # Repository already exists with 'test-laravel = "//span[contains(text(),"Repository already exists with 'test-laravel' name")]"
    Live_Pipeline_Logs = "//h5[contains(text(),'Live Pipeline Logs')]"

    # ****************************************From sidebar***********************************
    Applications = "//span[contains(text(),'Applications')]"
    find_Application_tolist = "//span[contains(text(),'101')]"
    # *******************************To deploy application*************************************
    # Deployment is now in pending. It will take a moment to start = "//span[contains(text(),'Deployment is now in pending. It will take a momen')]"
    # Now we are deploying your application. Please wait for a while. It may take upto 3 minutes = "//span[contains(text(),'Now we are deploying your application. Please wait')]"
    # Application Deployed! = "//body/div[3]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"
    # To_deploy = "//li[@id='6367295d806b560001d2dd50']//*[name()='svg']//*[name()='rect']"  # XPATH
    To_deploy = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/*[name()='svg'][1]"
    icon_application_build_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-details/div/div/kc-ci-cd-pipeline/div[1]/div/div[2]/div/div[1]/ul/li"
    button_application_build_info_xpath = "//span[contains(text(),'Info')]"
    button_build_application_pipeline_xpath = "(//span[contains(text(), 'Build')])[3]"
    Deploy_button = "//span[normalize-space()='Deploy']"
    Okay_button = "//span[contains(text(),'Okay')]"
    Deployment_Pending_msg = "//span[contains(text(),'Deployment is now in pending. It will take a momen')]"
    deployment_failed = "//span[contains(text(),'[Alert] Application deployment failed!')]"
    close = "// span[contains(text(), 'close')]"
    Deployment_Pending_time_msg = "//span[contains(text(),'Now we are deploying your application. Please wait')]"
    Application_Deployed = "//body/div[3]/div[1]/div[1]/snack-bar-container[1]/simple-snack-bar[1]"

    to_check_deploy = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/*[name()='svg'][1]"
    Deployed_success_status = "//p[contains(text(),'Success')]"
    Deployed_status = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-details/div/div/kc-ci-cd-pipeline/div[5]/div[2]/div[1]/div/p[2]"

    deployed_validation = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[3]/ul[1]/li[1]/div[1]/button[1]/span[1]/mat-icon[1]/*[name()='svg'][1]"

    # ********************************************** delete Application ********************************
    application_Settings_xpath = "(//span[contains(@class,'inline-block py-4 px-4')][normalize-space()='Settings'])[1]"
    application_Delete_button_xpath = "//span[contains(text(),'Delete')]"
    application_name_bar_xpath = "//input[@placeholder='Type here...']"
    Delete_permanently_button = "//span[contains(text(),'I understand this, Delete permanently')]"
    Application_Deleted_Success_msg = "//p[normalize-space()='Application Deleted Successfully']"
    DeleteApp_byIcon = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/kc-application-init[1]/div[1]/button[1]"

    #  for failed app
    Application_Initialization_failed = "//h5[contains(text(),'*** Application Initialization Failed ***')]"
    checkbox_application_build_trigger_mode_manual_xpath = "//div[@class='mat-radio-label-content' and contains(text(), 'Manual')]"
    # -------------------------------- affinity config----------------------------------------------------------
    button_affinity_config_application_xpath = "//span[normalize-space()='Affinity Config']"
    add_affinity_icon_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-details/div/div/kc-application-affinity-list/div/div/div/a"
    textbox_affinity_config_name_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-details/div/div/kc-affinity-form/div/form/div[1]/div/mat-form-field/div/div[1]/div[3]/input"
    Checkbox_Add_Required_Scheduler_Config_NodeAffinity_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-application-details/div/div/kc-affinity-form/div/form/div[1]/section[1]/div[2]/div[1]/div/mat-checkbox/label/div"

    # ******************************** Delete Cache *****************************************

    Cache_S = "(//span[@class='item-label'][normalize-space()='Cache'])[1]"
    Cache_Settings = "(//span[@class='inline-block py-3 pl-2'][normalize-space()='Settings'])[1]"
    Cache_Delete = "//span[contains(text(),'Delete')]"
    Cache_namebox_D = "//input[@placeholder='Type here...']"
    Cache_Deleted_Success_msg = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"

    Enable_Web_Client_P3_X_Redis = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-cache-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[6]/div[1]/div[1]/mat-checkbox[1]/label[1]/div[1]"

    # ******************************** namespace creation *************************
    Namespace_button = "//body/div[3]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]"  # XPATH

    NamespaceName_box = "input[placeholder='Namespace Name']"  # css selector
    # CPU_box = "//input[@class='ng-tns-c41-54 ng-pristine ng-valid ng-touched']"  # XPATH
    CPU_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[""1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[""1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[""1]"

    NamespaceButton = "button[role='menuitem']"
    Create_button_N = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-list[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]/span[1]"
    NamespaceName_bar = "input[placeholder='Namespace Name']"
    namespace_create_button = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/span[1]/span[1]"
    wait_toCreateNamespace = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-vpc-list/div/div[2]/div[2]/button[1]/span/div"
    check_crateMessage = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"

    # with organization

    Organization = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[2]/span[1]/div[1]"
    Organization_searchBar = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]"
    Choose_Default = "//span[contains(text(),'default')]"
    Choose_firstOrganization = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"

    CPU_bar = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Memory_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Volume_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Bandwidth_box = "//div[contains(text(),'Moderate')]"

    Team = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[3]/span[1]/div[1]"
    teamSearch_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]"
    Choose_TeamDefault = "//span[contains(text(),'default')]"
    Choose_firstTeam = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"

    # Namespace delete

    namespace_search_bar_xpath = "//input[@placeholder='Search']"
    NamespaceButton_sidebar = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav[1]/div[1]/kc-sidenav[1]/div[1]/div[2]/kc-sidenav-item[3]/a[1]/span[1]"
    Namespace_settings = "(//span[@class='inline-block py-3 pl-2'][normalize-space()='Settings'])[1]"
    deleteButton_namespace = "//span[contains(text(),'Delete')]"
    input_namespaceName = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/kc-delete-dialog[1]/div[1]/div[1]/div[1]/div[1]/input[1]"

    # Team_None = "//span[@class='mat-option-text'][normalize-space()='None']"

    # *******************************deploy application*************************************
    # deploy_icon_xpath = "//*[local-name()='path' and @fill="#4DBB7B" and contains(@d, "M24.9899 25.3455")]"
    deploy_icon_xpath = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/div[1]/kc-ci-cd-pipeline[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/*[name()='svg'][1]"
    deploy_button_xpath = "//span[normalize-space()='Deploy']"
    restart_button_xpath = "//span[normalize-space()='Restart']"
    okay_button_xpath = "//span[contains(text(),'Okay')]"
    wait_to_complete_deploy_xpath = "//div[@class='pipeline-live-log-job-item-container cursor-pointer focused']//button[@type='button']//mat-icon[@role='img']//*[name()='svg']"

    # *******************************user section*************************************
    create_user_icon_xpath = "//button[@class='ml-4 mat-focus-indicator mat-mini-fab mat-button-base mat-primary']"
    first_name_bar_xpath = "//input[@formcontrolname='firstName']"
    last_name_bar_xpath = "//input[@formcontrolname='lastName']"
    auth_type_listbox_xpath = "//mat-select[@formcontrolname='userRegistrationMethod']"
    email_input_bar_xpath = "//input[@formcontrolname='username']"
    create_admin_checkbox_xpath = "(//div[@class='mat-checkbox-inner-container'])[1]"
    provide_password_checkbox_xpath = "(//div[@class='mat-checkbox-inner-container'])[2]"
    password_input_bar_xpath = "/html/body/div[3]/div[2]/div/mat-dialog-container/kc-user-form/div/form/mat-dialog-content/mat-form-field[2]/div/div[1]/div[3]/input"
    password_confirmation_input_bar_xpath = "/html/body/div[3]/div[2]/div/mat-dialog-container/kc-user-form/div/form/mat-dialog-content/mat-form-field[3]/div/div[1]/div[3]/input"
    team_dropdown_button_xpath = "//div[@class='mat-select-value']/span/span[text()='default']"
    roles_dropdown_button_xpath = "/html/body/div[3]/div[2]/div/mat-dialog-container/kc-user-form/div/form/mat-dialog-content/mat-form-field[5]/div/div[1]/div[3]/mat-select/div/div[1]/span"
    create_button_user_xpath = "//span[text()='Create']"

    # *************************************** database ********************************
    button_create_new_database_xpath = "//span[@_ngcontent-nfa-c43 and text()='Create New']"
    database_framework_xpath = "//h3[contains(text(), 'Postgresql')]"
    button_relational_xpath = "//div[contains(text(),'RELATIONAL')]"
    # frameworks
    button_mysql_xpath = "//mat-tab-body//button[1]"
    button_mongodb_xpath = "//h3[contains(text(), 'Mongodb')]"
    button_postgresql_xpath = "//h3[contains(text(), 'Postgresql')]"
    header_select_namespace_xpath = "//span[normalize-space()='Select Namespace']"

    team_list_dropdown_xpath = "(//div[@class='mat-select-arrow-wrapper'])[1]"
    choose_team_from_list_xpath = "//span[normalize-space()='default']"
    choose_namespace_database_xpath = "//h3[@class='vpc__name' and text()='bigSpace']"
    textbox_database_server_name_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div[2]/div[2]/div/div[1]/mat-form-field/div/div[1]/div[3]/input"
    textbox_initial_admin_password_database_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div[2]/div[2]/div/div[2]/mat-form-field/div/div[1]/div[3]/input"
    textbox_confirm_password_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div[2]/div[2]/div/div[3]/mat-form-field/div/div[1]/div[3]/input"
    button_next_database_xpath = "//span[contains(text(),'Next')]"
    button_confirm_database_xpath = "//button[@class='confirm-btn mat-focus-indicator mat-raised-button mat-button-base mat-primary']//span[text()='Confirm']"
    button_database_status_xpath = "//span[contains(@class, 'status__btn')]"
    # webclient
    checkbox_Enable_Web_Client_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div[2]/div[4]/div[1]/div/mat-checkbox/label/span"
    textbox_web_client_username_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div[2]/div[6]/div[2]/div/mat-form-field[1]/div/div[1]/div[3]/input"
    textbox_web_client_password_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div[2]/div[6]/div[2]/div/mat-form-field[2]/div/div[1]/div[3]/input"
    # snapshot service
    checkbox_enable_snapshot_service_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'Enable Snapshot Service')]"
    Database_button = "//div[@class='cdk-overlay-container']//button[4]"
    wait_forfilter = "//span[contains(text(),'Select Database')]"
    MySQL_button = "//mat-tab-body//button[1]"

    Postgresql = "//h3[contains(text(),'Postgresql')]"
    Postgresql_Version_12_3_0 = "//span[contains(text(),'12.3.0')]"
    Web_Client_Email = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[5]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    Web_Client_Password = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[5]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/input[1]"

    Mongodb = "//h3[contains(text(),'Mongodb')]"

    defaultTeam_database = "//span[contains(text(),'default')]"
    firstTeam = "/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[1]/mat-option[3]/span[1]"

    namespace_first = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-form/div/div/kc-horizontal-stepper/section/div/form/div[3]/button[1]"
    database_ServerName = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    initial_AdminPassword = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/div[2]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    confirm_Password = "//*[@id='mat-input-2']"
    selectVersion_box = "//*[@id='mat-select-0']/div/div[2]"
    version_8_0_19 = "//span[contains(text(),'8.0.19')]"

    next_button = "//span[normalize-space()='Next']"
    enableWebClient = "//label[@for='mat-checkbox-2-input']//div[@class='mat-checkbox-inner-container']"
    confirm_button = "//button[@type='submit']"

    Database_CreatedMsg = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"

    # created validation by snapshot button
    WaitTo_Create = "/html[1]/body[1]/kc-toastr[1]/div[1]/div[1]/div[2]/p[2]"
    # waitTo_create = "//h3[contains(text(),'Allocated Resources Per Instance')]"
    # validation
    Event_log = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-database-details[1]/kc-page-layout[1]/kc-page-layout-content[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/span[1]"
    Database_FinalStatus = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-details/kc-page-layout/kc-page-layout-content/div/kc-database-initialization/div/div[2]/div[2]/pre[10]"
    Cancel_msg = "//body/kc-toastr[1]/div[1]/div[1]/button[1]/i[1]"

    # *********************************** delete database **********************************

    database_list = "(//span[@class='item-label'][normalize-space()='Database'])[1]"
    database_name = "//span[normalize-space()='test-sql-221']"
    database_Settings_xpath = "(//span[@class='inline-block py-3 pl-2'][normalize-space()='Settings'])[1]"
    button_database_Delete_xpath = "//span[contains(text(),'Delete')]"
    textbox_database_name_xpath = "//input[@placeholder='Type here...']"
    button_delete_permanently_database_xpath = "//span[contains(text(),'I understand this, Delete permanently')]"
    # Application_Deleted_Success_msg = "//p[normalize-space()='Application Deleted Successfully']"
    # DeleteApp_byIcon = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-details[1]/div[1]/kc-application-init[1]/div[1]/button[1]"
    # restart
    button_restart_database_xpath = "//button[@class='btn btn-primary round w-32 mat-focus-indicator mat-button mat-button-base ng-trigger ng-trigger-fadeInRight']"
    button_okay_database_xpath = "//span[contains(text(),'Okay')]"
    button_database_settings_xpath = "//span[@class='inline-block py-3 pl-2' and contains(text(), 'Settings')]"
    text_manage_snapshot_database_xpath = "//h3[normalize-space()='Manage Snapshot']"
    button_edit_to_manage_snapshot_xpath = "(//button[@class='btn btn-accent round w-32 mat-focus-indicator mat-button mat-button-base ng-trigger ng-trigger-fadeInRight' and .//span[text()='Edit']])[2]"
    checkbox_to_enable_manage_snapshot_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-database-details/kc-page-layout/kc-page-layout-content/div/kc-database-settings/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/mat-checkbox/label/div"
    button_save_to_manage_snapshot_xpath = "//span[normalize-space()='Save']"
    button_close_to_manage_snapshot_xpath = "//span[normalize-space()='Close']"
    button_snapshot_from_header_xpath = "//span[normalize-space()='Snapshot']"
    button_take_snapshot_xpath = "//span[@class='ng-tns-c42-64' and text()='Take Snapshot']"
    checkbox_default_automated_scheduler_config_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'Default Automated Scheduler Config')]"
    # ************************************ create cache *********************************************
    cache_framework_redis_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-cache-form/div/div/kc-horizontal-stepper/section/div[2]/div[1]/button/span/div"
    dropdown_team_list_xpath = "(//div[@class='mat-select-arrow-wrapper'])[1]"
    button_namespace_cache_xpath = "//h3[@class='vpc__name' and text()='bigSpace']"
    textbox_cache_server_name_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-cache-form/div/div/kc-horizontal-stepper/section/div[2]/div[2]/div/mat-form-field[1]/div/div[1]/div[3]/input"
    textbox_initial_admin_password_cache_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-cache-form/div/div/kc-horizontal-stepper/section/div[2]/div[2]/div/mat-form-field[2]/div/div[1]/div[3]/input"
    textbox_confirm_password_cache_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-cache-form/div/div/kc-horizontal-stepper/section/div[2]/div[2]/div/mat-form-field[3]/div/div[1]/div[3]/input"
    dropdown_version_list_cache_xpath = "//div[@class='mat-select-value']"
    checkbox_add_storage_cache_xpath = "//span[@class='mat-checkbox-label' and contains(text(), 'Add Storage')]"
    checkbox_enable_web_client_cache_xpath = "//span[contains(@class, 'mat-checkbox-label') and contains(text(), 'Enable Web Client (P3 X Redis UI)')]"
    textbox_web_client_username_cache_xpath = "//input[contains(@class, 'mat-input-element') and @type='text' and @id='mat-input-4']"
    textbox_web_client_password_cache_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-cache-form/div/div/kc-horizontal-stepper/section/div[2]/div[5]/div[2]/div[2]/div/mat-form-field[2]/div/div[1]/div[3]/input"
    checkbox_enable_snapshot_service_cache_xpath = "//div[contains(@class, 'slider-row') and .//span[contains(@class, 'mat-checkbox-label') and contains(text(), 'Enable Snapshot Service')]]"
    button_next_cache_xpath = "//span[normalize-space()='Next']"
    button_confirm_cache_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-cache-form/div/div/kc-horizontal-stepper/section/div[2]/form/div[2]/button[1]/span/div/span"
    button_cache_status_xpath = "//span[contains(@class, 'status')]"
