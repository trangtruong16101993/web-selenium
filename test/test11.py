from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/trangtruong/Desktop/web-selenium/chromedriver")
driver.implicitly_wait(10)

url = 'https://release.gigacover.com/'

driver.get(url)
c = driver.find_elements_by_xpath("//a[(text()='Income Protection')]").click()
