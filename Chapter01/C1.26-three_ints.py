# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Creativity exercise C1.21
# Ryoh Shinohara
# =======================================================================================
# C-1.26 Write a short program that takes as input three integers, a, b, and c, from the
# console and determines if they can be used in a correct arithmetic formula (in the
# given order), like "a+b = c," "a = b−c," or "a*b = c."

def main():
	print("This program will check if a set of three integers will fulfill the",
	"following conditions:")
	print("\t1. a + b = c")
	print("\t2. a = b - c")
	print("\t3. a * b = c")
	nums = []
	fail = True
	count = 0
	while fail:
		try:
			nums = [int(x) for x in (input("Enter three integers: ").split())]
			fail = False
		except:
			print("Try again.")
	a = nums[0]
	b = nums[1]
	c = nums[2]
	if a + b == c and a == b - c and a * b == c:
		print("Satisfies all conditions")
	else:
		print("Does not satisfy all conditions")

if __name__ == "__main__":
	main()