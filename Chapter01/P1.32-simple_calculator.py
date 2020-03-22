# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.32
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that can simulate a simple calculator, using the console as the
# exclusive input and output device. That is, each input to the calculator, be it a
# number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate
# line. After each such input, you should output to the Python console what would be
# displayed on your calculator.

input_text = "Input:  "
output_text = "Output: "

def get_num():
	"""
	Extracts a number from a given input; if the input is not valid, continues
	to ask the user for a valid input
	"""
	n = None
	bad_input = True
	while bad_input:
		user_input = input("{}".format(input_text))
		try:
			n = int(user_input)
			bad_input = False
		except:
			try:
				n = float(user_input)
				bad_input = False
			except:
				print("{}ERROR".format(output_text))
	return n
	
def calculate(num1, operator, num2):
	"""
	Calculates +, -, *, or / of num1 and num2 depending on operator
	"""
	if operator == '+':
		return num1 + num2
	elif operator == '-':
		return num1 - num2
	elif operator == '*':
		return num1 * num2
	elif operator == '/':
		return num1 / num2
	else:
		raise ValueError("Invalid input")

def get_operator():
	"""
	Extracts valid operator from a given input; if the input is not valid,
	continues to ask the user for a valid input
	"""
	operators = ['+', '-', '*', '/', '=']
	operator = None
	bad_input = True
	while bad_input:
		operator = input("{}".format(input_text))
		if operator in operators:
			bad_input = False
		else:
			print("{}ERROR".format(output_text))
	return operator

def main():
	print("This program simulates a simple calculator. Type each number and operator on",
	"a separate line.")
	num1 = get_num()
	num2 = None
	operator = None
	while operator != '=':
		operator = get_operator()
		if operator == '=':
			print("{}{}".format(output_text, num1))
		else:
			num2 = get_num()
			num1 = calculate(num1, operator, num2)
			print("{}{}".format(output_text, num1))
			num2 = None
			operator = None

if __name__ == "__main__":
	main()