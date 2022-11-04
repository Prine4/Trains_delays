from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  

rejectCookiesXPATH = "//button[@class='btn cookieman-operation full-width--phone revoke-all-submit txuc']"
searchBtnXPATH = "//button[@class='btn btn--lg btn-start-search txuc']"
departureFromBottomID = "departureFrom"
arrivalToBottomID = "arrivalTo"
morePrzyXPATH = "//button[@class='search-results__item-show-changes btn btn--transparent txlc']"


def input_to_web():
     return 'Warszawa Wschodnia', 'Sopot Wyścigi'


def searching(url, webdriver_path):
    chrome_options = Options() #te linijki sprawiają ze ten kod działa na serwerze i żeby też na serwerze zadziałał to trzeba wyjebać linijkę 21 
    chrome_options.add_argument("--headless") 
    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.get(url)
    return chrome_driver


def enter(departure, arrival):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, rejectCookiesXPATH)))
    driver.find_element(By.XPATH, rejectCookiesXPATH).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, searchBtnXPATH)))
    driver.find_element(By.ID, departureFromBottomID).send_keys(departure)
    driver.find_element(By.ID, arrivalToBottomID).send_keys(arrival)
    driver.find_element(By.XPATH, searchBtnXPATH).click()


def scrap() -> List:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".stime.search-results__item-hour"))
    )

    # todo kod ponizej bedzie przydatny bla bla bla bla bla NIE USUWAC
    # for btn in driver.find_elements(By.XPATH, morePrzyXPATH): btn.click()

    times = driver.find_elements(By.CSS_SELECTOR, ".search-results__item-hour")
    
    result = []
    times_str = []

    for time in times:
        time_str = time.text.replace('\n', '')
        if time_str != '':
            times_str.append(time_str)

    for i in range(0, len(times_str)-1):
        result.append({'departure': times_str[i], 'arrival': times_str[i+1], 'reason': None})

    return result

departureFrom, arrivalTo = input_to_web()

driver = searching('https://www.portalpasazera.pl/', 'chromedriver_linux64/chromedriver')

enter(departureFrom, arrivalTo)

print(scrap())

driver.close()

