# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Creativity exercise C1.21
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that repeatedly reads lines from standard input until an
# EOFError is raised, and then outputs those lines in reverse order (a user can indicate
# end of input by typing ctrl-D).
# Note:
#	Ctrl+D did not yield an EOFError when running the original version of this program
#	on Anaconda. Therefore, I couldn't follow the directions for this exercises.

def main():
    lines = []
    print("Please press enter/return two times when you would like to discontinue.")
    cont = True
    while cont:
        # Ctrl-D doesn't yield an EOFError.
        #try:
            #line = input("Type whatever you'd like: ")
            #lines.append(line)
        #except EOFError:
            #break
        line = input("Type whatever you'd like: ")
        if line == '':
            cont = False
        else:
            lines.append(line)
    print("\nIf we reverse what you've entered, we get the following:")
    for i in range(-1, -len(lines) - 1, -1):
        print(lines[i])
        
if __name__ == "__main__":
    main()