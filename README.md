# TMSPH

**Overview**

This Python script automates the registration form testing for a web application. It interacts with the form's fields, submits data, checks for valid and invalid responses, and verifies that the expected behavior occurs in each case. The script ensures that the registration page works correctly for various scenarios.
- Valid inputs lead to a successful registration.
- Invalid inputs trigger proper error messages.
- Required fields are not left empty.
- Specific behaviors (like checkbox selection) are properly enforced.


**Thought Process & Design**

Purpose of the Script

The main goal of this script is to ensure that the registration page of the web application is functioning correctly under various conditions.

- Modular Test Cases: Each test case is encapsulated in a function, making it easy to understand and extend.
- Use of Selenium WebDriver: Selenium is used for interacting with the web page, filling out fields, clicking buttons, and verifying results.
- Assertions: Assertions are used to check the expected outcome of each test case (e.g., error messages, page redirections).
- Delays: time.sleep() is used to simulate real-time user behavior and ensure that the page has time to load or show error messages.
 
**Test Case Scenarios**
1. Valid Registration
 - Description: Ensures that when valid information is entered (first name, last name, email, phone number, etc.), the form submits successfully, and the user is redirected to the dashboard.
 - Expected Result: The user should be directed to the "Dashboard" page.
  
2. Invalid Phone Number Format
 - Description: Provide an incorrect phone number format (e.g., with extra digits or country code). 
 - Expected Result: The system should see an error message indicating the phone number format is incorrect.

3. Invalid Email Format
 - Description: Invalid email format (e.g., missing "@" symbol or invalid characters). 
 - Expected Result: The system should display an error message indicating the email format is incorrect.
   
4. Empty Email and Phone Fields
 - Description: Ensures that the email and phone fields cannot be left empty, and should trigger a validation error.
 - Expected Result: The system should display an error message indicating the Email and Phone number fields cannot be empty.
   
5. Special Characters in Email and Phone Fields
 - Description: Entering special characters like "!@#" in both email and phone fields.
 - Expected Result: The form should not accept special characters, and an error message should appear indicating "Invalid characters in email or phone."
   
6. Unchecked Privacy Policy and Terms & Conditions
 - Description: Ensures that the user cannot submit the form unless both the "Privacy Policy" and "Terms & Conditions" checkboxes are selected.
 - Expected Result: An error message should appear indicating that the checkboxes need to be selected before proceeding.

Tools Used: 

**Selenium WebDriver:** Automates the web browser for the test cases.

**ChromeDriver:** Required to run the script on Google Chrome. (You must have Chrome installed).

**Python:** The script is written in Python.

**Python Packages**: Ensure the following Python packages are installed:
- selenium: For automating the web browser.
- time: For adding delays to simulate real-time actions.


**Installation**
1. install Python if you haven't yet. https://www.python.org/downloads/
2. Install Selenium via pip: pip install selenium
3. Download ChromeDriver and extract it to a folder on your computer. https://developer.chrome.com/docs/chromedriver/downloads
4. Update the executable_path in the script to point to the downloaded chromedriver.exe


**Running the Script**

1. Clone or Download the Script:

   - Clone this repository or download the script file.
     
2. Prepare the Script:

   - Make sure you have the ChromeDriver installed and update the executable_path in the script to point to the location of chromedriver.exe.

3. Run the Script:

   - Open a terminal and navigate to the directory where the script is located.
   - Execute the script by running: python registration_test_script.py
   - The script will open a Chrome browser, run the tests sequentially, and output results in the terminal.
