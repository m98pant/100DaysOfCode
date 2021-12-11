rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the First Reunion of the B99 Precint\'s OG Crew")
print("I am Commissioner Raymond Holt and I challenge you to play a game of RPS with me")
game_images = [rock, paper, scissors]
import random
user_choice = int(input("What do you choose Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number and then said BONE!, Dismissed")
else:
  print(game_images[user_choice])
  robot_choice = random.randint(0, 2)
  print(f"Meep Morp Zeep Robot choose:")
  print(game_images[robot_choice])

  if user_choice == 0 and robot_choice == 2:
   print("You win. Oh, I\'ve caused a problem. I think I am getting a text message. Bloop. Ah, there it is. Bye!!")
  elif robot_choice == 0 and user_choice == 2:
    print("Hot Damn! Robot wins You lose.")
  elif robot_choice > user_choice:
    print("You Lose. No ... From Now On, Call Me ... Velvet Thunder!!!")
  elif user_choice > robot_choice:
   print('You Won but don\'t worry Because No One Will Ever Believe You. ')
  elif user_choice == robot_choice:
    print(" It\'s a Draw. Everything Is Garbage. Never Love Anything")