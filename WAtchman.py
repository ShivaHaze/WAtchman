from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import datetime
import sys  

try:
	target = ""
	duration = ""
	logging = ""

	target = sys.argv[1]
	duration = int(sys.argv[2])
	logging = int(sys.argv[3])
except:
	pass

print "________________________________________"
print ""

if target == "":
	target = raw_input("Target name: ")
else:
	print "Target name: " + target

if duration == "":
	duration = input("Duration in minutes: ")
else:
	print "Duration in minutes: " + str(duration)

if logging == "":
	logging = raw_input("Activate logging? Y/N: ")
else:
	print "Activate logging? Y/N: " + str(logging)

print "________________________________________"

if duration != 0:
	duration = duration * 60
	int(duration)

now = datetime.datetime.now()
website = "https://web.whatsapp.com/";
xpath_target = '//span[@title="' + target + '"]'
xpath_input = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
xpath_online = '//*[@id="main"]/header/div[2]/div[2]/span'
lastOnlineState = ""
totalOnline = 0
totalOffline = 0
timeElapsed = 0
fileName = "[" + str(now.day) + "." + str(now.month) + "." + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + "] [" + target + "].log" 

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.split(scriptPath)[0]

relTotalPath = "logs/" + target + "/" + fileName
relLogFolderPath = "logs/" + target + "/"

absFilePath = os.path.join(scriptDir, relTotalPath)
absFolderPath = os.path.join(scriptDir, relLogFolderPath)

print ""
print "Launching Chrome"
print ""

#driver = webdriver.Chrome('CHROMEDRIVER-LOCATION-HERE')
driver = webdriver.Chrome()

print "Navigating to '" + website + "'"
print ""
driver.get("https://web.whatsapp.com/")

print "Loading website content.."
print ""
wait = WebDriverWait(driver, 600)

print "Waiting until '" + target + "' is locateable"
print " - Login to continue - "
print ""
targetName = wait.until(EC.presence_of_element_located((By.XPATH, xpath_target)))

print "Open chat with '" + target + "'"
print ""
targetName.click()

print "Wait for chat to load.."
print ""
onlineState = wait.until(EC.presence_of_element_located((By.XPATH, xpath_online)))
time.sleep(3)

if logging == "y" or logging == "Y" or logging == 1:
	if not os.path.exists(absFolderPath):
	    print "Log folder for '" + target + "' missing - Creating new one"
	    print ""
	    os.makedirs(absFolderPath)

	print "Logging started in"
	print "'" + absFilePath + "'"
	print ""
	f = open(absFilePath, "w")

print "Monitoring '" + target + "'"
print "________________________________________"
print ""

for x in range(0, duration):
	now = datetime.datetime.now()
	
	if now.second < 10:
		seconds = "0" + str(now.second)
	else:
		seconds = str(now.second)

	if now.minute < 10:
		minutes = "0" + str(now.minute)
	else:
		minutes = str(now.minute)

	if now.hour < 10:
		hours = "0" + str(now.hour)
	else:
		hours = str(now.hour)	

	timenow = "[" + hours + ":" + minutes + ":" + seconds + "]"

	try:
		driver.find_element_by_xpath(xpath_online)
		currentOnlineState = "Online"
	except:
		currentOnlineState = "Offline"
	
	try:
		timeElapsed = time.time() - oldNow
	except:
		oldNow = time.time()

	timeElapsed = int(timeElapsed)

	if lastOnlineState == "Online":
		totalOnline += 1
	else:
		totalOffline += 1

	onlineProportion = (totalOnline*100.00/(totalOnline*100.00 + totalOffline*100.00))*100.00
	onlineProportion = round(onlineProportion, 2) 

	if lastOnlineState != currentOnlineState:		
		if lastOnlineState != "":
			print " --- " + timenow + " --- "
			print "[" + target + "] " + currentOnlineState + " (" + str(timeElapsed) + " seconds " + lastOnlineState + ")"
			print "[" + target + "] was " + lastOnlineState + " from " + oldTimeNow + " - " + timenow
			print "[Total Time] " + str(totalOnline) + " seconds Online | " + str(totalOffline) + " seconds Offline"
			print "[Online Proportion] " + str(onlineProportion) + "%"
		
			if logging == "y" or logging == "Y" or logging == 1:
				f.write(" --- " + timenow + " --- \n")
				f.write("[" + target + "] " + currentOnlineState + " (" + str(timeElapsed) + " seconds " + lastOnlineState + ")\n")
				f.write("[" + target + "] was " + lastOnlineState + " from " + oldTimeNow + " - " + timenow)
				f.write("[Total Time] " + str(totalOnline) + " seconds Online | " + str(totalOffline) + " seconds Offline\n")
				f.write("[Online Proportion] " + str(onlineProportion) + "%\n")  
		else:
			print " --- " + timenow + " --- "
			print "[" + target + "]" + " is " + currentOnlineState
			
			if logging == "y" or logging == "Y" or logging == 1:
				f.write(" --- " + timenow + " --- \n")
				f.write("[" + target + "]" + " is " + currentOnlineState + "\n")

		oldTimeNow = timenow
		oldNow = time.time()
		lastOnlineState = currentOnlineState
		
		print ""

		if logging == "y" or logging == "Y" or logging == 1:
			f.write("\n")
	
	time.sleep(1)

print "________________________________________"
print "Monitoring '" + target + "' finished after " + str(duration/60) + " minute(s)."
print ""
print "[Total Time] " + str(totalOnline) + " seconds Online | " + str(totalOffline) + " seconds Offline"
print "[Online Proportion] " + str(onlineProportion) + "%"
print ""

if logging == "y" or logging == "Y" or logging == 1:
	f.write("________________________________________\n")
	f.write("Monitoring '" + target + "' finished after " + str(duration/60) + " minute(s).\n")
	f.write("\n")
	f.write("[Total Time] " + str(totalOnline) + " seconds Online | " + str(totalOffline) + " seconds Offline\n")
	f.write("[Online Proportion] " + str(onlineProportion) + "%\n")

	f.close()

sys.exit(1)