from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")

search_bar = driver.find_element_by_class_name("gLFyf")
search_bar.send_keys("hello!")
search_bar.send_keys(Keys.ENTER)

results = driver.find_elements_by_class_name("g")
print(results)

# driver.quit()
while True:
    pass