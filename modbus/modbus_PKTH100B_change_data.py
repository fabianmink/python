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

#https://stackoverflow.com/questions/69369408/calculating-crc16-in-python-for-modbus

def modbusCrc(msg:str) -> int:
    crc = 0xFFFF
    for n in range(len(msg)):
        crc ^= msg[n]
        for i in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc


#msg = bytes.fromhex("030600000001020406") #set device address of id=3 to id=4, baudrate 9600
#msg = bytes.fromhex("040600000001020306") #set device address of id=4 to id=3, baudrate 9600

msg = bytes.fromhex("030600000001020307") #set device address of id=3 to id=3, baudrate 19200

crc = modbusCrc(msg)
print("0x%04X"%(crc)) 

#On Modbus, bytes have to be added in this order
ba = crc.to_bytes(2, byteorder='little')
print("%02X %02X"%(ba[0], ba[1]))

