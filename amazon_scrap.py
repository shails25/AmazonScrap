from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json


options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")

dealslist = []

def getdeals():

    val = input("Enter a product to search: ")
    driver = webdriver.Chrome(options)
    driver.get("https://www.amazon.in")
    driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(val)
    driver.find_element(By.ID, 'nav-search-submit-button').click()

    products = driver.find_elements(By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[contains(@class, 's-result-item')]")
    
    for items in products:
        
        try:
            title = items.find_element(By.XPATH, './/span[contains(@class, "a-text-normal")]').text
        except:
            title = ''
        
        try:
            sponsored = items.find_element(By.XPATH, './/a[contains(@class, "sponsored")]').text
        except:
            sponsored = 'NA'

        try:
            saleprice = float(items.find_element(By.XPATH,'.//span[contains(@class, "a-price-whole")]').text.replace('₹','').replace(',','').strip())
            # oldprice = float(items.find_element(By.XPATH, './/span[contains(@class, "a-price")]/span[contains(@class, "a-offscreen")]').text.replace('₹','').replace(',','').strip())
            oldprice = float(items.find_element(By.XPATH, './/span[contains(@class, "a-price-whole")]').text.replace('₹','').replace(',','').strip())
        except:
            saleprice = 'NA'
            oldprice = 'NA'

        # print(saleprice)
        # print(oldprice)

        try:
            asin = items.get_attribute('data-asin')
        except:
            asin = ''

        # print(asin)

        if title != '':
            saleitem = {
                'title': title,
                'price': saleprice,
                'sponsored': sponsored,
                'asin': asin
            }
            
            dealslist.append(saleitem)
    driver.quit()
    return

getdeals()
print(json.dumps(dealslist, indent=4))

