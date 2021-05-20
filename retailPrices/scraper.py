from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time

def main():
    driver_path = '../chromedriver'
    driver = webdriver.Chrome(driver_path)

    websiteLink = 'https://fcainfoweb.nic.in/reports/report_menu_web.aspx'
    driver.get(websiteLink)

    ## scrape data
    # finalData = scrapeData(driver)
    scrapeData(driver)

    time.sleep(15)
    driver.quit()


def scrapeData(driver):

    ##select Report Type
    reportType = Select(driver.find_element_by_id("ctl00_MainContent_Ddl_Rpt_type"))
    reportType.select_by_value('Retail')
    

    ##Select Price Report
    driver.find_element_by_id("ctl00_MainContent_Rbl_Rpt_type_0").click()

    ##Select Daily Prices
    try: 
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_Ddl_Rpt_Option0")))
    finally:
        pricesType = Select(driver.find_element_by_id("ctl00_MainContent_Ddl_Rpt_Option0"))
        pricesType.select_by_value('Daily Prices')

    ##Select Date
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_Txt_FrmDate")))
    finally:
        driver.find_element_by_id("ctl00_MainContent_Txt_FrmDate").send_keys("08/04/2021")
    
    driver.find_element_by_id("ctl00_MainContent_btn_getdata1").click()




    ##now we have the data page open!!:))
    # ##print click
    # try: 
    #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btn_print")))
    # finally:
    #     driver.find_element_by_id("btn_print").click()
    return 


main()