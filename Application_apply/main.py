from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def cancel_application():
    cancel = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    cancel.click()

    discard = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button")
    discard.click()


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3967126474&f_AL=true&keywords=python%20developer"
           "&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

driver.implicitly_wait(5)
sign_up = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_up.click()
driver.implicitly_wait(2)
username = driver.find_element(By.ID, "username")
username.send_keys("mr.cool.100daysofcode@gmail.com", Keys.ENTER)
driver.implicitly_wait(2)
password = driver.find_element(By.ID, "password")
password.send_keys("Rashu@123", Keys.ENTER)

list_applications = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list ul li")


for application in list_applications:
    print("Opening Listing")
    application.click()
    try:
        driver.implicitly_wait(2)
        apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
        apply.click()

        driver.implicitly_wait(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("8290266852")

        submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
        submit = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.text == "Next":
            cancel_application()
            print("long process")
            continue
        else:
            print("submitted")
            submit.click()
        driver.implicitly_wait(5)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application")
        driver.implicitly_wait(5)
        cancel_application()


driver.quit()
# save = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div["
#                                      "2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/button")
# save.click()
