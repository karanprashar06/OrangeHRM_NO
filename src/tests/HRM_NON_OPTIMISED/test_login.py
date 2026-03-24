#password -f4kQ7wK@NG
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver


@allure.title("Verifying invalid login")
@allure.description("Verifying the login page with invalid credentials")
def test_login_invalid():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://testingkaran01-trials80.orangehrmlive.com/auth/login")
    assert "OrangeHRM" in driver.title


    element_username = driver.find_element(By.ID, "txtUsername")
    element_username.send_keys("wro")

    element_password = driver.find_element(By.ID, "txtPassword")
    element_password.send_keys("21233")

    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

    error_message = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='toast toast-error']")))
    print(error_message.text)

    assert "Invalid Credentials" in error_message.text

    driver.quit()

@allure.title("Verifying valid login")
@allure.description("Verifying the login page with valid credentials")
def test_login_valid():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get("https://testingkaran01-trials80.orangehrmlive.com/auth/login")
    assert "OrangeHRM" in driver.title


    element_username = driver.find_element(By.ID, "txtUsername")
    element_username.send_keys("admin")

    element_password = driver.find_element(By.ID, "txtPassword")
    element_password.send_keys("f4kQ7wK@NG")

    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

    confirm_message = wait.until(EC.visibility_of_element_located((By.XPATH,"//body")))
    print(confirm_message.text)

    assert "Employee Management" in confirm_message.text

    driver.quit()


@allure.title("Verifying add new user")
@allure.description("Verifying add new user")
def test_add_employee():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 30)

    driver.get("https://testingkaran01-trials80.orangehrmlive.com/auth/login")
    assert "OrangeHRM" in driver.title

    element_username = driver.find_element(By.ID, "txtUsername")
    element_username.send_keys("admin")

    element_password = driver.find_element(By.ID, "txtPassword")
    element_password.send_keys("f4kQ7wK@NG")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    element_employee_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Employee List']")))
    element_employee_list.click()
    driver.refresh()

    # Wait for Add button
    element_add_employee = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='addEmployeeButton'] i[class='material-icons']"))
    )

    # Scroll to element
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_add_employee)

    # Wait until clickable
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='addEmployeeButton'] i[class='material-icons']")))
    element_add_employee.click()


    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@ng-hide='usedForm.hideLabel']")))
    # Wait for upload section
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[contains(@id,'photo')]"))
    )

    # Locate hidden input
    file_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )

    # Make visible (if hidden)
    driver.execute_script("arguments[0].style.display='block';", file_input)

    # Upload
    file_input.send_keys(r"C:\Users\karan\OneDrive\Documents\KP.jpeg")

    element_first_name = driver.find_element(By.XPATH, "//input[@id='first-name-box']")
    element_first_name.send_keys("Akshay")
    element_last_name  = driver.find_element(By.XPATH, "//input[@id='last-name-box']")
    element_last_name.send_keys("Parashar")
    time.sleep(10)
    element_joining_date = driver.find_element(By.XPATH, "//input[@id='joinedDate']")
    element_joining_date.clear()
    element_joining_date.send_keys("2026-03-24")
    time.sleep(10)

    # Click dropdown
    element_location_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn']"))
    )
    element_location_dropdown.click()

    # Select option
    location_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='India Office']"))
    )
    location_option.click()

    element_next_button = driver.find_element(By.XPATH, "//button[@id='modal-save-button']")
    element_next_button.click()
    #time.sleep(10)

    #2ndpage-add employee

    wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@id='pimPersonalDetailsForm']")))

    element_adhaar_number = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='ssn']")))
    element_adhaar_number.send_keys("12345")
    element_DOB = driver.find_element(By.XPATH, "//input[@id='emp_birthday']")
    element_DOB.send_keys("1994-06-06")
    element_marital_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='emp_marital_status_inputfileddiv']")))
    element_marital_dropdown.click()
    marital_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Single']"))
    )
    marital_option.click()
    #select_gender
    element_gender_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='emp_gender_inputfileddiv']")))
    element_gender_dropdown.click()
    gender_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Male']")))
    gender_option.click()

    # select_nationality
    element_nationality_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='nation_code_inputfileddiv']")))
    element_nationality_dropdown.click()
    nationality_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Indian']")))
    nationality_option.click()

    element_next_button2 = driver.find_element(By.XPATH, "//button[normalize-space()='Next']")
    element_next_button2.click()



    time.sleep(10)

    driver.quit()
