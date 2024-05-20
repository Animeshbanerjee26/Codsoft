print("Calculator\n")

def stripNum(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num       #function for stripping insignificant 0s after decimal in float numbers 

try:
    num1 = stripNum(float(input("Enter the first number: ")))       #taking input of numbers from user
    num2 = stripNum(float(input("Enter the second number: ")))
    opr = input("Enter the operation to be performed (+ - * /):  ")     #taking input of operation 

        #addition
    if"+":
            print(f"{num1} + {num2} =", stripNum(num1 + num2))
        #subtraction
    elif "-":
            print(f"{num1} - {num2} =", stripNum(num1 - num2))
        #multiplication
    elif "*":
            print(f"{num1}*{num2} =", stripNum(num1 * num2))
        #division
    elif "/":
            print(f"{num1} / {num2} =", stripNum(num1 / num2))
        #case when user entered something else (wrong operator)
    else:
            print("Wrong operator entered!")

except ValueError:      #handling if user entered non-numeric input when asked for numbers
    print("Please enter numeric values!")