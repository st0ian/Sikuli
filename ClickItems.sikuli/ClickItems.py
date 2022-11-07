def DisplayStatus(event):
    popup("Still running!", "Workflow Status")

Env.addHotkey(Key.F1, KEY_CTRL, DisplayStatus)
import sys
def StopSikuli(event):
    sys.exit()

Env.addHotkey(Key.F2, KEY_CTRL, StopSikuli)
counter = 0;
while (True): 
    if (counter == 0):
        counter = 1
        click ("1666103258130.png")
    
    if exists ("1666107388996.png"):
        click("1666107388996.png")
    if not exists ("1666107388996.png"):
        if exists("1666103403827.png"):
            click ("1666103403827.png")

    if exists (Pattern("1666104145400.png").similar(0.45), 2):
        click(Pattern("1666104145400.png").similar(0.45))
        counter =0

      


    
    

       
     

    
        
        
        
    
        
        
    
    
        
    
    

        
        
    
                
   