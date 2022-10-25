import requests 
import packaging
import time

from bs4 import BeautifulSoup
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

	departureFrom=input('Wyjazd z:')	
	arrivalTo=input('Przyjazd do:')
	
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

	departureFrom_box = driver.find_element(By.ID,'departureFrom')
	departureFrom_box.send_keys(departureFrom)  

	arrivalTo_box = driver.find_element(By.ID,'arrivalTo')
	arrivalTo_box.send_keys(arrivalTo)

	driver.find_element(By.XPATH,"//button[@class='btn btn--lg btn-start-search txuc']").click()
	
enter()

def scrap():

	sleep(2)	

	curent_url = driver.current_url
	soup = BeautifulSoup(curent_url, 'html.parser')
	finder = soup.find('div', class_ ='search-results__item row abt-focusable')
	departure = finder.find_all('div', class_ ='col-5') 
	for item in departure:
		x = item.find('span')
		if x:
			print(x.text.strip())	

scrap()
