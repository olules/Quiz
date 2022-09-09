print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=80 and avg<=100:
    print("Your Grade is A")
elif avg>=50 and avg<81:
    print("Your Grade is B")
elif avg<51:
    print("Your Grade is F")
else:
    print('Invalid input')