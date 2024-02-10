#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
  """Prints x elements of a list, handling exceptions.

  Args:
    my_list: The list to print elements from.
    x: The number of elements to print (defaults to 0).

  Returns:
    The number of elements actually printed.
  """
  count = 0
  try:
    for i in range(x):
      print(my_list[i], end=" ")
      count += 1
  except IndexError:
    pass
  finally:
    print()
  return count
