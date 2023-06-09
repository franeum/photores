#!/usr/bin/env python3

import socket
from datetime import datetime
import time

TOTAL_TIME = 14400
UDP_IP = ""
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

file = open("log.txt", 'a+', encoding='utf-8')
start = time.time()

counter = 0

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    ora = datetime.now()
    ora_format1 = ora.strftime("%Y/%m/%d")
    ora_format2 = ora.strftime("%H:%M:%S")
    
    if counter % 1000 == 0:
        print(ora_format2, data)
        counter += 1

    t = time.time()
    if (t - start) >= TOTAL_TIME:
        break
    else:
        file.write(f"('{ora_format1}', '{ora_format2}', {float(data)}),\n")

file.close()
