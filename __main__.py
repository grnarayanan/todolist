"""
Created on Tue Jul 14 14:38:20 2020

@author: ganes

tdlist program that simulates a daily to-do list
"""


from .utils import addItem, checkItem, display
from datetime import datetime

def main():
    '''To do list program that tracks daily tasks
    
       Allows users to add and complete tasks and presents
       a daily summary.'''
    
    tdlist = []
    
    # opens and reads time from timestamp file
    timestamp = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\timestamp.txt','r')
    
    clear = timestamp.readline()
    
    timestamp.close()
    
    # clears list file if new day and writes new time to timestamp
    if ((int(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")[6:10]) > 
        (int(clear[6:10]))) and 
        (int(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")[12:14]) >= 5)):
        
        listfile = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\todolist.txt','w')
        listfile.close()
        timestamp = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\timestamp.txt','w')
        timestamp.write(datetime.now().strftime("%d/%m/%Y, 06:00:00"))
    
    elif ((int(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")[3:5]) > 
          (int(clear[3:5]))) and 
          (int(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")[12:14]) >= 5)):
        
        listfile = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\todolist.txt','w')
        listfile.close()
        timestamp = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\timestamp.txt','w')
        timestamp.write(datetime.now().strftime("%d/%m/%Y, 06:00:00"))
    
    elif ((int(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")[0:2]) > 
          (int(clear[0:2]))) and 
          (int(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")[12:14]) >= 5)):   
        
        # counts completed tasks from previous day, if applicable
        if (int(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")[0:2]) == 
           (int(clear[0:2]) + 1)):
            
            cklist = []
            finished = 0
            total = 0
                
            listfile = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\todolist.txt','r')
            
            for line in listfile:
            
                cklist.append(line.strip())
        
            listfile.close()
                
            for task in cklist:
                
                if (task[1] == "+"):
                    
                    finished += 1
                
                total += 1
            
            print()
            
            if ((finished == total) and (total > 0)):
                
                print("Yesterday you finished all your tasks!")
            
            else:
                
                print("Yesterday you finished " + str(finished) + " out of " + 
                      str(total) + " tasks.")
        
            print()
        
        listfile = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\todolist.txt','w')
        listfile.close()
        timestamp = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\timestamp.txt','w')
        timestamp.write(datetime.now().strftime("%d/%m/%Y, 06:00:00"))
    
    # displays todolist to user
    listfile = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\todolist.txt','r')
    
    for line in listfile:
        
        tdlist.append(line.strip())
    
    listfile.close()
    
    display(tdlist)
    
    ans = "i"
    
    # todolist operation on tdlist
    while (ans.strip().lower() != "e"):
        
        ans = None
        
        # asks user for command
        while (type(ans) != str):
            
            try:
            
                ans = str(input("What would you like to do? "))
        
            except: 
                
                ans = "error"
        
        # appends new item to list and displays
        if (ans.strip().lower() == "a"):
            
            task = input("Add a new task: ")
            
            if (task.strip().lower() != "e"):
                
                tdlist = addItem(tdlist, task)
            
                print()
                display(tdlist)
        
        # marks a task as completed and displays list
        if (ans.strip().lower() == "c"):
            
            try:
                
                task = int(input("Completed task: "))
            
            except:
                
                print("Error, invalid entry.")
                task = 1191
            
            if (task <= 0):
                
                task = 1
            
            if (task > len(tdlist) and task != 1191):
                
                task = len(tdlist)
            
            # 1191 is the escape clause
            if (task != 1191):
            
                tdlist = checkItem(tdlist, task - 1)
            
                print()
                display(tdlist)
        
        if (ans.strip().lower() != "a" and ans.strip().lower() != "c" and 
            ans.strip().lower() != "e"):
            
            print("Error, invalid entry.")
    
    # writes tasks from list to file
    listfile = open('C:\\Users\\ganes\\Documents\\Personal\\Projects\\todolist\\essentials\\todolist.txt','w')
    
    for i in tdlist:
        
        listfile.write(i + "\n")
    
    listfile.close()
    
    
if __name__ == "__main__":
    main()