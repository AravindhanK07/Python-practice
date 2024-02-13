options = "Please choose the operation you want to do\nA. Sum\nB. Subtract\nC. Multiply\nD. Divide\nE. Find Fibonacci number\nF. Find palindrome or not"
print(options)

option=(input("Enter the option: ")).upper()

def sum():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a+b)

def subtract():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a-b)

def multiply():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a*b)

def divide():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a/b)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
         return 1
    return fib(n-1) + fib(n-2)

def isPalindrome(f):
    if f == f[::-1]:
        print("Yes")
    else:
        print("No")


if option=="A":
    sum()
elif option=="B":
    subtract()
elif option=="C":
    multiply()
elif option=="D":
    divide()
elif option=="E":
     n=int(input("Enter a number: "))
     res = fib(n)
     print("Fibonacci of", n, "is:", res)
elif option=="F":
     f=input("Enter a string: ")
     isPalindrome(f)
else:
    print("Invalid option")