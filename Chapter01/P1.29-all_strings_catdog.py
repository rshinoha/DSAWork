# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.29
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that outputs all possible strings formed by using the characters
# c , a , t , d , o , and g exactly once.
# Note: I referred to this Stack Exchange answer https://stackoverflow.com/a/53917934 for
# this function.

def all_strings(arr, i, length):
	"""
	Returns all possible strings using each letter in arr once
	
	Variables:
	- arr = array containing all characters of interest
	- i = current position in string 
	"""
	# If we can't swap any more letters, print the final string
	if i == length:
		print(''.join(arr))
	else:
		for j in range(i, length):
			# Swap letters from two positions
			arr[i], arr[j] = arr[j], arr[i]
			# Move one more position to the right
			all_strings(arr, i + 1, length)
			# Swap the letters back
			arr[i], arr[j] = arr[j], arr[i]

def main():
	arr = ['c', 'a', 't', 'd', 'o', 'g']
	print("This program will generate all strings that can be generated by using the",
	"following list of characters:")
	print(arr)
	length = len(arr)
	all_strings(arr, 0, length)
	
if __name__ == "__main__":
	main()