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

def get_num(str_input, cur_pos = 0):
	"""
	Given a string, str_input, and current position of the string, cur_pos, returns
	a valid number, n, and the updated position in the string, i. If there is an
	invalid input before an operator or a clear/off button input, the function will
	halt any further reads and will return the error symbol.
	"""
	numeric_symbols = ['-', '.']
	i = cur_pos
	while str_input[i] in numeric_symbols or 