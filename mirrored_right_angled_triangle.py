"""
A right angled triangle in the following manner
        *
       **
      ***
     ****
    *****
   ******
  *******
*********
"""


def mirrored_right(num_rows):
    for i in range(1, num_rows+1):
        line = " "*((num_rows+1)-i) + "*"*i
        print(line)


rows = int(input("How many rows?: "))
mirrored_right(rows)
