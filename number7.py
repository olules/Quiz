print("Program to print star pattern: \n");
rows = input("Enter maximum stars you want display on a single line")
num_rows = int (rows)
for i in range (0, num_rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")