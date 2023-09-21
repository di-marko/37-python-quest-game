import time
from dictionary import adventures, win


# Timer to set a pause before printing scene, questions. 
def time_sleep():
    time.sleep(0.5)
    
# Display scene, question. Wait for user's input and check for answers.
def q_and_a(scene, question, answer, correct, wrong):
    print(scene)
    time_sleep()   
    
    print(question)
    
    # Keep asking player for an answer until it is correct.
    # Check for the correct data type player inputs.
    while True:
        try:
           player = int(input("-> ")) 
           
           if player == answer:
               break
           else: 
               print(wrong)
        except ValueError:
            print("Try entering a number.")
    print(correct)
    
def winner():
    player_win = win["message"]
    print(player_win)
    
def adventure(direction):
    scene = adventures[direction]["scene"]
    question = adventures[direction]["question"]
    answer = adventures[direction]["answer"]
    correct = adventures[direction]["correct"]
    wrong = adventures[direction]["wrong"]
    
    time_sleep()
    print(f"|------------------|")
    print(f"| You chose {direction}! |")
    print(f"|------------------|\n")
    time_sleep()
    
    q_and_a(scene, question, answer, correct, wrong)
    time_sleep()
     

def north_adventure():
    adventure("north")
    winner()
    exit()
    
def east_adventure():
    adventure("east")
    winner()
    exit()
    
def south_adventure():
    adventure("south")
    winner()
    exit()
    
def west_adventure():
    adventure("west")
    winner()
    exit()
          
          