# **About WAtchman**
WAtchman is a low-key bot written with Python.     
Its purpose is to monitor individuals on Web-WhatsApp in order to log the time a victim is online or not.    
This way it's impossible for victims to hide their "Last Time Seen"-status as everything is beeing logged and analysed.

# **Dependencies**
 - [Python 2.7+](https://www.python.org/download/releases/2.7/)
 - [Pip](https://pypi.python.org/pypi/pip)
 - [Selenium](https://pypi.python.org/pypi/selenium)
 - [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

# **Installing**
1. Make sure you have [Python 2.7+](https://www.python.org/download/releases/2.7/) installed
2. If you still need to install Selenium, install [Pip](https://pypi.python.org/pypi/pip) first
3. Install [Selenium](https://pypi.python.org/pypi/selenium) via Pip
4. Add the location of '[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)' to your PATH Variable **OR**
	- In WAtchman.py uncomment line 70
	- Edit 'CHROMEDRIVER-LOCATION-HERE' to the absolute location of your chromedriver
	- Comment line 71
5. Give full rights to chromedriver & WAtchman.py as the script might create folders and write to log-files

# **Useage**
1. Start WAtchman via console (**Optional**: Pass Arguments)
	- #1 Argument: The victims name exactly as you have it saved
	- #2 Argument: The monitoring duration in minutes
	- #3 Argument: Enable logging (Y/N) 
2. Wait for WAtchman to boot up
3. **Manually** login by scanning the QR-Code with your mobile phone

**Done** - Watch the console for live updates

# **Notice**
 - There is currently no way to let the Script run infinitely.
 - Each victim has its own folder in the logs folder
 - The "logs" folder will get created automaticly once logging initially used
 - Log-files will be created once is the script is finished or terminated
 - There is a minor bug which occurs rarely - The script will fail before monitoring
 - The victims name is treated case sensitive
 - Avoid names with emojis, it will fail
 - Changing the chat will make the script monitor the new chat - **This completely breaks the analysis**
 - After the first online-state has been detected the timer starts running

# **Preview**

# **Developer**
 - **Shiva**