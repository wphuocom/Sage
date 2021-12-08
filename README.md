# Sage
Sage is a Python Script/SEO utility designed to automate browser services in order to decrease the bounce rate in the analytics of a website to a reasonable percentage.


How Sage Works
--------------
Sage effectively utilizes free proxy lists and the Selenium API to navigate to a website with browser automation (Selenium). On each execution a request is made to the proxy list for a new IP address. During this process the client (web browser) waits for an appropriate amount of time before transitioning to a different section of your website or a new domain in your domain list. You specify each URL for the browser to navigate to in the domain list (**urls.txt**).

If a proxy in the proxylist fails to load, the script will stop itself and relaunch with a new IP address. The script will wait for a total of 90 seconds to attempt to receive the connection. We do this simply because proxies can often be quite slow or offline.


Install
-------
* Install the Chrome Browser
* Install Python 3.9
* You will need to install Selenium:
	* pip install Selenium
* You will need to place the latest **stable** Chrome Driver (chromedriver.exe) on your OS environment path. https://sites.google.com/a/chromium.org/chromedriver/downloads


Build Proxy List
----------------
* Gather a working proxy list and name the file proxylist.txt. (With each proxy address on a separate line)
* Sage will by default use the proxylist.txt file
* In the Sage folder there is a script called proxyGrabber.py, proxyGrabber.py will gather a list of freely available proxies.


Modify Script
--------------
* Create a domain/url list in urls.txt
* Modify runChrome.py specifying the amount of times you wish to run the script
* Timestopper.crx is a browser extension for the project. It is designed to block window.alert and window.confirm dialog boxes. I found that some proxies would create confirm and alert dialogs boxes and they would halt the script. So I made this extension to prevent that. You can disable this extension simply by commenting out this line: `chrome_options.add_extension(os.getcwd() + '\Timestopper.crx')`		
		
Launching
---------
* Run the script with this command: python runChrome.py


Notes
-----
* You will not see results if browsing to a single page on a website. This has to do with how bounce rate is calculated from average session duration in Google Analytics.

* After exiting the script 'runChrome.py' you will need to do additional cleanup by killing any of the remaining Chrome processes still present.

Let it continue as it loops through your domain list using your Chrome browser, the script will pause between 90 and 120 seconds on each page it navigates to. When it finishes the loop the script will close and respawn with a new IP address.

![Image of Sage](https://images.suck-o.com/static/images/image_uploads.file_upload.b930c500450f6ff6.73637265656e73686f742e706e67.png)

