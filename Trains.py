import requests 
import selenium	
from selenium import webdriver 
from time import sleep 

def imput_to_web ():
	
	departureFrom=input('Wyjazd z:')	
	arrivalTo=input('Przyjazd do:')
	date=input('Podaj date wyjazdu:(format[##.##.####])')
	time=input('Podaj godzine wyjazdu:(format[##.##])')

	driver = 'muszę dać linię do tego' 
	driver.get('https://www.portalpasazera.pl/')
	print('Jestem w Poratlu pasażera')
	
	
imput_to_web()
