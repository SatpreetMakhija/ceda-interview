from typing import final
import requests
from requests.api import request
from bs4 import BeautifulSoup as bs4
import csv



websiteLink = "https://agmarknet.gov.in/"
res = requests.get(websiteLink)
htmlPage = bs4(res.text, 'html.parser')


##get commodities List
commodity = htmlPage.find("select", id = "ddlCommodity").findAll("option")
commodityList = []
for item in commodity:
    commodityList.append((item.text, item['value']))
#remove (--Select, 0) from the list
del commodityList[0]




finalData = []

for i in range(len(commodityList)):
    url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=" + commodityList[i][1] + "&Tx_State=DL&Tx_District=1&Tx_Market=0&DateFrom=10-May-2021&DateTo=16-May-2021&Fr_Date=10-May-2021&To_Date=16-May-2021&Tx_Trend=1&Tx_CommodityHead=Pumpkin&Tx_StateHead=NCT+of+Delhi&Tx_DistrictHead=Delhi&Tx_MarketHead=--Select--"
    res = requests.get(url)

    commodityPage = bs4(res.text, "html.parser")
    span = commodityPage.find("span", id = "cphBody_GridArrivalData_lblarrival_std_unit_0")

    #if commodity data exists otherwise
    if span:
        #add commodityName, commodityValue
        commodityValue = span.text
        finalData.append(([commodityList[i][0], commodityValue]))
    else:
        #add commodityName, 'NOT FOUND'
        commodityValue = 'NOT FOUND'
        finalData.append(([commodityList[i][0], commodityValue]))





    
#write finalData
with open("./agmarketData/10-05-21_to_16-05-21.csv", "w+") as file:
    csvWriter= csv.writer(file, delimiter = ",")
    csvWriter.writerows(finalData)
print(finalData)        