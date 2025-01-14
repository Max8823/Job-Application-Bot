from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginHandler:
    def __init__(self, settings_manager):
        self.settings_manager = settings_manager

#checking if the user is already logged in by checking if there is a signout or logout link
    def check_logged_in(self, driver):

        try:
            links = driver.find_elements(By.TAG_NAME, "a")

            for link in links:

                link_html = link.get_attribute("outerHTML").lower()
                if "logout" in link_html or "sign out" in link_html:
                    return True

        except Exception as e:
            print(f"Error while checking login status: {e}")
        return False


    def login(self, driver, site_url):

        try:
            # Navigate to the site
            driver.get(site_url)

            # Wait for the page to load
            WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

            # Check if already logged in
            if self.check_logged_in(driver):
                return True

        except Exception as e:
            print(f"An error occurred during login: {e}")


        print("Not logged in... attempting to log in...")

        # Find all anchor elements
        links = driver.find_elements(By.TAG_NAME, "a")

        #finding all possible signin / login links
        for link in links:
            try:
                link_html = link.get_attribute("outerHTML").lower()

                #checking if link could be used to sign in
                if "login" in link_html or "sign in" in link_html or "signin" in link_html:

                    # wait for the link to be clickable
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(link))
                    link.click()
                    print("Login link clicked.")
                    break

            except Exception as inner_exception:
                print(f"Error while interacting with link: {inner_exception}")

        #seek has some limited anti-bot measures this assists in bypassing do not remove
        sleep(2)

        if self.Check_GoogleForm(driver):
            return True
        else:
            ##TODO Implement manual login using details from Settings -- used for employer sites later
            return False


    # checks for and logs in using google form - works with most sites implementations
    def Check_GoogleForm(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))

        # Handle Google Login (if applicable)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:

            try:

                button_html = button.get_attribute("outerHTML").lower()

                if "google" in button_html or "continue with google" in button_html:
                    button.click()
                    self.GoogleLogin(driver)
                    return True

            except Exception as button_exception:
                print(f"Error while interacting with button: {button_exception}")

        print("Login process completed.")
        return False


    def GoogleLogin(self, driver):
        """Handle Google login workflow."""
        sleep(2)
        if self.check_logged_in(driver):
            return True

        print("Attempting Google Login...")

        # Retrieve login credentials from settings
        email = self.settings_manager.get_setting("google_email")
        password = self.settings_manager.get_setting("google_password")

      #checks if email already exists - clicks it
        try:
            email_selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@data-email='{email}']")))
            email_selector.click()

            # Wait for a confirmation element (e.g., profile or dashboard)
            ###TODO: this isnt needded on all sites for some reason - will not break code - it may hang for a shortwhile though
            continue_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue')]")))
            continue_button.click()
            return True

        # this will often trigger - won't break the program
        except Exception:
            print(f"Email selection for {email} not found. Proceeding with manual login.")
            if self.check_logged_in(driver):
                return True

        try:
            # Wait for the email input field and enter the email
            email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
            email_field.send_keys(email)

            # Click 'Next' button after entering email
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "identifierNext")))
            next_button.click()

            # Wait for the password input field and enter the password
            password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Passwd")))
            password_field.send_keys(password)

            # Click 'Next' button after entering password
            next_button_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "passwordNext")))
            next_button_password.click()

            # Waiting for the continue span
            ###TODO: this isnt needded on all sites for some reason - will not break code - it may hang for a shortwhile though
            continue_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue')]")))
            continue_button.click()
            print("Google login successful.")
            return True

        except Exception as e:
            print(f"An error occurred during Google login: {e}")
            return False

    def CheckGMail(self, driver):
        print("Checking GMail...")

