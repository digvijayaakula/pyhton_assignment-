def is_palindrome(word_box):
    return word_box == word_box[::-1]

user_word = input("Enter a word: ")
result_box = is_palindrome(user_word)
print(result_box)