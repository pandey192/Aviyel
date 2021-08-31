from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/home/shivam/Downloads/pycharm/chromedriver')


# URL of the website
url = "https://www.google.com/"


driver.get(url)


driver.find_element_by_xpath('//input[@title="Search"]').send_keys("UI Test Automation Playground")

time.sleep(2)
driver.find_element_by_xpath('//div[@class="lJ9FBc"]//input[@name="btnK"]').click()  

print('web page header tags found seo')

driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()

time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Dynamic ID")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()

time.sleep(2)

print('web page header tags not found seo')

driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Class Attribute")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags not found seo')

driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Hidden Layers")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags not found seo')

driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Load Delay")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags not found seo')

driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("AJAX Data")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags not found seo')

driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Client Side Delay")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Click")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Text Input")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Scrollbars")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Dynamic Table")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')



driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Verify Text")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Progress Bar")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Visibility")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Sample App")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')

driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Mouse Over")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.find_element_by_xpath('//input[@aria-label="Search"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//input[@aria-label="Search"]').send_keys("Non-Breaking Space")

time.sleep(2)

driver.find_element_by_xpath("//span[@class='z1asCe MZy1Rb']//*[local-name()='svg']").click()
print('web page header tags Not found seo')


driver.close()