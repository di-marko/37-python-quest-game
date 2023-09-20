import time
from questions import adventures

def time_sleep():
    time.sleep(0.5)

def north_adventure():
    # Retrieve question and answer from dictionary.
    scene = adventures["north"]["scene"]
    question = adventures["north"]["question"]
    answer = adventures["north"]["answer"]
    wrong = adventures["north"]["wrong"]
    correct = adventures["north"]["correct"]
    
    time_sleep()
    print("|------------------|")
    print("| You chose north! |")
    print("|------------------|\n")
    time_sleep()
    
    print(scene)
    time_sleep()   
    
    print(question)
    player = int(input("-> "))
    
    # Keep asking player for an answer until it is correct.
    while player != answer:
        print(wrong)
        player = int(input("-> "))            
    print(correct)
        
    
def east_adventure():
    time_sleep()
    print("|-----------------|")
    print("| You chose east! |")
    print("|-----------------|\n")
    time_sleep()
    
def south_adventure():
    time_sleep()
    print("|------------------|")
    print("| You chose south! |")
    print("|------------------|\n")
    time_sleep()
    
def west_adventure():
    time_sleep()
    print("|-----------------|")
    print("| You chose west! |")
    print("|-----------------|\n")
    time_sleep()
          
          