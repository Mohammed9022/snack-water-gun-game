import random

def gameWin(computer, your_turn):
	if computer == your_turn:
		return None
	elif computer == "s":
		if your_turn == "w":
			return False
		elif your_turn == "g":
			return True
	
	elif computer == "w":
		if your_turn == "g":
			return False
		elif your_turn == "s":
			return True

	elif computer == "g":
		if your_turn == "s":
			return False
		elif your_turn == "w":
			return True
			

print("Computer Turn: Snack(s) Water(w) Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
	computer = "s"
elif randNo == 2:
	computer = "w"
elif randNo == 3:
	computer = "g"


your_turn = input("Your Turn3: Snack(s) Water(w) Gun(g)?")

a = gameWin(computer, your_turn)

print(f"Computer choose {computer}")
print(f"You choose {your_turn}")

if a == None:
	print("The game is a tie!")
elif a:
	print("You Win!")
else:
	print("You lose!")