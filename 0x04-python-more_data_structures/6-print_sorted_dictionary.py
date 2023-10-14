def print_sorted_dictionary(a_dictionary):
  """
  Prints the values in a dictionary in alphabetical order.

  Args:
    a_dictionary: A dictionary.
  """

  keys = sorted(a_dictionary.keys())
  for key in keys:
    print(key, ":", a_dictionary[key])

print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
