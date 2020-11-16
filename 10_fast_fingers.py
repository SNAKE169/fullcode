from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

PATH = r"D:\Document\\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=options)
driver.get("https://10fastfingers.com/typing-test/vietnamese")
driver.implicitly_wait(15)
# try:    
#     ok = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "highlight"))
#     )

# except:
print(0)
search = driver.find_element_by_id('inputfield')
spans = driver.find_elements_by_css_selector('#row1 > span')
for text in spans:
    txt = text.text
    for i in txt:
        search.send_keys(i)
    search.send_keys(Keys.SPACE)
time.sleep(100)