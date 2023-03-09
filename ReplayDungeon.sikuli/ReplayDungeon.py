def DisplayStatus(event):
    popup("Still running!", "Workflow Status")

Env.addHotkey(Key.F1, KEY_CTRL, DisplayStatus)

def DisplayRuns(event):
    popup("{runs}", "Curent Run")

Env.addHotkey(Key.F3, KEY_CTRL, DisplayRuns)

import sys
def StopSikuli(event):
    sys.exit()

Env.addHotkey(Key.F2, KEY_CTRL, StopSikuli)

runs = 1
while (runs < 14): 
    if exists (Pattern("1665819006193.png").similar(0.66),2):
        click(Pattern("1665819006193.png").similar(0.66))
        runs = runs + 1
        
    if exists ("1675268691791.png",2):
        click("1675268691791.png")
        runs = runs + 1

    



       
     

    
        
        
        
    
        
        
    
    
        
    
    

        
        
    
                
   