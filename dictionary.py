# If in the future I want to expand the game by adding more quests or puzzles,
# I can write new keys to the dictionary.

adventures = {
    "north" : 
        {
            "scene": "Scene: A giant statue of Archimedes stands before you, holding a tablet that reads: 'Find my number to proceed.'\n",
            "question": "I think of a number. I double it and then add 10. The result is 34. What's my number?",
            "answer": 12,
            "correct": "Correct! A door behind the statue opens, revealing a passage. You proceed.\n",
            "wrong": "Wrong! The statue's eyes glow red. You feel compelled to try again."
        },
    "east" : 
        {
            "scene": "A serene pool of water with Fibonacci spiral patterns. At the center, a pedestal emerges with a note.\n",
            "question": "The sequence starts with 0 and 1. Every number after is the sum of the two preceding ones. What's the 5th number in this sequence?",
            "answer" : 3,
            "correct": "Correct! The water parts, allowing you to cross to the other side.\n",
            "wrong": "Wrong! The water churns violently. You realize you need to answer correctly to pass."
        },
    "south" : 
        {
            "scene": "A garden filled with Pythagorean trees. A chalkboard stands with a triangle drawn, one side labeled 5, another labeled 12.\n",
            "question": "I am the length of the hypotenuse. Who am I?",
            "answer" : 13,
            "correct": "Correct! The trees rearrange, creating a path forward.\n",
            "wrong": "Wrong! The trees seem to close in. You must find the right length to proceed."
        },
    "west" : 
        {
            "scene": "A large observatory with celestial bodies depicted on the dome. A voice echoes, 'Align the stars with the right equation.'\n",
            "question": "Which equation is true?\n1. 4^2 + 3^2 = 5^2\n2. 5^2 + 12^2 = 13^2\n3. 8^2 + 15^2 = 17^2",
            "answer" : 2,
            "correct": "Correct! The stars align to form a constellation that points to the exit.\n",
            "wrong": "Wrong! The room darkens momentarily. The voice urges you to try again."
        }        
}