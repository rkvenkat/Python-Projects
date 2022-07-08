#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException        
import time
from bs4 import BeautifulSoup
import re
import csv

data = []

def verify(driver):
    try:
        driver.find_element(By.CSS_SELECTOR,'div.dmach-loadmore.et_pb_button.result_count_right')
    except NoSuchElementException:
        return False
    return True

def open_browser(year):    

    driver = webdriver.Chrome('/home/venkat/Downloads/chromedriver_linux64/chromedriver')
    driver.get(f'https://datascience.duke.edu/people/graduation-year/{year}/')

    button_exists = True

    while button_exists:
        country = driver.find_element(By.CSS_SELECTOR,'div.dmach-loadmore.et_pb_button.result_count_right')
        country.click()
        time.sleep(10)
        button_exists = verify(driver)
    

    a = driver.find_element(By.XPATH,"//*").get_attribute("outerHTML")

    soup = BeautifulSoup(a, 'html.parser')

    x = soup.find_all("div",{"class" : "grid-posts loop-grid"})

    h = soup.find_all("div", {"class": "et_pb_module_inner"})

    c = h[0].find_all('div', attrs={'class': re.compile(f'graduation_year-{year}')})

    for i in c:
        name = i.find('h2',attrs={'itemprop':'name'}).text
        url = i.find('div',{"class":"bc-link-whole-grid-card"})['data-link-url']
        year = year
        class_names = i['class']
        role = [i for i in class_names if 'role' in i][0]
        role = role.replace("role-","")   
        data.append([name,url,role,year])

    return data   


for i in range(2020,2024):
    open_browser(i)



with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)