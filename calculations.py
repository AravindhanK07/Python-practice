class Utility:
    def display_options(self):
        options = [
            "A. Sum",
            "B. Subtract",
            "C. Multiply",
            "D. Divide",
            "E. Find Fibonacci number",
            "F. Find palindrome or not",
        ]
        print("Please choose the operation you want to do:")
        for option in options:
            print(option)


class Main:
    def addition(self):        
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a + b)
        
    def subtraction(self):
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

    def multiplication(self):
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a * b)

    def division(self):
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0:
                print("Error: Division by zero.")
            else:
                print("Result:", a / b)
     
    def fibonacci(self):
            n = int(input("Enter a number: "))
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            print("Fibonacci of", n, "is:", a)

    def is_palindrome(self):
        f = input("Enter a string: ")
        if f == f[::-1]:
            print("Yes, it's a palindrome.")
        else:
            print("No, it's not a palindrome.")

    def execute_operation(self, option):
        if option == "A":
            self.addition()
        elif option == "B":
            self.subtraction()
        elif option == "C":
            self.multiplication()
        elif option == "D":
            self.division()
        elif option == "E":
            self.fibonacci()
        elif option == "F":
            self.is_palindrome()
        else:
            print("Invalid option")


if __name__ == "__main__":
    main = Main()
    while True:
        utility = Utility()
        utility.display_options()
        option = input("Enter the option: ").upper()
        main.execute_operation(option)
