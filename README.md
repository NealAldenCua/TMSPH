# TMSPH-practical-exam

**Overview**

This Python script automates the registration form testing for a web application. It interacts with the form's fields, submits data, checks for valid and invalid responses, and verifies that the expected behavior occurs in each case. The script ensures that the registration page works correctly for various scenarios.


**Thought Process & Design**

Purpose of the Script

The main goal of this script is to ensure that the registration page of the web application is functioning correctly under various conditions.

Design:
- Modular Test Cases: Each test case is encapsulated in a function, making it easy to understand and extend.
- Use of Selenium WebDriver: Selenium is used for interacting with the web page, filling out fields, clicking buttons, and verifying results.
- Assertions: Assertions are used to check the expected outcome of each test case (e.g., error messages, page redirections).
- Delays: time.sleep() is used to simulate real-time user behavior and ensure that the page has time to load or show error messages.
