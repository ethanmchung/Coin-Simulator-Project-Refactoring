import random

coin = random.randint(1, 2)
# since there are 2 possibilities (1 and 2), there is a 50/50 percent chance for both,
# just like the odds of landing heads or tails in an actual coin

if coin == 1:
	print("The coin is Heads")
else:
	print("The coin is Tails")
	
