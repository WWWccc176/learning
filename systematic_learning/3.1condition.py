a = int(input("enter a number:"))
if a <= 0:
    print("you should enter a positive number")
else:
    print("the number is valid")
num = int(input("Enter another number: "))
if num > 0:
    print(num, "is positive")
    print(num, "squared is ", num**2)
