import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

scrapeUrl = "https://weixin.sogou.com/weixin?p=01030402&query=%E6%A5%BC%E5%B8%82%E5%8F%82%E8%80%83&type=2&ie=utf8"
req = urllib.request.Request(scrapeUrl)
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)') 
response = urllib.request.urlopen(req)  
html = response.read()
    
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.__str__())