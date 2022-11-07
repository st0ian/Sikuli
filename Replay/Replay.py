def DisplayStatus(event):
    popup("Still running!", "Workflow Status")

Env.addHotkey(Key.F1, KEY_CTRL, DisplayStatus)
import sys
def StopSikuli(event):
    sys.exit()

Env.addHotkey(Key.F2, KEY_CTRL, StopSikuli)

while (True): 
    if exists ("1665819006193.png"):
        click("1665819006193.png")
    if exists (Pattern("1666465664947.png").similar(0.56), 1):
        click (Pattern("1666465664947.png").similar(0.56))
        if exists (Pattern("1666465718857.png").similar(0.50),2):
            
            click (Pattern("1666465718857.png").similar(0.50))
            wait (2)
            click (Pattern("1666465718857.png").similar(0.50))
    type ("r")
    wait(5)
    
    if exists ("1665693026327.png", 1):
       
        type(Key.ESC)
        wait (10)
    if exists("1666272492409.png"):
        click ("1666272492409.png")    



       
     

    
        
        
        
    
        
        
    
    
        
    
    

        
        
    
                
   