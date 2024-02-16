import json

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
        numbers = []
        while True:
            num_input = input("Enter a number (press Enter to finish): ")
            if num_input.strip() == "":
                break
            numbers.append(float(num_input))
        print(sum(numbers))    
        return {"Sum": sum(numbers)}
        
        
    def subtraction(self):
        numbers = []
        while True:
            num_input = input("Enter a number (press Enter to finish): ")
            if num_input.strip() == "":
                break
            numbers.append(float(num_input))
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print(result)
        return {"Result": result}

    def multiplication(self):
        numbers = []
        while True:
            num_input = input("Enter a number (press Enter to finish): ")
            if num_input.strip() == "":
                break
            numbers.append(float(num_input))
        result = 1
        for num in numbers:
            result *= num
        print(result)
        return {"Result": result}

    def division(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            return {"Error": "Division by zero."}
        else:
            print(a/b)
            return {"Result": a / b}
     
    def fibonacci(self):
        n = int(input("Enter a number: "))
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        print("Fibonacci of {}:{}".format(n,a))
        return {"Fibonacci of {}".format(n): a}

    def is_palindrome(self):
        f = input("Enter a string: ")
        if f == f[::-1]:
            print("Yes, it's a palindrome.")
            return {"Result": "Yes, it's a palindrome."}
        else:
            print("No, it's not a palindrome.")
            return {"Result": "No, it's not a palindrome."}

    def execute_operation(self, option):
        if option == "A":
            return self.addition()
        elif option == "B":
            return self.subtraction()
        elif option == "C":
            return self.multiplication()
        elif option == "D":
            return self.division()
        elif option == "E":
            return self.fibonacci()
        elif option == "F":
            return self.is_palindrome()
        else:
            return {"Error": "Invalid option"}


if __name__ == "__main__":
    main = Main()
    results = {}
    while True:
        utility = Utility()
        utility.display_options()
        option = input("Enter the option: ").upper()
        if option == "EXIT":
            break
        result = main.execute_operation(option)
        results.update(result)

    with open("operation_results.json", "w") as file:
        json.dump(results, file)

    with open("operation_results.json", "r") as file:
        data = json.load(file)
        print("\nContents of the JSON file:")
        print(json.dumps(data, indent=4))
