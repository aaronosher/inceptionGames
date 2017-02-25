# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:30:22 2017

@author: Andrea
"""
def findbox(x,y):
    one=[1,2,3]
    two=[4,5,6]
    three=[7,8,9]
    i=(x // 98)+1 #row of x(1-9)
    j=(y // 98)+1 #row of y(1-9)
    if i in one:
        bigrow=1
    elif i in two:
        bigrow=2
    elif i in three:
        bigrow=3
    if j in one:
        bigcol=1
    elif j in two:
        bigcol=2
    elif j in three:
        bigcol=3
    if i%3!=0:
        tinyrow=i%3
    else:
        tinyrow=3
    if j%3!=0:
        tinycol=j%3
    else:
        tinycol=3
      
    return (bigrow,bigcol,tinyrow,tinycol)