# TMSPH

**Overview**

This Python script automates the registration form testing for a web application. It interacts with the form's fields, submits data, checks for valid and invalid responses, and verifies that the expected behavior occurs in each case. The script ensures that the registration page works correctly for various scenarios.


**Thought Process & Design**

Purpose of the Script

The main goal of this script is to ensure that the registration page of the web application is functioning correctly under various conditions.

- Modular Test Cases: Each test case is encapsulated in a function, making it easy to understand and extend.
- Use of Selenium WebDriver: Selenium is used for interacting with the web page, filling out fields, clicking buttons, and verifying results.
- Assertions: Assertions are used to check the expected outcome of each test case (e.g., error messages, page redirections).
- Delays: time.sleep() is used to simulate real-time user behavior and ensure that the page has time to load or show error messages.
 

Tools Used: 

**Selenium WebDriver:** Automates the web browser for the test cases.

**ChromeDriver:** Required to run the script on Google Chrome. (You must have Chrome installed).

**Python:** The script is written in Python.

**Python Packages**: Ensure the following Python packages are installed:
- selenium: For automating the web browser.
- time: For adding delays to simulate real-time actions.


**Running the Script**

1. Clone or Download the Script:

   - Clone this repository or download the script file.
     
2. Prepare the Script:

   - Make sure you have the ChromeDriver installed and update the executable_path in the script to point to the location of chromedriver.exe.

3. Run the Script:

   - Open a terminal and navigate to the directory where the script is located.
   - Execute the script by running: python registration_test_script.py
   - The script will open a Chrome browser, run the tests sequentially, and output results in the terminal.
