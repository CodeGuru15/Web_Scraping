from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import time


chrome_path = "chromedriver.exe"
service = Service(executable_path=chrome_path)
driver = webdriver.Chrome(service = service)

url = "https://en.m.wikipedia.org/wiki/FIFA_World_Cup#Attendance"


driver.get(url) 
time.sleep(3)
section = driver.find_element(By.ID,"content-collapsible-block-4")
table = section.find_element(By.TAG_NAME,'table')
t_headers = table.find_elements(By.TAG_NAME,'th')
tbody = table.find_element(By.TAG_NAME,"tbody")
rows = tbody.find_elements(By.TAG_NAME,'tr')


def web_scraping(desired_columns):
    
    extracted_data = [] # To store the collected data
    theads = ["year","hosted_by","venue","total_attendance","matches","avg_attendance","highest_attendace"] 
  
    for row in rows:
       row_data = {}
       cells = row.find_elements(By.TAG_NAME, 'td')   
       for i, cell in enumerate(cells):
            if i in desired_columns:
                if i == 3: 
                    cell_value = cell.text.strip()
                    if cell_value == "":
                      row_data[theads[i]] = cell_value
                    else:
                      row_data[theads[i]] = int(cell_value.replace(",",""))  
                else:
                    row_data[theads[i]] = cell.text.strip()
                extracted_data.append(row_data)

    final_data = dict( attendance = extracted_data)

    print(json.dumps(final_data, indent= 2))

web_scraping([0,1,3])






