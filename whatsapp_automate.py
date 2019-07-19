import time
from selenium import webdriver

contactName = input('Who to send message ? ')
message = input('What to tell ?')
driver = webdriver.Chrome('chrome web driver path')
driver.get("https://web.whatsapp.com/")
time.sleep(10);
contacts = driver.find_elements_by_class_name('_3H4MS') 

index = 0;
for i in range(0,len(contacts)):
	if contacts[i].text == contactName:
		index = i;
		break

contacts[index].click()
chatBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
chatBox.send_keys(message)
enterKey = driver.find_element_by_class_name('_3M-N-')
enterKey.click()