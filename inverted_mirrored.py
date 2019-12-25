"""
triangle in the following form
*********
 ********
  *******
   ******
    *****
     ****
      ***
       **
        *
"""


def inverted_right_mirror(num_rows):
    num_rows += 1

    for i in range(num_rows):
        line = " "*(i) + "*"*(num_rows-i)
        print(line)


rows = int(input("How many rows?: "))
inverted_right_mirror(rows)
