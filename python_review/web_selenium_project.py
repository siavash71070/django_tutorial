from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = Chrome(executable_path='chromedriver.exe')
driver.get("https://google.com")
search_bar = driver.find_element_by_name('q')
search_bar.send_keys("آموزش پایتون مکتبخونه")
search_bar.send_keys(Keys.ENTER)
soup = BeautifulSoup(driver.page_source)

name_list = soup.find_all('h3')
with open('name.txt', 'a', encoding='utf8') as f:
    for name in name_list:
        f.write(name.text)
        f.write('\n')
input()