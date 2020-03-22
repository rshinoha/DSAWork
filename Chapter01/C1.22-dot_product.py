# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Creativity exercise C1.21
# Ryoh Shinohara
# =======================================================================================
# Write a short Python program that takes two arrays a and b of length n storing int
# values, and returns the dot product of a and b. That is, it returns an array c of
# length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.

def dot_product(a, b):
    """
    Given two arrays of equal length, returns the dot product

    Example:
        a = [1, 2]
        b = [3, 4]

        dot_product(a, b)
        >> 11
    """
    if len(a) != len(b):
        raise ValueError('Arrays are of different lengths')
    else:
        return [a[i] * b[i] for i in range(len(a))]

def is_valid_array(n):
	"""
	Given an array length, n, prompts the user to enter n integers
	"""
	arr = []
	while len(arr) != n:
		try:
			arr = list(map(int, input("Enter integer values: ").split()))
		except:
			print("Invalid input")
		if len(arr) != n:
			print("Must have {} integers".format(n))
	return arr
		
def main():
	arr_len = 0
	while arr_len < 1:
		try:
			arr_len = int(input("Enter a valid array length: "))
		except (ValueError):
			print("Invalid array length")
	a = is_valid_array(arr_len)
	b = is_valid_array(arr_len)
	
	print("Array a is {}.".format(a))
	print("Array b is {}.".format(b))
	print("The dot product of the arrays is {}.".format(dot_product(a, b)))
	
if __name__ == "__main__":
	main()