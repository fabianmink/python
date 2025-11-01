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

from scipy.integrate import OdeSolver, DenseOutput
from warnings import warn


def rk4_step(f, h, t_k, x_k):
    k1 = f(t_k, x_k)
    k2 = f(t_k + 0.5 * h, x_k + 0.5 * h * k1)
    k3 = f(t_k + 0.5 * h, x_k + 0.5 * h * k2)
    k4 = f(t_k + 1.0 * h, x_k + 1.0 * h * k3)
    x_k = x_k + h * (k1 + 2*(k2 + k3 ) + k4) / 6
    t_k = t_k + h
    return t_k, x_k


def warn_extraneous(extraneous):
    if extraneous:
        warn("The following arguments are unused in RK4: "
             f"{', '.join(f'`{x}`' for x in extraneous)}.",
             stacklevel=3)

class rk4Solver(OdeSolver):

    def __init__(self, fun, t0, y0, t_bound, vectorized=False,
                 stepsize=None, **extraneous):
        
        warn_extraneous(extraneous)
        
        super().__init__(fun, t0, y0, t_bound, vectorized,
                         support_complex=False)
        
        #TODO: Validate stepsize
        #if stepsize is None:
            #TODO: error
        # .. other validations ...
            
        self.stepsize = stepsize    
            
        #DEBUGGING INFO
        print("__init__ of myrk4")


    #A solver must implement a private method _step_impl(self) 
    #which propagates a solver one step further. 
    #It must return tuple (success, message), where success is a 
    #boolean indicating whether a step was successful, 
    #and message is a string containing description of a failure
    #if a step failed or None otherwise.
    def _step_impl(self):
        t = self.t
        y = self.y

        #t_new = t + self.stepsize
        #y_new = y #dummy for testing, no change of y
        t_new, y_new = rk4_step(self.fun, self.stepsize, t, y)

        self.t = t_new
        self.y = y_new
       
        #DEBUGGING INFO
        #print("_step_impl of myrk4" )
        #print("stepsize: " + str(self.step_size) )
        #print("t:" + str(self.t) + " t_old:" + str(self.t_old))
        #print("y: " + str(self.y) )
        #print("n: " + str(self.n) )
        #print("status:" + str(self.status))
        #print("direction:" + str(self.direction))
        #print("")
        
        return True, None

    #A solver must implement a private method _dense_output_impl(self),
    #which returns a DenseOutput object covering the last successful step.
    def _dense_output_impl(self):
        #DEBUGGING INFO
        print("_dense_output_impl of myrk4" )
        #TODO: Keine Ahnung ob das sinnvoll implementiert ist; die Funktion wird offensichtlich
        #durch solve_ivp nie aufgerufen
        return DenseOutput(self.t_old, self.t)
