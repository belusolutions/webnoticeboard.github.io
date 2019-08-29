from selenium import webdriver
import time
import urllib
import urllib3

x=input("Enter the URL")
refreshrate=input("Enter the number of seconds")
refreshrate=int(refreshrate)
driver = webdriver.Chrome()
driver.get("http://"+x)
while True:
    time.sleep(refreshrate)
    driver.refresh()
