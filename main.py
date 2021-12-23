import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
os.environ['PATH']+=os.pathsep+"/home/faisal/Documents/chromeDriver"
options=Options()
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36')
driver=webdriver.Chrome(chrome_options=options)
driver.get('https://www.agoda.com/')
driver.implicitly_wait(30)
text_input=driver.find_element_by_css_selector('input.SearchBoxTextEditor')
text_input.clear()
text_input.send_keys('jakarta')
text_input.send_keys(Keys.ENTER)
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME,'ab-close-button'))).click()