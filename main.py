#Returns Sum of num1 and num2 +
def add(num1, num2):
    return num1 + num2

#Returns Sum of num1 and num2 -
def sub(num1, num2):
    return num1 - num2

#Returns Sum of num1 and num2 *
def mul(num1, num2):
    return num1 * num2

#Returns Sum of num1 and num2 /
def div (num1, num2):
    return num1 / num2

def main():
    operation = input("Choose operation (+,-,*,/): ")
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
       #invalid operation
       print("You must enter valid operation")
       return main()
    else:
       var1 = int(input("Enter num1:"))
       var2 = int(input("Enter num2:"))
       if (operation == '+') :
          print(add(var1, var2))
       elif (operation == '-') :
          print(sub(var1, var2))
       elif (operation == '*') :
          print(mul(var1, var2))
       elif (operation == '/') :
          print(div(var1, var2))
    return main()

def main():

    var3 = int(input("Enter Miles :"))
    km = 1.6 * var3
    print("km:")
    print(km)

main()