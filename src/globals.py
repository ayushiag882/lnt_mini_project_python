import tkinter as tk

from tkinter import Label, Tk

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

def initialize():
    global label
    global app_window
    app_window = Tk() 
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
