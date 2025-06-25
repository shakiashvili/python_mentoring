from selenium.webdriver.common.by import By


class Locators:
    # Locators for first test case

    careers_link = (By.XPATH, "//a[text()='Careers' and contains(@class,'js-op')]")
    keyword_field = (By.ID, 'new_form_job_search-keyword')
    cookies = (By.ID, "onetrust-accept-btn-handler")

    remote_option = (By.XPATH, "//*[@for[contains(., 'remote')]]")
    submit_button = (By.XPATH, "//button[@type='submit']")
    last_elemenet = (By.XPATH, "(//*[contains(@class,'item-apply-23')])[last()]")

    position_detail = (By.XPATH, "//h1[contains(@class,'vacancy-details')]")
    location_dropdown = (By.XPATH, "(//*[contains(@class,'select2-selection')])[1]")

    all_locations = (By.XPATH, "//*[contains(@class,'select2-results__option') and contains(text(),'All Locations')]")

    # Locators for second test case

    search_icon = (By.XPATH, "//span[contains(@class,'search-icon')]")
    search_keyword_field = (By.ID, "new_form_search")

    find_button = (By.XPATH, "//span[@class='bth-text-layer']")
    links = (By.XPATH, "//*[@class='search-results__title-link']")
