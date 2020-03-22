# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.31
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that can “make change.” Your program should take two numbers as
# input, one that is a monetary amount charged and the other that is a monetary amount
# given. It should then return the number of each kind of bill and coin to give back as
# change for the difference between the amount given and the amount charged. The values
# assigned to the bills and coins can be based on the monetary system of any current or
# former government. Try to design your program so that it returns as few bills and coins
# as possible.

def make_change(paid, owed, bills_coins):
	"""
	Given the amount paid and amount owned, returns the minimum bills and coins required
	in giving back change in the currency of interest as a dictionary.
	
	Variables
	- paid: amount of money paid by customer
	- owed: actual balance of purchase
	- bills_coins: value of bills and coins for given currency
	"""
	ordered_bills_coins = bills_coins
	ordered_bills_coins.sort(reverse = True)
	# Amount of change owed
	change = paid - owed
	if change > 0:
		# Whole number amount of change owed (for when currencies have decimals)
		whole = int(change // 1)
		# Amount of change required that is less than 1
		decimal = change - whole
		# Dictionary of bills and coins required
		bc_dict = {key: 0 for key in ordered_bills_coins}
		
		for bc in bc_dict:
			# If the bill or coin has a whole number value, use whole number division and mod
			if int(bc // 1) >= 1:
				bc_dict[bc] = int(whole // bc)
				whole = whole % bc
			else:
				count_bc = 0
				while decimal - bc > 0:
					decimal -= bc
					count_bc += 1
				bc_dict[bc] = count_bc
		return bc_dict
	else:
		raise ValueError("Amount of change must be greater than 0")

def print_change(bc_dict, bills_coins, currency):
	for key, value in bc_dict.items():
		print("{}{}: {}".format(currency, key, value))
	
def main():
	# Default: using American dollars
	bills_coins = [50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
	currency = "$"
	
	paid = float(input("Enter amount paid: "))
	owed = float(input("Enter amount owed: "))
	dollar = str(input("Are we working with dollars?[y/n]: "))
	if dollar[0].lower() != 'y':
		currency = str(input("Input the name or symbol associated with the currency: "))
		bills_coins = [float(x) for x in input("Enter the list of bills and coins in your currency: ").split()]
	
	bc_dict = make_change(paid, owed, bills_coins)
	
	print("You owe the customer the following:")
	print("===================================")
	print_change(bc_dict, bills_coins, currency)
	
if __name__ == "__main__":
	main()