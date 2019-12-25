"""
Triangle in the following manner
********
*******
******
*****
****
***
**
*
"""


def inverted_right(num_rows):
    num_rows += 1
    for i in range(1, num_rows):
        line = "*"*(num_rows-i)
        print(line)


rows = int(input("How many rows?: "))
inverted_right(rows)
