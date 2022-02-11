num1 = input("What is your first number: ")
num2 = input("What is your second number: ")
operation = input("What operations \"x\", \"-\", \"+\" : ")

if(operation == "x"):
    print("Doing multiplication - result = " + str(int(num1)*int(num2)))
elif(operation == "-"):
    print("Doing subtraction - result = " + str(int(num1) - int(num2)))
elif(operation == "+"):
    print("Doing addition - result = " + str(int(num1) + int(num2)))
else:
    print("invalid input mate")
