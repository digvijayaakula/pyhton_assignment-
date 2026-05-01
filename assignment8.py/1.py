Write a program that takes a list of numbers and uses built-in functions to print:

* Maximum value
* Minimum value
* Sum of elements
* Length of the list'''
#take user in`put for list of numbers
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers] 
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of elements:", sum(numbers))
print("Length of the list:", len(numbers))  
