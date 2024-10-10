def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def palindrome(s):
    return s == s[::-1]

def get_length(obj):
    return len(obj)

import my_module

def main():
    print("Enter your choices:")
    print("1. Palindrome")
    print("2. Fibonacci")
    print("3. Length")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        s = input("Enter a string: ")
        result = my_module.palindrome(s)
        print(f"Is '{s}' a palindrome? {result}")
    elif choice == 2:
        n = int(input("Enter a number: "))
        result = my_module.fibo(n)
        print(f"The Fibonacci number at position {n} is {result}")
    elif choice == 3:
        obj = input("Enter a list or string: ")
        result = my_module.get_length(obj)
        print(f"The length of the input is: {result}")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()