def DisplayStatus(event):
    popup("Still running!", "Workflow Status")

Env.addHotkey(Key.F1, KEY_CTRL, DisplayStatus)
import sys
def StopSikuli(event):
    sys.exit()

Env.addHotkey(Key.F2, KEY_CTRL, StopSikuli)

runs = 0
print("Starting runs", runs)

while (runs <=2):  
    
    if exists ("1675292826411.png",2):
        wait(1)
        click("1675292826411.png")
        runs = runs + 1
    
    if exists (Pattern("1666465664947.png").similar(0.54), 2):
        click (Pattern("1666465664947.png").similar(0.54))
        if exists (Pattern("1666465718857.png").similar(0.50),2):
            
            click (Pattern("1666465718857.png").similar(0.50))
            wait (2)
            click (Pattern("1666465718857.png").similar(0.50))   
            
print("Total runs", runs)

    



       
     

    
        
        
        
    
        
        
    
    
        
    
    

        
        
    
                
   