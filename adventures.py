import time
from dictionary import adventures, winner_msg


# Timer to set a pause before printing scene, questions. 
def time_sleep():
    time.sleep(0.5)
   
# Display the winning message. 
def winner_message():
    player_win = winner_msg["message"]
    print(player_win)   
     
class Adventure:
    def __init__(self, direction):
        self.direction = direction
        self.scene = adventures[direction]["scene"]
        self.question = adventures[direction]["question"]
        self.answer = adventures[direction]["answer"]
        self.correct = adventures[direction]["correct"]
        self.wrong = adventures[direction]["wrong"]
        
    def display_scene(self):
        time_sleep()
        print(f"|------------------|")
        print(f"| You chose {self.direction}! |")
        print(f"|------------------|\n")
        time_sleep()    
        print(self.scene)
        time_sleep()       

    # Display scene, question. Wait for user's input and check for answers.
    def q_and_a(self):
        print(self.question)
        time_sleep()        
        # Keep asking player for an answer until it is correct.
        # Check for the correct data type player inputs.
        while True:
            try:
                player = int(input("-> "))                
                if player == self.answer:
                    break
                else: 
                    print(self.wrong)
            except ValueError:
                print("Try entering a number.")
        print(self.correct)


def north_adventure():
    north_journey = Adventure("north")
    north_journey.display_scene()
    north_journey.q_and_a()
    winner_message()
    exit()
    
def east_adventure():
    east_journey = Adventure("east")
    east_journey.display_scene()
    east_journey.q_and_a()
    winner_message()
    exit()
    
def south_adventure():
    south_journey = Adventure("south")
    south_journey.display_scene()
    south_journey.q_and_a()
    winner_message()
    exit()
    
def west_adventure():
    west_journey = Adventure("west")
    west_journey.display_scene()
    west_journey.q_and_a()
    winner_message()
    exit()
          
          