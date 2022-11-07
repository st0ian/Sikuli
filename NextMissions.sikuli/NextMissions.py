def DisplayStatus(event):
    popup("Still running!", "Workflow Status")

Env.addHotkey(Key.F1, KEY_CTRL, DisplayStatus)
import sys
def StopSikuli(event):
    sys.exit()

Env.addHotkey(Key.F2, KEY_CTRL, StopSikuli)

while (True): 
    if exists ("1667543498576.png"):
        click("1667543498576.png")
    if exists ("1667545268511.png"):
        click("1667545268511.png")
    if exists ("1665819006193-1.png"):
        click("1665819006193-1.png")   
    if exists (Pattern("1667543779285.png").similar(0.64)):
        click(Pattern("1667543779285.png").similar(0.68))             
    #type ("r")
    #wait(10)
    
    if exists("1666272492409.png"):
        click ("1666272492409.png")    



       
     

    
        
        
        
    
        
        
    
    
        
    
    

        
        
    
                
   