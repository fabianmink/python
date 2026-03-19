# -*- coding: utf-8 -*-
"""
RK4-Solver for scipy.integrate.solve_ivp

@author: Fabian Mink
"""

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
        #print("__init__ of myrk4")


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
