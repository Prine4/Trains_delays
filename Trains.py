import requests 
import packaging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep 

def imput_to_web():

	global departureFrom
	global arrivalTo
#	global date
#	global time

	departureFrom=input('Wyjazd z:')	
	arrivalTo=input('Przyjazd do:')
#	date=input('Podaj date wyjazdu:(format[##.##.####])')
#	time=input('Podaj godzine wyjazdu:(format[##:##])')
	

imput_to_web()

def serching():
	
	global driver

	driver = webdriver.Chrome(executable_path=r'/home/krzysztof/Desktop/Git/Trains_delays/master/chromedriver_linux64/chromedriver')
	driver.get('https://www.portalpasazera.pl/');
	print('Jestem w Poratlu pasażera')
	
serching()

def enter():
	
	global departureFrom
	global arrivalTo
#	global date
#	global time

	try:
		element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='k-widget k-window k-window--with-footer cookieman-window']")))
	finally:

		driver.find_element(By.XPATH,"//button[@class='btn cookieman-operation full-width--phone revoke-all-submit txuc']").click()

		departureFrom_box = driver.find_element(By.ID,'departureFrom')
		departureFrom_box.send_keys(departureFrom)  
			
		arrivalTo_box = driver.find_element(By.ID,'arrivalTo')
		arrivalTo_box.send_keys(arrivalTo)

#	date_box = driver.find_element(By.ID,'main-search__dateStart')	
#	date_box.send_keys(date_box)
#	sleep(1)
#
#	time_box = driver.find_element(By.ID,'main-search__timeStart')
#	time_box.send_keys(time_box)
#	sleep(1)

			
		driver.find_element(By.XPATH,"//button[@class='btn btn--lg btn-start-search txuc']").click()

	sleep(10)

enter()
