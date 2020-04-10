# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.33
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that simulates a handheld calculator. Your program should
# process input from the Python console representing buttons that are “pushed,” and then
# output the contents of the screenafter each operation is performed. Minimally, your
# calculator should beable to process the basic arithmetic operations and a reset/clear
# operation.

# Symbol for the clear button
clear = 'c'
# Symbol for off button
off = 'o'
# Symbol for error
error = 'e'
# All operators
operators = ['+', '-', '*', '/', '=']
# All numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_num(str_input):
	"""
	Given a string, str_input, returns a valid number. All invalid
	characters and extra decimals will be ignored.
	"""
	numeric_symbols = ['-', '.']
	# stores temp string
	num_str = ''
	for i in range(len(str_input)):
		if str_input[i].isnumeric() or str_input[i] in numeric_symbols:
			num_str += str_input[i]
		if str_input[i] == '-' or len(num_str) > 0:
			numeric_symbols[0] = ''
		if str_input[i] == '.':
			numeric_symbols[1] = ''
	if len(num_str) == 0:
		return 0
	if '.' in num_str:
		return float(num_str)
	else:
		return int(num_str)

def get_operator(str_input):
	"""
	Given a string, str_input, returns the last valid operator in the
	string or an empty string if no valid operator is found
	"""
	found_operator = False
	operator = ''
	i = len(str_input) - 1
	while i >= 0 and not found_operator:
		if str_input[i] in operators:
			found_operator = True
			operator = str_input[i]
		i -= 1
	return operator

def calculate(operator, new_num, cur_num = 0):
	"""
	Given two numbers, cur_num and new_num, and an operator
	character, operator, calculates the solution. The default value
	for cur_num is 0.
	"""
	solution = 0
	if operator == '+':
		solution = cur_num + new_num
	elif operator == '-':
		solution = cur_num - new_num
	elif operator == '*' :
		solution = cur_num * new_num
	elif operator == '/':
		solution = cur_num / new_num
	elif operator == '=':
		solution = cur_num
	return solution

def main():
	print("Mock Handheld Calculator")
	print("========================")
	clear_symbol = 'c'
	off_symbol = 'o'
	off = False
	cur_num = 0
	new_num = 0
	operator = ''
	while not off:
		str_input = input().lower()
		if len(str_input) == 0:
			pass
		elif str_input[0] == clear_symbol:
			cur_num = 0
		elif str_input[0] == off_symbol:
			off = True
		elif sum([int(char in numbers) for char in str_input]) > 0:
			new_num = get_num(str_input)
			if operator == '':
				cur_num = new_num
				new_num = 0
			elif operator == '=':
				operator = ''
			else:
				cur_num = calculate(operator, new_num, cur_num)
				operator = ''
		else:
			operator = get_operator(str_input)
			while operator == '':
				str_input = input()
				operator = get_operator(str_input)
		if not off:
			print(cur_num)

if __name__ == "__main__":
	main()