print('''
************************************************************************
            ^
          /   \
          \   /
          |   |
          |   |
          | 0 |
         // ||\\
        (( // ||
        \\))  \\
       //||    ))
       ( ))   //
        //   ((

                 _     _ 
                (_)   | |
 ___  __ _ _   _ _  __| |
/ __|/ _` | | | | |/ _` |
\__ \ (_| | |_| | | (_| |
|___/\__, |\__,_|_|\__,_|
        | |              

                                             __ _  __ _ _ __ ___   ___  ___ 
                                            / _` |/ _` | '_ ` _ \ / _ \/ __|
                                           | (_| | (_| | | | | | |  __/\__ \
                                            \__, |\__,_|_| |_| |_|\___||___/
                                             __/ |                          
                                            |___/                    
 
************************************************************************
''')
print("Welcome to Squid Games.")
print("Your mission is to play games and survive at any cost to win $45.6 billion Korean Won.") 

choice1 = input('We\'re at the Squid Games. Which team do you want to select? Type "left" or "right".\n').lower()

if choice1 == "left":
 choice2 = input('There is a small island in the middle of the lake. You\'ve a choice to stay or swim back to safety. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
 if choice2 == "wait":
   choice3 = input("You were ubered to the island by the Front Man. There is a playground with 3 doors with different shapes in it. One circle , one star and one umbrella. Which shape do you want to choose?\n").lower()
   if choice3 == "circle":
      print("You were almost done cutting off the edges of the circle in the honeycomb but it broke a little bit so you were eliminated")
   elif choice3 == "star":
      print(f"You were able to manage to cut off the edges of the star in the honeycomb. Congratulations You have won a cashprize of ${45.6} billion Korean Won")
   elif choice3 == "umbrella" :
      print(f"You were given the Shape of Death and you are not as smart as Player {456} so you were eliminated.")
   else:
     print("You tried to get away from games with quota or by feminazi card so you were eliminated")
 else:
    print("You tried to swam away but were killed by the Front Man\'s workers lol ")
else:
 print("You are safe at home lol xdd")