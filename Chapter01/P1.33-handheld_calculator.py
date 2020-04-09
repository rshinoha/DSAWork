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
	if '.' in num_str:
		return float(num_str)
	else:
		return int(num_str)

tempStr = input('Enter a number: ')
tempNum = get_num(tempStr)
print(tempNum)
print(type(tempNum))