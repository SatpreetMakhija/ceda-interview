from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time
import csv

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


    dates = ["10/04/2021", "11/04/2021"]



    for date in range(1, 31):

        ## set date
        if (date < 10):
            dateToScrape = "0" + str(date) + "/04/2021"
        else:
            dateToScrape = str(date) + "/04/2021"

        
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
            driver.find_element_by_id("ctl00_MainContent_Txt_FrmDate").send_keys(dateToScrape)
        
        driver.find_element_by_id("ctl00_MainContent_btn_getdata1").click()




        ##now we have the data page open!!:))
        try: 
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btn_print")))
        finally:
            rows_xpath = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr/td/div/div/table/tbody/tr"
            rows = 1 + len(driver.find_elements_by_xpath(rows_xpath))
            columns_xpath = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[1]/td"
            columns = len(driver.find_elements_by_xpath(columns_xpath))

            ##array to store data for each day
            dayData = []
            

            ##get the table headings
            dayDataHeadings = []
            for p in range(1, columns+1):
                value = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr/td/div/div/table/thead/tr/th["+str(p)+"]").text
                dayDataHeadings.append(value)
            dayData.append(dayDataHeadings)
            

            




            ##Loop over the table
            for r in range(1, rows):
                dayData.append([])
                for p in range(1, columns+1):
                    value = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr/td/div/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                    dayData[r].append(value)

            fileName = dateToScrape[:2] + "-" + dateToScrape[3:5] + "-" + dateToScrape[6:] + ".csv"
            with open("./retailPricesData/"+fileName, "w+") as file:
                csvWriter = csv.writer(file, delimiter=',')
                csvWriter.writerows(dayData)

            print(dayData)
        
        print("[INFO]scraped  for date: " + dateToScrape)
        ## now return to home page
        driver.find_element_by_id("btn_back").click()



    return 


main()