### PYTHON LIBRARIES
import os, sys, time, random
import fileinput

### EXTERNAL LIBRARIES (SELENIUM)
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *

### LINKS CONFIG ###
links = [line.rstrip('\n') for line in open('urls.txt', 'r')]
proxyList = [proxy.rstrip('\n') for proxy in open('proxylist.txt', 'r')]


### LOG MESSAGES TO TERMINAL ###
def log(message):
    print(message)


def replaceAll(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)


def readystate_complete(d):
    # AFAICT Selenium offers no better way to wait for the document to be loaded,
    # if one is in ignorance of its contents.
    return d.execute_script("return document.readyState") == "complete"


def sage():
    ### INITIATE BROWSER UNDER PROXY CONFIG

    myProxy = str(random.choice(proxyList))
    myProxy = myProxy.rstrip()
    
##    proxy = Proxy({
##        'proxyType': ProxyType.MANUAL,
##        'httpProxy': myProxy,
##        'ftpProxy' : myProxy,
##        'sslProxy' : myProxy,
##        'socksProxy' : myProxy,
##        'noProxy': ''
##        })
##
##    profile = webdriver.FirefoxProfile()
##    profile.set_preference("browser.cache.disk.enable", False)
##    profile.set_preference("browser.cache.memory.enable", False)
##    profile.set_preference("browser.cache.offline.enable", False)
##    profile.set_preference("network.http.use-cache", False)
##
##    fox_cap = DesiredCapabilities.FIREFOX
##    fox_cap["wires"] = True
##    
##
##    browser = webdriver.Firefox(profile, proxy=proxy, capabilities=fox_cap)


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument("--proxy-server=%s" % myProxy)
    chrome_options.add_extension(os.getcwd() + '\Timestopper.crx')
    browser = webdriver.Chrome(executable_path='chromedriver.exe',
                              options=chrome_options)
    browser.set_page_load_timeout(120)
    
    try:
        browser.get("http://www.techshinobi.com/browser/test-page.html")
        assert "Tech-Shinobi-Test-Page" in browser.title
        log("[+] Proxy: %s passed initial test" % (myProxy))
    except:
        log("[-] Proxy: %s failed initial test" % (myProxy))
        try:
            log("[-] Failed proxy: %s removed from list" % (myProxy))
            replaceAll("proxylist.txt", myProxy + "\n", "")
        except:
            pass
        browser.quit()
        sys.exit(0)

        
    for link in links:
        try:
            ### OPEN FIREFOX BROWSER AND VISIT URLS ###
            browser.get(str(link))            
            
            ### WAIT FOR BROWSER READY STATE ###
            WebDriverWait(browser, 90).until(readystate_complete)
            
            ### SLEEP FOR DURATION ###
            sleepingTime = random.randrange(90, 120)
            log("[+] Sleeping %s seconds between next query" % (sleepingTime))
            time.sleep(sleepingTime)
        except:
            ### QUIT IF CONNECTION FAILS ###
            log("[-] Connection to proxy failed ... Closing browser")
            try:
                log("[-] Failed proxy: %s removed from list" % (myProxy))
                replaceAll("proxylist.txt", myProxy + "\n", "")
            except:
                pass
            browser.quit()
            sys.exit(0)
    else:            
        ### QUIT WHEN DONE FOR NEXT LAUNCH ###
        browser.quit()
        sys.exit(0)

        
if __name__ == '__main__':
    sage()
