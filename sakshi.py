def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b): 
    if b==0:
        return "Error:Cannot divide by zero"
    return a/b
def clear():
    print("\nCalculator cleared.\n")
def calculator():
    while True:
        print("-----Simple Calculator-----")
        print("1.Addition(+)")
        print("2.Subtraction(-)")
        print("3.Mulytiplication(*)")
        print("4.Division(/)")
        print("5.clear")
        print("6.Exit")
        
        choice= input("Enter your choice(1-6):")
        if choice =='6':
            print("Exiting Calculator...")
            break
        if choice == '5':
            clear()
            continue
        try:
            num1=float(input("Enter your first number:"))
            num2=float(input("Entersecond number:"))
        except ValueError:
            print("Invalid input PLease enter numbers only.\n")
            continue
        if choice =='1':
            print("Result:",add(num1,num2))
        elif choice =='2':
            print("Result:",subtract(num1,num2))
        elif choice =='3':
            print("Result:",multiply(num1,num2))
        elif choice =='4':
            print("Result:",divide(num1,num2))
        else:
            print("Invalid choice! Please try again.")
        print()
        
       
calculator()        
        
        
                      
                   
            
        
        

