"""
an inverted pyramid
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""


def inverted_tri(num_rows):
    num_rows += 1

    for i in range(1, num_rows):
        line = " "*i + "* "*(num_rows-i)
        print(line)


rows = int(input("How many rows?: "))
inverted_tri(rows)
