from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import os
import time

while True:
    
    #Lendo RA do caboclo
    ra = int(input("Qual seria seu RA?\n"))

    #Parar programa se RA = 0
    if ra == 0:
        break
    
    #geckodriver_path = os.path.abspath("geckodriver")
    #Mostrar para a Kitty jeito mais bonitinho
    url = f"https://minhagrade-ufabc.up.railway.app/?ra={ra}"
    service = Service(executable_path="geckodriver")
    options = webdriver.FirefoxOptions()

    driver = webdriver.Firefox(service= service, options= options)
    
    driver.get(url)
    time.sleep(5)
    driver.quit()