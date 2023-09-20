import time
from questions import adventures

def time_sleep():
    time.sleep(0.5)
    
# Display scene, question. Wait for user's input and check for answers.
def q_and_a(scene, question, answer, correct, wrong):
    print(scene)
    time_sleep()   
    
    print(question)
    player = int(input("-> "))
    
    # Keep asking player for an answer until it is correct.
    while player != answer:
        print(wrong)
        player = int(input("-> "))            
    print(correct)

def north_adventure():
    # Retrieve scene, question and answers from dictionary.
    scene = adventures["north"]["scene"]
    question = adventures["north"]["question"]
    answer = adventures["north"]["answer"]
    correct = adventures["north"]["correct"]
    wrong = adventures["north"]["wrong"]
    
    time_sleep()
    print("|------------------|")
    print("| You chose north! |")
    print("|------------------|\n")
    time_sleep()
    
    q_and_a(scene, question, answer, correct, wrong)        
    
def east_adventure():
    # Retrieve scene, question and answers from dictionary.
    scene = adventures["east"]["scene"]
    question = adventures["east"]["question"]
    answer = adventures["east"]["answer"]
    correct = adventures["east"]["correct"]
    wrong = adventures["east"]["wrong"]
    
    time_sleep()
    print("|-----------------|")
    print("| You chose east! |")
    print("|-----------------|\n")
    time_sleep()
    
    q_and_a(scene, question, answer, correct, wrong)
    
def south_adventure():
    # Retrieve scene, question and answers from dictionary.
    scene = adventures["south"]["scene"]
    question = adventures["south"]["question"]
    answer = adventures["south"]["answer"]
    correct = adventures["south"]["correct"]
    wrong = adventures["south"]["wrong"]
    
    time_sleep()
    print("|------------------|")
    print("| You chose south! |")
    print("|------------------|\n")
    time_sleep()
    
    q_and_a(scene, question, answer, correct, wrong)
    
def west_adventure():
    # Retrieve scene, question and answers from dictionary.
    scene = adventures["west"]["scene"]
    question = adventures["west"]["question"]
    answer = adventures["west"]["answer"]
    correct = adventures["west"]["correct"]
    wrong = adventures["west"]["wrong"]
    
    time_sleep()
    print("|-----------------|")
    print("| You chose west! |")
    print("|-----------------|\n")
    time_sleep()
    
    q_and_a(scene, question, answer, correct, wrong)
          
          