def DisplayStatus(event):
    popup("Still running!", "Workflow Status")

Env.addHotkey(Key.F1, KEY_CTRL, DisplayStatus)
import sys
def StopSikuli(event):
    sys.exit()

Env.addHotkey(Key.F2, KEY_CTRL, StopSikuli)


while (True): 
    if exists (Pattern("1665819006193.png").similar(0.66)):
        click(Pattern("1665819006193.png").similar(0.65))
    type ("r")
    wait(5)




       
     

    
        
        
        
    
        
        
    
    
        
    
    

        
        
    
                
   