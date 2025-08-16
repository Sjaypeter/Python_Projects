#This app just shows how to work with loops
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1): #This indexes the time in a reversed form 
    seconds = x % 60 #To convert time to seconds
    minutes = int(x/60) % 60 #Convert to minutes
    hours = int(x/3600) #Convert to hours 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("TIME'S UP!")
    
    