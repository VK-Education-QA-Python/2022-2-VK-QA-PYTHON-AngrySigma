from selenium.webdriver.common.by import By


class CampaignPageLocators:
    AUDIO_TYPE_CAMPAIGN_BUTTON = (By.XPATH,
                                  '//*[contains(@class, "column-list-item")'
                                  'and contains(@class, "audio")]')
    AD_URL_INPUT = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
    CAMPAIGN_NAME_INPUT = (By.XPATH,
                           '//div[contains(@class,'
                           '"campaign-name__name-wrap")]//descendant::input')
    CAMPAIGN_NAME_TILTE = (By.XPATH,
                           '//span[@data-translated="Campaign name"]')

    SEX_CHOICE = (By.XPATH,
                  '//li[@data-setting-name="sex"and @class="setting-item"]')
    SEX_CHOICE_OPENED = (By.XPATH,
                         '//li[@data-setting-name="sex"'
                         'and @class="setting-item setting-item_expanded"]')
    MALE_CHECKBOX = (By.XPATH, '//input[@type="checkbox" and @value="male"]')
    FEMALE_CHECKBOX = (By.XPATH,
                       '//input[@type="checkbox" and @value="female"]')

    AGE_CHOICE = (By.XPATH,
                  '//li[@data-setting-name="age" and @class="setting-item"]')
    AGE_CHOICE_OPENED = (By.XPATH,
                         '//li[@data-setting-name="age"'
                         'and @class="setting-item setting-item_expanded"]')
    AGE_SETTINGS = (By.XPATH,
                    '//div[contains(@class, "age-setting__select-wrap")]')
    CUSTOM_AGE_SETTING = (By.XPATH, '//li[@data-id="custom"]')
    AGE_SETTING_TEXT = (By.XPATH,
                        '//div[contains(@class, "age-setting__text")]'
                        '//descendant::textarea')

    SOC_DEM_CHOICE = (By.XPATH,
                      '//li[@data-setting-name="interests_soc_dem"'
                      'and @class="setting-item"]//child::div')
    SOC_DEM_CHOICE_OPENED = (By.XPATH,
                             '//li[@data-setting-name="interests_soc_dem"'
                             'and @class="setting-item '
                             'setting-item_expanded"]')
    SOC_DEM_TREE_BRANCH = (By.XPATH,
                           '//li[@data-setting-name="interests_soc_dem"]'
                           '//descendant::span'
                           '[@class="fast-tree-item__collapse-icon '
                           'js-toggle-collapse"]')
    SOC_DEM_TREE_ELEMENT = (By.XPATH,
                            '//li[@data-setting-name="interests_soc_dem"]//'
                            'descendant::input'
                            '[@class="fast-tree-item__input js-checkbox"]')

    INTERESTS_CHOICE = (By.XPATH,
                        '//li[@data-setting-name="interests"'
                        'and @class="setting-item"]')
    INTERESTS_CHOICE_OPENED = (By.XPATH,
                               '//li[@data-setting-name="interests"and'
                               '@class="setting-item setting-item_expanded"]')
    INTERESTS_TREE_BRANCH = (By.XPATH,
                             '//li[@data-setting-name="interests"]//'
                             'descendant::span'
                             '[@class="fast-tree-item__collapse-icon '
                             'js-toggle-collapse"]')
    INTERESTS_TREE_ELEMENT = (By.XPATH,
                              '//li[@data-setting-name="interests"]//'
                              'descendant::input'
                              '[@class="fast-tree-item__input js-checkbox"]')

    ADDITIONAL_TARGETING = (By.XPATH,
                            '//div[@data-name="additionalTargeting"]//'
                            'child::div'
                            '[@class="settings__group-head js-group-head"]')
    ADDITIONAL_TARGETING_OPENED = (By.XPATH,
                                   '//div[@data-name="additionalTargeting"]//'
                                   'child::div[@class="settings__group-head '
                                   'js-group-head _expanded"]')

    AGE_RESTRICTION_CHOICE = (By.XPATH,
                              '//li[@data-setting-name="age_restriction" '
                              'and @class="setting-item"]')
    AGE_RESTRICTION_CHOICE_OPENED = (By.XPATH,
                                     '//li'
                                     '[@data-setting-name="age_restriction"'
                                     ' and @class="setting-item '
                                     'setting-item_expanded"]')
    AGE_RESTRICTION_MENU = (By.XPATH, '//div[@data-test="select"]')
    AGE_RESTRICTION_AGE = {age: (By.XPATH, f'//li[@data-test="{age}"]')
                           for age in ['0+', '6+', '12+', '16+', '18+']}

    AB_TEST_CHOICE = (By.XPATH, '//li[@data-setting-name="split_audience" '
                                'and @class="setting-item"]')
    AB_TEST_CHOICE_OPENED = (By.XPATH,
                             '//li[@data-setting-name="split_audience" '
                             'and @class="setting-item '
                             'setting-item_expanded"]')
    AB_TEST_SEGMENT = {number: (By.XPATH, f'//input[@value="{number}"]//'
                                          f'parent::label[contains(@class, '
                                          f'"splitAudience-module-label")]')
                       for number in range(1, 11)}

    FULLTIME_CHOICE = (By.XPATH,
                       '//li[@data-setting-name="fulltime" '
                       'and @class="setting-item"]')
    FULLTIME_CHOICE_OPENED = (By.XPATH,
                              '//li[@data-setting-name="fulltime" and '
                              '@class="setting-item setting-item_expanded"]')
    FULLTIME_CHOICES = {time: (By.XPATH,
                               f'//li[@data-name="{time}"]') for time in
                        ['allDays', 'weekDays', 'weekends', 'workTime']}

    SHOWS_LIMIT_CHOICE = (By.XPATH,
                          '//li[@data-setting-name="uniq_shows_limit" '
                          'and @class="setting-item"]')
    SHOWS_LIMIT_CHOICE_OPENED = (By.XPATH,
                                 '//li[@data-setting-name="uniq_shows_limit" '
                                 'and @class="setting-item '
                                 'setting-item_expanded"]')
    SHOWS_LIMIT_USER = (By.XPATH, '//select[contains(@id, "period")]')
    SHOWS_LIMIT_USER_VALUES = {period: (By.XPATH,
                                        f'//select[contains(@id, "period")]//'
                                        f'child::option[@value="{period}"]')
                               for period in ['day', 'week', 'month']}
    SHOWS_LIMIT_CAMPAIGN = (By.XPATH, '//select[contains(@id, "show")]')
    SHOWS_LIMIT_CAMPAIGN_VALUES = {
        time: (By.XPATH, f'//select[contains(@id, "show")]//'
                         f'child::option[@value="{time}"]') for time in
        range(32)}
    SHOWS_LIMIT_AD = (By.XPATH, '//select[contains(@id, "ads")]')
    SHOWS_LIMIT_AD_VALUES = {
        time: (By.XPATH,
               f'//select[contains(@id, "ads")]//'
               f'child::option[@value="{time}"]')
        for time in
        range(32)}

    BUDGET_CHOICE = (By.XPATH,
                     '//li[@data-setting-name="budget_setting" '
                     'and @class="setting-item"]')
    BUDGET_CHOICE_OPENED = (By.XPATH,
                            '//li[@data-setting-name="budget_setting" and '
                            '@class="setting-item setting-item_expanded"]')
    BUDGET_PER_DAY_INPUT = (By.XPATH, '//input[@data-test="budget-per_day"]')
    BUDGET_TOTAL_INPUT = (By.XPATH, '//input[@data-test="budget-total"]')

    # GEO_CHOICE = (
    #     By.XPATH, '//li[@data-setting-name="geo" and @class="setting-item"]')
    # GEO_CHOICE_OPENED = (
    #     By.XPATH, '//li[@data-setting-name="geo" '
    #               'and @class="setting-item setting-item_expanded"]')

    # IMAGE_UPLOAD_BUTTON = (
    #     By.XPATH, '//div[contains(text(), "1000")]//'
    #               'parent::div[contains(@class,'
    #               '"roles-module-uploadButton")]')
    IMAGE_UPLOAD_BUTTON = (By.XPATH,
                           '//div[contains(@class, "upload-module-wrapper")]//'
                           'child::input[contains(@accept, "jpg") '
                           'and @data-test="overlay_500x500"]')
    # AUDIO_UPLOAD_BUTTON = (
    #     By.XPATH, '//div[contains(@class, "upload-module-wrapper")]//'
    #               'child::input[contains(@accept, "mp3")')
    AUDIO_UPLOAD_BUTTON = (By.XPATH,
                           '//div[contains(@class, "upload-module-wrapper") '
                           'and not(contains(@class, "hidden"))]//'
                           'child::input[contains(@accept, "mp3") '
                           'and not(@multiple)]')

    SUBMIT_BANNER_BUTTON = (By.XPATH,
                            '//div[@data-test="submit_banner_button"]')
    SUBMIT_CAMPAIGN_BUTTON = (By.XPATH,
                              '//div[contains(@class, "footer__button")]//'
                              'child::button')
