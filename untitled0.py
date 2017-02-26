# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:19:06 2017

@author: Andrea
"""

from appJar import gui

    # the title of the button will be received as a parameter
def press(btn):
    print("("+str(i)+", "+str(j)+")")
    #app.setButton(str(i)+str(j), 'x')
            

app=gui()
# 3 buttons, each calling the same function

for i in range(1,10):
    for j in range(1,10):
        app.addButton(str(i)+str(j), press,i,j)
            
                  
app.go()