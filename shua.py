# -*- coding=utf-8 -*-
import urllib.request
import socket
import time
import sys

# 設定網址
urls = "輸入步驟一"
 

print("\n開始訪問網頁...")
# 設定次數
brushNum = 150

for i in range(brushNum):
    # 設定timeout (單位：秒)
    socket.setdefaulttimeout(120)
    
    # 記得更改cookie
    
    headers = {
 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
 'Cookie':'輸入步驟二'}
    req = urllib.request.Request(urls, headers=headers)
    urllib.request.urlopen(req).read()    
    # 計算次數
    
    print("目前",i+1,"次",",剩餘：",brushNum-i-1,"次")
    # 等待 
    print()
    #time.sleep(0.1)
