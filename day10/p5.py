from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()

service=Service(ChromeDriverManager().install)

driver=webdriver.Chrome(service=service,options=options)

try:
    driver.get("http://www.google.com")

    input("Press Enter to close the browser..")

finally:

    driver.quit()