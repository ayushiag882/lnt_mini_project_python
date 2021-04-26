from digital_clock import *

import globals 
 
if _name_ == "_main_": 
   globals.initialize() 

globals.app_window.title("Digital Clock") 
globals.app_window.geometry("420x150") 
globals.app_window.resizable(1,1)

globals.label.grid(row=0, column=1)

digital_clock()
globals.app_window.mainloop()
