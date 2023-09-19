import time
from questions import adventures


def north_adventure():
    time.sleep(0.5)
    print("|------------------|")
    print("| You chose north! |")
    print("|------------------|\n")
    time.sleep(0.5)
    
    print("Scene: A giant statue of Archimedes stands before you,")
    print("holding a tablet that reads: 'Find my number to proceed.'\n")
    time.sleep(0.5)
    
    # Retrieve question and answer from dictionary.
    question = adventures["north"]["question"]
    answer = adventures["north"]["answer"]
    
    print(question)
    player = int(input("-> "))
    
    # Keep asking player for an answer until it is correct.
    while player != answer:
        print("The statue's eyes glow red. You feel compelled to try again.")
        player = int(input("-> "))            
    print("Correct! A door behind the statue opens, revealing a passage. You proceed.\n")
        
    
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
          
          