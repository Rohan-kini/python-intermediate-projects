from unicodedata import name
import pyautogui
import time
import tkinter as tk   

def screenshot():
    name=time.time()
    name='C:/Users/rohan/OneDrive/Desktop/python.rohan/pythonsmallprojs/{}.png'.format(name)
    img=pyautogui.screenshot()
    img.save(name)
    img.show()


root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,text='Take Screenshor',command=screenshot)
button.pack(side=tk.LEFT)                                  

close=tk.Button(frame,text='Quit',command=quit)
close.pack(side=tk.RIGHT)

root.mainloop()