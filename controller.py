from sqdata.sqlite import *

def ordering():
    drinkchoice = input("Hi, what drink would you like today?  ")
    size = input("what size would you like? Large, Medium or small?  ")
    name = input("May i have your name?   " )
    order =  [drinkchoice, size, name]
    return insertdata(order)

