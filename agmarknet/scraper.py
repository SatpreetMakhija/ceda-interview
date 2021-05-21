from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
import time
import csv

def main():
    driver_path = '../chromedriver'
    driver = webdriver.Chrome(driver_path)

    websiteLink = 'https://agmarknet.gov.in/'
    driver.get(websiteLink)

    scrapeData(driver)

    time.sleep(20)
    driver.quit()

def scrapeData(driver):

    startDate = "10-May-2021"
    endDate = "16-May-2021"
    numberOfCommodities = len(driver.find_elements_by_xpath('/html/body/form/div[3]/div[6]/div[1]/div/div[2]/label/select/option'))
    print(numberOfCommodities)

    #select Price/Arrival
    arrival = Select(driver.find_element_by_id('ddlArrivalPrice'))
    arrival.select_by_visible_text('Arrival')
   
    ##loop to select the commodity
    commodity = Select(driver.find_element_by_id('ddlCommodity'))
    commodity.select_by_visible_text('Raddish')

    ##Select state
    selectState = Select(driver.find_element_by_id('ddlState'))
    selectState.select_by_visible_text('NCT of Delhi')

    # startDatePicker = driver.find_element_by_xpath('//*[@id="txtDate"]')
    # startDatePicker.send_keys(startDate)





    ##select date
    try: 
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtDate")))
    finally:
        startDatePicker = driver.find_element_by_xpath('//*[@id="txtDate"]')
        startDatePicker.send_keys(startDate)
        
        
    try: 
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtDateTo")))
    finally:
        endDatePicker = driver.find_element_by_xpath('//*[@id="txtDateTo"]')
        endDatePicker.send_keys(endDate)

    ##click on Go button
    # goButton = driver.find_element_by_id("btnGo")
    # goButton.click()
   
   
    


    return 
main()