from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
driver=webdriver.Chrome(executable_path="C:\\Users\\HitanshuRami\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe") #used to set chromepath
def f1():
    driver.maximize_window()
    driver.get("https://www.egov.aging.state.il.us/IdentityGuardAuth/IdentityGuardLogin.aspx?IGDest=https://www.egov.aging.state.il.us/eGov/root/dn.asp")
    driver.implicitly_wait(7)
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/center/table/tbody/tr/td[2]/div[1]/div/div/table/tbody/tr[2]/td[3]/span/input").send_keys("harivadan")
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/center/table/tbody/tr/td[2]/div[1]/div/div/table/tbody/tr[3]/td[2]/span/input").send_keys("Jm941200")
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/center/table/tbody/tr/td[2]/div[1]/div/div/table/tbody/tr[4]/td/center/input").click()
    driver.implicitly_wait(7)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("/html/body/div[14]/table/tbody/tr/td[2]/a/img").click()
    driver.find_element_by_xpath("/html/body/div[17]/table/tbody/tr/td[3]/a").click()
    driver.implicitly_wait(7)
    select = Select(driver.find_element_by_name('sltProviderContractNumber'))
    select.select_by_value('ADS1712019')

    driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[5]/td/p[2]/input[1]").send_keys(10)
    driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[5]/td/p[2]/input[2]").send_keys(2019)
    driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[10]/td/div/input[1]").click()
    driver.implicitly_wait(5)
    for tr in driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/table[2]'):
        tds = tr.find_elements_by_tag_name('td')
        print ([td.text for td in tds])
    driver.close()

data=pd.read_excel("C:\\Users\\HitanshuRami\\Desktop\\Pending\\octt_vrfp.xlsx",sheetname="Sheet2")
ssn=list(data['SSN'])
#print(ssn)

#ssn=322689558
driver.maximize_window()
driver.get("https://secure1.illinois.gov/AGE/ParticipantSearch/")
driver.implicitly_wait(7)
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/table[1]/tbody/tr[5]/td/table/tbody/tr[3]/td[1]/input").click()
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/table[1]/tbody/tr[11]/td/table/tbody/tr[2]/td[2]/input").send_keys("harivadan.patel")
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/table[1]/tbody/tr[11]/td/table/tbody/tr[3]/td[2]/input").send_keys("Km@941200")

driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/table[1]/tbody/tr[11]/td/table/tbody/tr[4]/td[2]/input").click()
time.sleep(5)
for s in ssn:
    s=int(s)
    print(s)
    driver.find_element_by_xpath("/html/body/div/section/div/div/form/div[1]/div[2]/input").clear()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/section/div/div/form/div[1]/div[2]/input").send_keys(s)
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/section/div/div/form/div[3]/div[2]/input").click()
    time.sleep(5)
    #time.sleep(50)
    table=driver.find_element_by_xpath("/html/body/div/section/div/div/div[2]/table")
    print(table.find_element_by_xpath('.//tbody/tr[1]').text)


    table=driver.find_element_by_xpath("/html/body/div/section/div/div/div[7]/table")
    print(table.find_element_by_xpath('.//tbody/tr[1]').text)
#print(table.find_element_by_xpath('.//tr[2]').text)
#tr=table.find_element_by_tag_name('tr')
#print(tr.text)

driver.implicitly_wait(50)
driver.close()
