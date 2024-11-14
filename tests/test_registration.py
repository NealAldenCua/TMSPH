from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver') #put where you downloaded the driver.
driver.get("URL_of_the_registration_page")

#Navigate to Register Page
def navigate_to_register_page():
    driver.get("URL_of_the_registration_page") #
    assert "Register" in driver.title  # check if the page has the title. If it does not find it, then it maybe loading or have error.
    print("Navigated to the Register Page.")

#Valid Registration
def valid_registration():
    #Personal Information
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
    driver.find_element(By.ID, "phone").send_keys("09088175555")

    #business Information
    driver.find_element(By.ID, "business_name").send_keys("John Technologies")

    #select from the drop down
    dropdown_element = driver.find_element(By.ID, "your_dropdown_id")
    select = Select(dropdown_element)
    select.select_by_visible_text("Options")
    driver.find_element(By.ID, "address_line").send_keys("420 ABC St.Canton Hill")

    #checkboxes
    # Selecting a checkbox
    checkbox1 = driver.find_element(By.ID, "privacy_policy" )
    checkbox2 = driver.find_element(By.ID, "terms_conditions")

    # Check the first checkbox if it's not already selected
    if not checkbox1.is_selected():
        checkbox1.click()

    # Check the second checkbox if it's not already selected
    if not checkbox2.is_selected():
        checkbox2.click()

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)  # Wait for response
    assert "Dashboard" in driver.title  # Check dashboard access
    print("Successfully registered and navigated to the dashboard.")

# Step 3: Invalid Phone Number Format
def invalid_phone_number():
    #personal information
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
    driver.find_element(By.ID, "phone").send_keys("+6390881755556")

    # business Information
    driver.find_element(By.ID, "business_name").send_keys("John Technologies")

    # select from the drop down
    dropdown_element = driver.find_element(By.ID, "industry_type")
    select = Select(dropdown_element)
    select.select_by_visible_text("Options")
    driver.find_element(By.ID, "address_line").send_keys("420 ABC St.Canton Hill")

    # checkboxes
    # Selecting a checkbox
    checkbox1 = driver.find_element(By.ID, "privacy_policy")
    checkbox2 = driver.find_element(By.ID, "terms_conditions")

    # Check the first checkbox if it's not already selected
    if not checkbox1.is_selected():
        checkbox1.click()

    # Check the second checkbox if it's not already selected
    if not checkbox2.is_selected():
        checkbox2.click()

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    error_message = driver.find_element(By.ID, "error").text
    assert "Incorrect phone number format" in error_message
    print("Incorrect phone number format.")

#Invalid email and valid phone
def invalid_email_and_phone():
    #personal information
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("valid_user@@example.com")
    driver.find_element(By.ID, "phone").send_keys("09088175555")

    # business Information
    driver.find_element(By.ID, "business_name").send_keys("John Technologies")

    # select from the drop down
    dropdown_element = driver.find_element(By.ID, "industry_type")
    select = Select(dropdown_element)
    select.select_by_visible_text("Options")
    driver.find_element(By.ID, "address_line").send_keys("420 ABC St.Canton Hill")

    # checkboxes
    # Selecting a checkbox
    checkbox1 = driver.find_element(By.ID, "privacy_policy")
    checkbox2 = driver.find_element(By.ID, "terms_conditions")

    # Check the first checkbox if it's not already selected
    if not checkbox1.is_selected():
        checkbox1.click()

    # Check the second checkbox if it's not already selected
    if not checkbox2.is_selected():
        checkbox2.click()

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.ID, "error").text
    assert "Incorrect email and phone number format" in error_message
    print("Incorrect email and phone format.")

# Email and phone left empty
def empty_email_and_phone():
    #personal information
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("")
    driver.find_element(By.ID, "phone").send_keys("")

    # business Information
    driver.find_element(By.ID, "business_name").send_keys("John Technologies")

    # select from the drop down
    dropdown_element = driver.find_element(By.ID, "industry_type")
    select = Select(dropdown_element)
    select.select_by_visible_text("Options")
    driver.find_element(By.ID, "address_line").send_keys("420 ABC St.Canton Hill")

    # checkboxes
    # Selecting a checkbox
    checkbox1 = driver.find_element(By.ID, "privacy_policy")
    checkbox2 = driver.find_element(By.ID, "terms_conditions")

    # Check the first checkbox if it's not already selected
    if not checkbox1.is_selected():
        checkbox1.click()

    # Check the second checkbox if it's not already selected
    if not checkbox2.is_selected():
        checkbox2.click()

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.ID, "error").text
    assert "Email and Phone number fields cannot be empty." in error_message
    print("Email and Phone number fields cannot be empty.")

# Special characters on Email and phone fields
def special_characters():
    #personal information
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("!@#user@#$%^")
    driver.find_element(By.ID, "phone").send_keys("!@#user@#$%^")

    # business Information
    driver.find_element(By.ID, "business_name").send_keys("John Technologies")

    # select from the drop down
    dropdown_element = driver.find_element(By.ID, "industry_type")
    select = Select(dropdown_element)
    select.select_by_visible_text("Options")
    driver.find_element(By.ID, "address_line").send_keys("420 ABC St.Canton Hill")

    # checkboxes
    # Selecting a checkbox
    checkbox1 = driver.find_element(By.ID, "privacy_policy")
    checkbox2 = driver.find_element(By.ID, "terms_conditions")

    # Check the first checkbox if it's not already selected
    if not checkbox1.is_selected():
        checkbox1.click()

    # Check the second checkbox if it's not already selected
    if not checkbox2.is_selected():
        checkbox2.click()

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.ID, "error").text
    assert "Email and Phone number fields are invalid." in error_message
    print("Email and Phone number fields are invalid.")

def notchecked_checkbox():
    #personal information
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("valid_user@example.com")
    driver.find_element(By.ID, "phone").send_keys("09088175555")

    # business Information
    driver.find_element(By.ID, "business_name").send_keys("John Technologies")

    # select from the drop down
    dropdown_element = driver.find_element(By.ID, "industry_type")
    select = Select(dropdown_element)
    select.select_by_visible_text("Options")
    driver.find_element(By.ID, "address_line").send_keys("420 ABC St.Canton Hill")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.ID, "error").text
    assert "privacy policy and terms & conditions must be checked." in error_message
    print("privacy policy and terms & conditions must be checked.")

# Run Tests Sequentially
try:
    navigate_to_register_page()
    valid_registration()
    invalid_phone_number()
    invalid_email_and_phone()
    empty_email_and_phone()
    special_characters()
    notchecked_checkbox()
finally:
    driver.quit()  # Ensure the browser closes after tests
