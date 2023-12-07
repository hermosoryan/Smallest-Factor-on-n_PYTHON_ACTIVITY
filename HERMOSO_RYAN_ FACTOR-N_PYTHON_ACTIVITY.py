
print("Name: Hermoso  Ryan ")
print("Section: BS COMPUTER SCIENCE 1E")
print("Instructor: Mr.Ralph Angelo Baguio ")
print("DATE: December 8, 2023")

def smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor of {n} (other than 1) is: {i}")
            break

# Example usage:
try:
    number = int(input("Enter an integer greater than or equal to 2: "))
    smallest_factor(number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

