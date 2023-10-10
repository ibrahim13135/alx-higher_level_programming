def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers.

  Args:
    matrix: A list of lists of integers.
  """

  for row in matrix:
    for element in row:
      print(element, end=" ")
    print()

# Example usage:

print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
