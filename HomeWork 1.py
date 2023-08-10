def is_palindrome(string):
    return string == string[::-1]
input_string = "лепсспел"
print(is_palindrome(input_string))  # Вывод: True

input_string = "helloworld"
print(is_palindrome(input_string))  # Вывод: False

