# CoDDED BY ARI4N
# Telegram : @ariancom


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform
#میتونید به دلخواه این قسمت رو تغییر بدهید
options = Options()
if platform == "linux":
	options.binary_location = r"/home/arian/Desktop/wibulk/chromedriver"

print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****             WHATSAPP BULK MESSENGER           ******")
print("*****                 CoDDED by ARI4N 	           ******")
print("*****               telegram: @ariancom             ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")

f = open("Yourmessage.txt", "r")
message = f.read()
f.close()

print("##########################################################")
print('This is your message\n\n')
print(message)
print("##########################################################")
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line != "":
		numbers.append(line)
f.close()
total_number=len(numbers)
print("##########################################################")
print('\nWe found ' + str(total_number) + ' numbers in the file')
print("##########################################################")
print()
delay = 30

driver = webdriver.Chrome(executable_path="/home/arian/Desktop/wibulk/chromedriver")
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable	.")
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print('{}/{} => Sending message to {}.'.format((idx+1), total_number, number))
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME , '_4sWnG')))
				except Exception as e:
					print(f"Something went wrong..\n Failed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it.")
					input("Press enter to continue")
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print('Message sent to: ' + number)
	except Exception as e:
		print('Failed to send message to ' + number + str(e))
