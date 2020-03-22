# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.30
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that can take a positive integer greater than 2 as input and
# write out the number of times one must repeatedly divide this number by 2 before
# getting a value less than 2.

def evenly_divisible_by_2(num):
	count = 0
	temp_num = num
	while temp_num % 2 == 0 and temp_num >= 2:
		temp_num //= 2
		count += 1
	return count

def main():
	print("This program will print the number of times a number can be evenly divided by", 
	"two before getting a value less than 2.")
	while True:
		try:
			num = int(input("Enter an integer: "))
			break
		except:
			print("Invalid input")
	print("# of times {} can be divided by 2: {}".format(num, evenly_divisible_by_2(num)))

if __name__ == "__main__":
	main()