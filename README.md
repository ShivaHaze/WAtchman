# **About WAtchman**
WAtchman is a bot written in Python.
The purpose is to monitor individuals on Web WhatsApp in order to harvest the time one is online or not.
This way it's not possible for victims to hide their "Last Time Seen"-Status as everything is beeing logged.

# **Dependencies**
 - [Python 2.7+](https://www.python.org/download/releases/2.7/)
 - [Pip](https://pypi.python.org/pypi/pip)
 - [Selenium](https://pypi.python.org/pypi/selenium)
 - [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

# **Installing**
1. Make sure you have [Python 2.7+](https://www.python.org/download/releases/2.7/) installed
2. If you still need to install Selenium, install [Pip](https://pypi.python.org/pypi/pip) first
3. Download [Selenium](https://pypi.python.org/pypi/selenium) via Pip
4. Add the location of '[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)' to your PATH Variable OR
	- In WAtchman.py uncomment line 51
	- Edit 'CHROMEDRIVER-LOCATION-HERE' to the absolute location of your chromedriver
	- Comment line 52
5. Make sure you have the privileges to execute chromedriver & WAtchman.py

# **Useage**
1. Start WAtchman via console with or without arguments
	- First Argument: Target name
	- Second Argument: Monitoring duration in minutes ()
2. Wait for WAtchman to start Chrome and navigate to Web-Whatsapp
3. **Manually** login by scanning the QR-Code with your mobile phone
4. Wait for WAtchman to navigate to the target's chat
5. After the first online-state has been detected the timer starts running

# **Preview**
**Following**

# **Developer**
Shiva