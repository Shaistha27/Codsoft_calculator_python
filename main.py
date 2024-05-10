def calculator():

    def add(list):
        return list[0]+list[1]
    
    def sub(list):
        return list[0]-list[1]
    
    def mul(list):
        return list[0]*list[1]
    
    def div(list):
        return list[0]/list[1]
    
    print("\n_Calculator_")
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)
    option = input("Enter the Operation : ").lower()
    numbers = input("Enter the two numbers sepearted by comma  : ").split(",")
    numbers = [int(x) for x in numbers]

    if option=="addition" or option=="add" or option=="+" or option=="1":
        result = add(numbers)
    elif option=="subtraction" or option=="sub" or option=="-" or option=="2":
        result = sub(numbers)
    elif option=="multiplication" or option=="mul" or option=="*" or option=="3":
        result = mul(numbers)
    elif option=="division" or option=="div" or option=="/" or option=="4":
        result = div(numbers)
    else:
        result = "Incorrect operation has been selected"
    print(f"Result : {result}")

repeat = True
calculator()

while repeat:
    ask = input("\nDo you want to continue? Y or N  ").lower()
    if ask=="y" or ask=="yes":
        calculator()
    elif ask == "n" or ask=="no":
        repeat = False
        print()
    else :
        print("\nMistyped")
        ask = input("Do you want to continue? Y or N  ").lower()
        if ask=="y" or ask=="yes":
            calculator()
        elif ask == "n" or ask=="no":
            repeat = False
            print()