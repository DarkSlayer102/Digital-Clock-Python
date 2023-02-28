from vars.imp import testing,title,background_C,fam,siz,message
from tkinter import *
import time
from tkinter.font import Font

'''
In this project, I have imported all the necessary packages, including time and Tkinter. Tkinter is a built-in library that enables the creation of Graphical User Interfaces (GUIs).
'''


def clocks():
    '''
    This function displays the current time.
    '''
    currentTime = time.gmtime()
    currentTime = f'{currentTime.tm_hour}:{currentTime.tm_min}:{currentTime.tm_sec}'
    clock.config(text=currentTime)
    clock.after(200, clocks)
    '''
This is simply printing out to verify whether it is functioning correctly or not.
    '''
    print(testing)

'''
Here I created a instance of TK  class
'''
window = Tk()
#creating a title 
window.title(title)
#creating background color
window.config(bg=background_C)

font1 = Font(family=fam, size=siz, weight="normal")
#creating a header using Label Widget
header = Label(window, text=message, font=font1, bg="gray", fg="white")
#using grid() to place the header somewhere comfortable in the gui
header.grid(row=1, column=2)
'''
A clock is being constructed using the Label Widget, which exhibits the current time and is positioned using grid. 
'''
clock = Label(window, font=("times", 90, "bold"), bg="blue", fg='white')
clock.grid(row=2, column=2, padx=620, pady=250)

'''

calling the function here
'''
clocks()

'''
running the main window
'''
if __name__ == "__main__":

    window.mainloop()
