def is_palindrome(s):
    return s == s[::-1]

def find_next_palindrome(number, base):
    while True:
        number += 1
        converted_number = format(number, 'b') if base == 2 else str(number)
        
        if is_palindrome(converted_number):
            return number

def main():
    try:
        number = int(input("Enter a number: "))
        base = int(input("Enter the base (2 for binary, 10 for decimal): "))
        
        if number < 0 or base < 2:
            print("Please enter a positive number with a base greater than or equal to 2.")
            return

        next_palindrome = find_next_palindrome(number, base)
        print(f"The next higher palindromic number in base {base} is: {next_palindrome}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()