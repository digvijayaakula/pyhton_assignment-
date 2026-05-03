def add(num_box1, num_box2):
    return num_box1 + num_box2

def multiply(num_box1, num_box2):
    return num_box1 * num_box2

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter number to multiply: "))

final_box = multiply(add(first_num, second_num), third_num)
print(final_box)