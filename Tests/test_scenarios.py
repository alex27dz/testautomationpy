from General_functions import *


def test01_bmw_elements():
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to the BMW website
    driver.get("https://www.bmw.com")
    # driver.maximize_window()
    time.sleep(3)

    # Verify that the logo is displayed
    logo = driver.find_element(By.CSS_SELECTOR, "body > header > div > div > div > div > a > img")
    assert logo.is_displayed()

    # Close the browser
    driver.quit()


def test02_demoblaze_elements():
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to the Demoblaze website
    driver.get("https://www.demoblaze.com/")
    # driver.maximize_window()
    time.sleep(3)
    # Verify that the logo is displayed
    logo = driver.find_element(By.CSS_SELECTOR, "#navbarExample > ul")
    assert logo.is_displayed(), 'logo not found'

    # Verify that the search bar is displayed
    search_bar = driver.find_element(By.CSS_SELECTOR, "#itemc")
    assert search_bar.is_displayed(), 'search bar not found'

    # Verify that the footer is displayed
    footer = driver.find_element(By.CSS_SELECTOR, "#fotcont")
    assert footer.is_displayed(), ' footer not found'


def test03_google_search_bob():
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box
    search_box = driver.find_element_by_name("q")

    # Enter the search term "BOB"
    search_box.send_keys("BOB")

    # Submit the search form
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(3)

    # Verify that the results page contains the text "BOB"
    assert "BOB" in driver.page_source, 'BOB not found'

    # Close the browser
    driver.quit()


def test04_google_search_alex():
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box
    search_box = driver.find_element_by_name("q")

    # Enter the search term "Alex"
    search_box.send_keys("Alex")

    # Submit the search form
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(3)

    # Verify that the results page contains the text "Alex"
    assert "Alex" in driver.page_source, 'Alex not found'

    # Close the browser
    driver.quit()


def test05_google_maps_169():
    # Start the Chrome browser
    driver = webdriver.Chrome(chrome_location)

    # Navigate to Google Maps
    driver.get("https://www.google.com/maps")

    # Find the search box
    search_box = driver.find_element_by_name("q")

    # Enter the search term "169 fort york ontario"
    search_box.send_keys("169 fort york ontario")

    # Submit the search form
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)


    # Verify that the results page contains the text "169"
    assert "169" in driver.page_source, "address not located"

    # Close the browser
    driver.quit()




