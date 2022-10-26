from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rejectCookiesXPATH = "//button[@class='btn cookieman-operation full-width--phone revoke-all-submit txuc']"
searchBtnXPATH = "//button[@class='btn btn--lg btn-start-search txuc']"
departureFromBottomID = "departureFrom"
arrivalToBottomID = "arrivalTo"
morePrzyXPATH = "//button[@class='search-results__item-show-changes btn btn--transparent txlc']"


def input_to_web():
    return 'Warszawa Wschodnia', 'Gdynia Główna'


def searching(url, webdriver_path):
    chrome_driver = webdriver.Chrome(executable_path=webdriver_path)
    chrome_driver.get(url)
    return chrome_driver


def enter(departure, arrival):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, rejectCookiesXPATH)))
    driver.find_element(By.XPATH, rejectCookiesXPATH).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, searchBtnXPATH)))
    driver.find_element(By.ID, departureFromBottomID).send_keys(departure)
    driver.find_element(By.ID, arrivalToBottomID).send_keys(arrival)
    driver.find_element(By.XPATH, searchBtnXPATH).click()


def scrap():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".stime.search-results__item-hour"))
    )

    # todo kod ponizej bedzie przydatny bla bla bla bla bla NIE USUWAC
    # for btn in driver.find_elements(By.XPATH, morePrzyXPATH): btn.click()

    times = driver.find_elements(By.CSS_SELECTOR, ".search-results__item-hour")

    for i, t in enumerate(times):
        if i % 2 == 0:
            print('Odjazd: ', t.text)
        else:
            print('Przyjazd: ', t.text)


departureFrom, arrivalTo = input_to_web()

driver = searching('https://www.portalpasazera.pl/', 'chromedriver_linux64/chromedriver')

enter(departureFrom, arrivalTo)

scrap()

driver.close()
