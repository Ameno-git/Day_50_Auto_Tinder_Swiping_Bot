from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

URL = "https://tinder.com/"
LOGIN = "FACEBOOK LOGIN TEST"
PASSWORD = "FACEBOOK PASS 2Q"
CODE = "code from code gen"

driver = webdriver.Chrome(executable_path="D:\pythonProject\othersoft\chromedriver.exe")

driver.get(URL)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="o1286841894"]/div/div[2]/div/div/div[1]/button').click()
time.sleep(1)
driver.find_element_by_css_selector("a.button").click()
time.sleep(1)

# check if no facebook button
try:
    driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
except NoSuchElementException:
    driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(2)

# switch to login window and login with dualauth
main_window = driver.window_handles[0]
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(LOGIN)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(4)
code = driver.find_element_by_xpath('//*[@id="approvals_code"]')
code.send_keys(CODE)
code.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]').click()
time.sleep(2)

# switch window and accept/deny pop up notifications
driver.switch_to.window(main_window)
print(driver.title)
driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div/div/div[3]/button[2]').click()

# autolike
for i in range(20):
    time.sleep(2)
    try:
        driver.find_element_by_xpath(
            '//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button').click()
    except ElementClickInterceptedException:
        try:
            #todo find element if much
            print("mutch?")
            time.sleep(1)
            driver.find_element_by_link_text("BACK TO TINDER")

            time.sleep(2)
            driver.find_element_by_xpath(
                '//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button').click()
        except NoSuchElementException:
            print("pop up")
            driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[2]/button[2]').click()
            time.sleep(2)
            driver.find_element_by_xpath(
                '//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button').click()
