"""
Created on Tue Jul 14 14:17:17 2020

@author: ganes

Functions (add, check, and display) for tdlist program
"""


def addItem(tdlist, item):
    '''Appends an item to the list
        
       Returns the list'''
    
    item = "[-] " + item.capitalize()
    
    tdlist.append(item)
    
    return tdlist


def checkItem(tdlist, index):
    '''Marks a tasks as completed
     
       Returns the list'''
    
    item = tdlist[index]
    
    del tdlist[index]
    
    item = "[+] " + item[4:]
    
    tdlist.insert(index, item)
    
    return tdlist


def display(tdlist):
    '''Displays list
     
       Returns the list'''
    
    print()
    print("\033[1m\033[4mTo-Do List\033[0m")
    print()
    
    for i in tdlist:
        
        print(i)
    
    print()
    
    