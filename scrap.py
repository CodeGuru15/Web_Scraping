from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_path = "chromedriver.exe"
service = Service(executable_path=chrome_path)
driver = webdriver.Chrome(service = service)

url = "https://en.m.wikipedia.org/wiki/FIFA_World_Cup#Attendance"


driver.get(url)
section = driver.find_element(By.ID,"content-collapsible-block-4")
table = section.find_element(By.TAG_NAME,'table')
t_headers = table.find_elements(By.TAG_NAME,'th')
tbody = table.find_element(By.TAG_NAME,"tbody")
rows = tbody.find_elements(By.TAG_NAME,'tr')


def web_scraping(desired_columns):
    
    extracted_data = [] # To store the collected data

    for row in rows:
        row_data = {}
        cells = row.find_elements(By.TAG_NAME, 'td')

        for i, cell in enumerate(cells):
          if i in desired_columns:
            # Extract text content from the desired columns
              row_data[t_headers[i].text] = cell.text.strip()
              extracted_data.append(row_data)

    print(extracted_data)

web_scraping([0,1,3])






