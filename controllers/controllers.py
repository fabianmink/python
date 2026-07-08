

class controller_PI():

    def __init__(self, Kp, Ti, Ts):
        
        self.Ts = Ts
        self.i_val = 0
        
        self.max = float("inf")
        self.min = float("-inf")

        self.Kp = Kp
        if (Ti > 0):
            self.Ki = (Ts*Kp/Ti)
        
        else :
            self.Ki = 0		
            
    def __str__(self):
        return "Kp = " + str(self.Kp)
	
    
    def step(self, ref, act):
        Kp = self.Kp
        Ki = self.Ki
        
        ctrldiff = (ref - act)
	
        p_val = Kp * ctrldiff;
        i_val = 0
        if(Ki != 0):	 
            i_val = Ki * ctrldiff + self.i_val
	
        out = p_val + i_val;	
    
        if(out > self.max):
            out = self.max;
            i_val = self.max - p_val;
		
        if(out < self.min):
            out = self.min;
            i_val = self.min - p_val;

        self.i_val = i_val
   
        return out

