input_number = int(input())

first_digit = input_number // 100
second_digit = input_number // 10 % 10
third_digit = input_number % 10

print(first_digit + second_digit + third_digit)
