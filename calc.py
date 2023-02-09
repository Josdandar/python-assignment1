def print_menu():
    print("-------")
    print("[1] Sum")
    print("[2] Substract")
    print("-------")


print_menu()
opt = input("Select an option")
num1 = float(input("Please provide num1: "))
num2 = float(input("Please provide num2: "))

if opt == "1":
    total = num1 + num2 
    print("The total is: "+ str(total))

elif opt == "2":
    total = num1 - num2 
    print("The total is: "+ str(total))

elif opt == "3":
    total = num1 * num2 
    print("The total is: "+ str(total))

elif opt == "4":
    total = num1 / num2 
    print("The total is: "+ str(total))