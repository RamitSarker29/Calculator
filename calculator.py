n1= float(input("Enter Your first number: "))
n2= float(input("Enter your second number: "))
operator = input("Enter your operator: ")
if operator == "+":
    print("The sum of the numbers are: ",n1+n2)
elif operator =="-":
    print("The difference of the numbers are: ",n1-n2)
elif operator =="*":
    print("The product of the numbers are: ",n1*n2)
elif operator =="/":
    print("The division of the numbers are: ",n1/n2)
elif operator =="^":
    print("The result is : ",n1**n2)
else:
    print("Invalid operator")
