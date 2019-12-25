"""
write a function to print a pyramid of the following fashion
*
**
***
****
*****
******
*******
********
"""


def right_pyramid(num_rows):
    for i in range(1, num_rows+1):
        print("*"*i)


rows = input("How many rows?: ")
right_pyramid(int(rows))
