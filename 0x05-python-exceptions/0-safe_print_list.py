#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
   """
 Prints x elements of a list, handling potential errors.

 Args:
     my_list: The list to print elements from (default empty list).
     x: The number of elements to print (default 0).

 Returns:
     The number of elements actually printed.
 """
  k = 0
  for i in range(x):
    try:
      print(my_list[i], end=" ")
      k += 1
    except IndexError:
      pass
  print()
  return k
          
