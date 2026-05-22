
# 9. Write a Program to accept a two number and find sum of even or odd
choice = input("Do you want to sum 'even' or 'odd' numbers? ").lower()


while True:
    n1 = int(input(f"Enter first {choice} number: "))
    if (choice == "even" and n1 % 2 == 0) or (choice == "odd" and n1 % 2 != 0):
        break
    print(f"Error! {n1} is not {choice}. Try again.")


while True:
    n2 = int(input(f"Enter second {choice} number: "))
    if (choice == "even" and n2 % 2 == 0) or (choice == "odd" and n2 % 2 != 0):
        break
    print(f"Error! {n2} is not {choice}. Try again.")

print(f"The sum of your {choice} numbers is: {n1 + n2}")
