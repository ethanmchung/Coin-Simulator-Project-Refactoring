import random

guess = input("Do you think it will be heads or tails. Type in 'h' for heads or 't' for tails.")

coin = random.randint(1, 2)
# since there are 2 possibilities (1 and 2), there is a 50/50 percent chance for both,
# just like the odds of landing heads or tails in an actual coin

if coin == 1:
	print("The coin is Heads")
	if guess == 'h':
		print("You were right")
	else:
		print("Wrong guess")
else:
	print("The coin is Tails")
	if guess == 't':
		print("You were right")
	else:
		print("Wrong guess")