#!/usr/bin/python3

# def print_last_digit(number):
def print_last_digit(number):
  """Prints the last digit of a number and returns it."""
  print(abs(number % 10), end="")
  return abs(number % 10)

print_last_digit(12345)
print_last_digit(67890)
