import time

adventures = {
    "north" : ["I think of a number. I double it and then add 10. The result is 34. What's my number?", 12],
}

def north_adventure():
    time.sleep(0.5)
    print("|------------------|")
    print("| You chose north! |")
    print("|------------------|\n")
    time.sleep(0.5)
    
    print("Scene: A giant statue of Archimedes stands before you,")
    print("holding a tablet that reads: 'Find my number to proceed.'\n")
    time.sleep(0.5)
    
    print(adventures["north"][0])
    player = int(input(""))
    
    while player != adventures["north"][0][0]:
        if player == 12:
            print("Correct! A door behind the statue opens, revealing a passage. You proceed.")
            break
        else:
            print("The statue's eyes glow red. You feel compelled to try again.\n")
            player = int(input("-> "))
        
    
def east_adventure():
    time.sleep(1)
    print("|-----------------|")
    print("| You chose east! |")
    print("|-----------------|\n")
    time.sleep(1)
    
def south_adventure():
    time.sleep(1)
    print("|------------------|")
    print("| You chose south! |")
    print("|------------------|\n")
    time.sleep(1)
    
def west_adventure():
    time.sleep(1)
    print("|-----------------|")
    print("| You chose west! |")
    print("|-----------------|\n")
    time.sleep(1)
          
          