"""
Triangle featuring odd number of stars
*
***
*****
*******
*********
***********
*************
"""


def odd_tri(num_rows):
    num_rows *= 2

    for i in range(1, num_rows):
        if i%2 !=0:
            line = "*"*i
            print(line)


rows = int(input("How many rows?: "))
odd_tri(rows)
