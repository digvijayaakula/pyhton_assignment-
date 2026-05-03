def count_even_odd(num_list_box):
    even_box = 0
    odd_box = 0
    for num_box in num_list_box:
        if num_box % 2 == 0:
            even_box += 1
        else:
            odd_box += 1
    return even_box, odd_box

user_input = input("Enter numbers separated by space: ")
num_list_box = list(map(int, user_input.split()))

even_result, odd_result = count_even_odd(num_list_box)

print("Even count:", even_result)
print("Odd count:", odd_result)