import urllib.request
def proxyScrape():
    url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    file = urllib.request.urlopen(url)
    print("[+] Writing proxies to a file")
    with open('proxylist.txt','wb') as output:
        output.write(file.read())
    print("[+] File generation completed")
          
proxyScrape()
