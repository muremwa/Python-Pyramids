"""
draw a pyramid
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
"""


def pyramid_tri(num_rows):
    num_rows += 1

    for i in range(1, num_rows):
        line = " "*(int((num_rows-i))+1) + "* "*i
        print(line)


rows = int(input("How many rows?: "))
pyramid_tri(rows)
