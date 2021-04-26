import time
import globals

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   globals.label.config(text=time_live) 
   globals.label.after(200, digital_clock)
