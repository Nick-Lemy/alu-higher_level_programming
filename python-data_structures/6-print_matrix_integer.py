#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print("")
    else:
        for i in matrix:
            if len(i) > 1:
                for j in i:
                    print("{:d}".format(j), end=" " if i[-1] != j else "\n")
            else:
                print("{:d}".format(i), end=" ")
print_matrix_integer()
