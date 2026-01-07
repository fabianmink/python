# -*- coding: utf-8 -*-

#   Copyright (c) 2025 Fabian Mink <fabian.mink@iem.thm.de>
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
# pip install python-vxi11
# pip install standard-xdrlib

import vxi11
import struct
import numpy as np 
from matplotlib import pyplot as plt


#Agilent Technologies,33220A
instrFgIpAddr = "192.168.10.11"   #IP-Address of Instrument
funGenAgilent =  vxi11.Instrument(instrFgIpAddr)
print(funGenAgilent.ask("*IDN?"))
print(funGenAgilent.ask("APPL?"))


funGenAgilent.write("APPL:SIN +1.0e3,+1.0,0.0")  #also enables output
#funGenAgilent.write("APPL:PULS +10.0e3,+1.0,0.0")  #also enables output, no pulse width setting possible!!

#Following steps do not enable output
#funGenAgilent.write("FUNC SIN") 
#funGenAgilent.write("FREQ 4e3") 
#funGenAgilent.write("VOLT 1.0")
#funGenAgilent.write("VOLT:OFFS 0.0")

#Following steps do not enable output
#funGenAgilent.write("FUNC PULS") 
#funGenAgilent.write("FREQ 1e3") 
#funGenAgilent.write("VOLT 1.0")
#funGenAgilent.write("VOLT:OFFS 0.5")
#funGenAgilent.write("FUNC:PULS:WIDT 0.2e-3")  #Pulswidth / s
#funGenAgilent.write("FUNC:PULS:DCYC 40")      #Duty Cycle / %

#Output off / on 
#funGenAgilent.write("OUTP OFF")
#funGenAgilent.write("OUTP ON")


#Siglent Technologies,SDS1104X-E
instrScopeIpAddr = "192.168.10.10"   #IP-Address of Instrument
dScopeSiglent =  vxi11.Instrument(instrScopeIpAddr)
print(dScopeSiglent.ask("*IDN?"))

#Channel
dScopeSiglent.write("C1:VDIV 5.0")
dScopeSiglent.write("C1:TRA ON")
dScopeSiglent.write("C2:VDIV 1.0")
dScopeSiglent.write("C2:TRA ON")
dScopeSiglent.write("C3:TRA OFF")
dScopeSiglent.write("C4:TRA OFF")

print(dScopeSiglent.ask("C1:VDIV?"))
print(dScopeSiglent.ask("C1:OFST?"))
print(dScopeSiglent.ask("C1:ATTN?"))
print(dScopeSiglent.ask("C1:UNIT?"))
print(dScopeSiglent.ask("C1:CPL?"))
print(dScopeSiglent.ask("C1:TRA?"))

#Timebase
dScopeSiglent.write("TDIV 2e-4")
print(dScopeSiglent.ask("TDIV?"))
trdl = dScopeSiglent.ask("TRDL?")
print(trdl)
Td = float((trdl.split()[1]).split("S")[0])

#Trigger
dScopeSiglent.write("C1:TRLV 0.0")
dScopeSiglent.write("C1:TRSL POS")
print(dScopeSiglent.ask("TRCP?"))
print(dScopeSiglent.ask("TRLV?"))
print(dScopeSiglent.ask("TRSE?"))
#print(dScopeSiglent.ask("TRSL?")) #Does not work

#Sampling rate
sara = dScopeSiglent.ask("SARA?")
print(sara)
fs = float((sara.split()[1]).split("S")[0])

#print(dScopeSiglent.ask("SANU?")) #Does not work


#Setup Waveform
dScopeSiglent.write("WFSU SP,0,NP,1000000,FP,0")

#Query waveform
#Raw query must be used, as return contain bytes that can not be utf-8 decoded
raw_query_bytes = "C1:WF? DAT2".encode("utf-8") 
response_bytes = dScopeSiglent.ask_raw(raw_query_bytes)
wf_bytes = response_bytes[22:-2]  #remove header and end
wf = []
for value in struct.iter_unpack("b", wf_bytes): #interprete each byte as b="signed char"
    wf.append(value[0])
    
u_ch1 = np.array(wf) / 128.0 * 5.0;  #scale to 5V/div
    
n_ch1 = len(u_ch1)
t = np.linspace(-1/fs*n_ch1/2, 1/fs*n_ch1/2, n_ch1) - Td  

plt.plot(t*1000, wf, 'r-', lw=1)  
ax = plt.gca();
ax.set_xlabel("t/ms")
ax.set_ylabel("u/V")
ax.grid()
 
  





