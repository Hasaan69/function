age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    if age % 2 == 0:
        print("The age entered is even.")
    else:
        print("The age entered is odd.")
else:
    print("Error: Please enter a valid whole number.")