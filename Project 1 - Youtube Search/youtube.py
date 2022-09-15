from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
key = input('Search: ')
options = Options()
# options.add_argument()
driver = webdriver.Chrome()
driver.get(f'https://www.youtube.com/results?search_query={key}')
print(f'Searched: {key} ! ')


