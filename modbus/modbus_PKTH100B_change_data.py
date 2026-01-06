# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 11:17:51 2025

@author: Fabian Mink
"""


#PKTH100B Temperatur /  Humidity Modul Address / Baudrate changing Bytes calculation


#https://medium.com/@boonsanti/how-to-change-device-id-of-pkth100b-cz1-modbus-rtu-temperature-humidity-sensor-5bbb4e173358
# Set Slave addr and baud rate (message dedscription)
# ===================================================
# 
# Request:
# --------
# 01      Slave addr
# 06      Function Code (Write Single register)
# 00 00   Start Address (0)  
# 00 01   Register value (1)
# 02      Number of additional data bytes (Non standard extension)
# AA      New slave addr (Non standard extension)
# BB      New baud rate (Non standard extension)
# 
# Response:
# --------
# 01      Slave addr
# 06      Function Code (Write Single register)
# 00 00   Start Address (0)  
# 00 01   Register value
# 
# 
# Slave addr AA:
# 01-F7
# 
# Baud rate BB:
# 03: 1200
# 04: 2400
# 05: 4800
# 06: 9600
# 07: 19200


def calcModbusCrc(msg):
    crc = 0xFFFF
    for ibytes in range(len(msg)):
        crc ^= msg[ibytes]
        for i in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc


#msg_bytes = bytes.fromhex("030600000001020406") #set device address of id=3 to id=4, baudrate 9600
#msg_bytes = bytes.fromhex("040600000001020306") #set device address of id=4 to id=3, baudrate 9600

msg_bytes = bytes.fromhex("030600000001020307") #set device address of id=3 to id=3, baudrate 19200
crc = calcModbusCrc(msg_bytes)
crc_bytes = crc.to_bytes(2, byteorder='little') #Modbus CRC has Little Endian order
msg_w_crc_bytes = msg_bytes + crc_bytes

#print(crc_bytes.hex())
#print(msg_w_crc_bytes.hex())
print(''.join("%02X "%c for c in msg_bytes))
print(''.join("%02X "%c for c in crc_bytes))
print(''.join("%02X "%c for c in msg_w_crc_bytes))



