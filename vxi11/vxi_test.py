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

instrScopeIpAddr = "192.168.10.10"   #IP-Address of Instrument
dScopeSiglent =  vxi11.Instrument(instrScopeIpAddr)

instrFgIpAddr = "192.168.10.11"   #IP-Address of Instrument
funGenAgilent =  vxi11.Instrument(instrFgIpAddr)

print(dScopeSiglent.ask("*IDN?"))
print(funGenAgilent.ask("*IDN?"))
#print(funGenAgilent.ask("APPL?"))

funGenAgilent.write("OUTP OFF")
funGenAgilent.write("OUTP ON")

funGenAgilent.write("APPL:SIN +1.0e3,+1.0,0.0")  #also enables output
funGenAgilent.write("APPL:PULS +10.0e3,+1.0,0.0")  #also enables output, no pulse width setting possible!!

#Following steps do not enable output
funGenAgilent.write("FUNC SIN") 
funGenAgilent.write("FREQ 4e3") 
funGenAgilent.write("VOLT 1.0")
funGenAgilent.write("VOLT:OFFS 0.0")

#Following steps do not enable output
funGenAgilent.write("FUNC PULS") 
funGenAgilent.write("FREQ 1e3") 
funGenAgilent.write("VOLT 1.0")
funGenAgilent.write("VOLT:OFFS 0.5")
#funGenAgilent.write("FUNC:PULS:WIDT 0.2e-3")  #Pulswidth / s
funGenAgilent.write("FUNC:PULS:DCYC 40")      #Duty Cycle / %



