"""
draw such
*
**
* *
*  *
*   *
*    *
*     *
*      *
*********
"""


def hollow_tri(num_rows):
    for i in range(1, num_rows+1):
        line = "*" + " "*int(i-2) + "*"

        if i == 1:
            line = "*"

        if i == num_rows:
            line = "*"*num_rows

        print(line)


rows = int(input("How many rows?: "))
hollow_tri(rows)
