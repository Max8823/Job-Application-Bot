import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from LoginHandler import LoginHandler
from SettingsManager import SettingsManager


def initialize_webdriver():

    options = Options()

    # Specify the location of the Chrome binary
    options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    # Specify the location of the Chrome profile
    options.add_argument("user-data-dir=C:\\Users\\user\\ChromeProfile")
    options.add_argument("--profile-directory=Profile 3")

    # Add stability and stealth options
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Initialize WebDriver
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver-win64", "chromedriver.exe")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    return driver

if __name__ == "__main__":

    # Initialize settings manager and load settings
    settings_manager = SettingsManager("settings.yaml")
    settings_manager.load_settings()
    print("Settings loaded successfully.")

    driver = initialize_webdriver()


    try:

        login_handler = LoginHandler(settings_manager)

        #TODO implement process for all sites listed.

        # Perform login for a specific site
        site_url = "https://seek.com.au/"

        login_success = login_handler.login(driver, site_url)

        if login_success:
            print("Login process completed successfully.")
        else:
            print("Login process failed.")

    except Exception as e:
        print(f"An error occurred during the login process: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()


