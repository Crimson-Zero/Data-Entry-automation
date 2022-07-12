import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


address_list=[]
amount_list=[]
link_list=[]

driver = webdriver.Chrome()

headers = {
    "Accept-Language" : "lan",
    "User-Agent" : "Agent"
    
    }

response = requests.get(url = "https://www.zillow.com/san-francisco-ca/rentals/",headers=headers)
website = response.text
soup = BeautifulSoup(website , "html.parser")



address = soup.find_all(name = "address", class_="list-card-addr")


for address_acq in address:
    address_text = address_acq.text
    address_list.append(address_text)

print(address_list)

amount_element = soup.find_all(name= "div",class_= "list-card-price")


for amount_get in amount_element:
    amount = amount_get.text.split('+')[0]
    amount_list.append(amount)

print(amount_list)


all_link_elements = soup.select(".list-card-top a")



for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        link_list.append(f"https://www.zillow.com{href}")
    else:
        link_list.append(href)

print(link_list)

for n in range(len(link_list)):
    
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSerTvbyPETpT5RwYF2qDKQ0BdgkS73BhxQhWDC77DvTmg3zyw/viewform?usp=sf_link')
    address_send = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
     
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    address_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    
    address_send.send_keys(address_list[n])
    price.send_keys(amount_list[n])    
    address_link.send_keys(link_list[n])
    submit_button.click()
    
time.sleep(20)
