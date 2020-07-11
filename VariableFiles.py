from math import sin, cos, tan, degrees, radians, sqrt
from statistics import mean, median, mode, stdev
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def completesin(x):
    return sin(radians(x))

def completecos(x):
    return cos(radians(x))

def completetan(x):
    return tan(radians(x))

def completesqrt(x):
    return sqrt(x)

def completemean(x):
    return mean(x)

def completemedian(x):
    return median(x)

def completemode(x):
    return mode(x)

def completestdev(x):
    return stdev(x)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Raise to a power")
print("6.Sin function")
print("7.Cos function")
print("8.Tan Function")
print("9.Square root function")
print("10.Mean of a list")
print("11.Median of a list")
print("12.Mode of a list")
print("13.Standard Deviation of a list")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "raised to a power of", num2, "=", power(num1, num2))

        break
    else:
        if choice in ('6', '7', '8', '9'):
            c = float(input("Enter your number:"))

            if choice == '6':
                print("The sine of", c, "is", completesin(c))

            elif choice == '7':
                print("The cosine of", c, "is", completecos(c))

            elif choice == '8':
                print("The tangent of", c, "is", completetan(c))

            elif choice == '9':
                print("The square root of", c, "is", completesqrt(c))

            break
        else:
            if choice in ('10', '11', '12', '13'):
                lst = [] 
  
                n = int(input("Enter number of elements : ")) 
  
                for i in range(0, n): 
                    ele = int(input()) 
  
                    lst.append(ele)
                if choice == '10':
                    print("The mean of your numbers is", completemean(lst))

                if choice == '11':
                    print("The median of your numbers is", completemedian(lst))

                if choice == '12':
                    print("The mode of your numbers is", completemode(lst))

                if choice == '13':
                    print("The standard deviation of your numbers is", completestdev(lst))
                break
            else:
                print("Invalid Input")
            break
