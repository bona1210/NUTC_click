# -*- coding=utf-8 -*-
import urllib.request
import socket
import time
import sys

# 設定網址
urls = "https://elearn.nutc.edu.tw/forum/m_node_chain.php?cid=10071642&bid=1000202245&nid=000000001"
 

print("\n開始訪問網頁...")
# 設定次數
brushNum = 4

for i in range(brushNum):
    # 設定timeout (單位：秒)
    socket.setdefaulttimeout(120)
    
    # 記得更改cookie
    
    headers = {
 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
 'Cookie':'PHPSESSID=4f0a6ul4tq24ujlo2kj2r3phs5; sIdx=; _ga=GA1.3.1664925445.1663918416; school_hash=f1f431772863feb541000143e736476d; wm_lang=Big5; idx=399adbdd08c09b6502032f545fea8272'}
    req = urllib.request.Request(urls, headers=headers)
    urllib.request.urlopen(req).read()    
    # 計算次數
    
    print("目前",i+1,"次",",剩餘：",brushNum-i-1,"次")
    # 等待 
    print()
    #time.sleep(0.1)
