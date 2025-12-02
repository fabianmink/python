# -*- coding: utf-8 -*-

#   Copyright (c) 2025 Fabian Mink <fabian.mink@gmx.de>
#
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this
#      list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#   ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import pymodbus.client as ModbusClient


mbclient = ModbusClient.ModbusSerialClient( "COM5", baudrate=9600, bytesize=8, parity="N", stopbits=1)
#mbclient = ModbusClient.ModbusSerialClient( "COM5", baudrate=19200, bytesize=8, parity="N", stopbits=1)

mbclient.connect()  

try:    
    # *** Test for R414A01 Temperatur /  Humidity Module ***
    
    #mbclient.write_register(2, 5, device_id=1) #write device id of device 1 to "5"
    #result = mbclient.read_holding_registers(0, count=4, device_id=5) #PyModbus V.4.0
    #Modbus-Request:  05 03 00 00 00 04 45 8D
    
    result = mbclient.read_holding_registers(0, count=2, device_id=5) #PyModbus V.4.0
    #Modbus-Request:  05 03 00 00 00 02 C5 8F
    regs = result.registers
    #0 = temp
    #1 = humid
    #2 = deviceId
    #3 = baudrate (0=1200, 1=2400, 2=4800, 3=9600, 4=19200)
    
    
    # *** Test for PKTH100B Temperatur /  Humidity Module ***
    #writing of registers does not work, as device uses non-standard modbus functionality
        
    #result = mbclient.read_holding_registers(0, count=2, device_id=3) 
    #regs = result.registers
    #0 = temp
    #1 = humid
    
    print(regs)
    
except Exception as e:
    print(e)
    

mbclient.close()    