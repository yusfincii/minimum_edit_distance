"""
# a useful method can be use instead for loop to print matrix
def printX(matrix):
    for row in matrix:
        print("|  {}  |".format(row))
"""


# main function
def min_edit_distance(text1, text2):
    len_text1 = len(text1)
    len_text2 = len(text2)

    # create an empty matrix according to given strings length
    matrix = [[0] * (len_text2 + 1) for i in range(len_text1 + 1)]

    # assigns the matrix's default values
    for x in range(len_text1 + 1):
        matrix[x][0] = x
    for y in range(len_text2 + 1):
        matrix[0][y] = y

    # fill the matrix's empty cells with distance values
    for i in range(1, len_text1 + 1):  # starts from 1
        for j in range(1, len_text2 + 1):  # starts from 1
            # same letter case
            if text1[i - 1] == text2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            # if letters are not equal the distance value will be increment with 1
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j],
                                   matrix[i][j - 1]) + 1

    print()
    print("--------------------  MATRIX  ----------------------")
    print("----------------------------------------------------")
    # print the matrix
    for row in matrix:
        print("|  {}  |".format(row))
    print("----------------------------------------------------")
    print()

    # keeping word lengths for
    # explaining operations for each step
    length1 = len_text1
    length2 = len_text2

    print("--- Operations with reverse order ---")
    while length1 > 0 or length2 > 0:
        # same letter case
        if length1 > 0 and length2 > 0 and text1[length1 - 1] == text2[length2 - 1]:
            print("No operation ({} == {})".format(text1[length1 - 1], text2[length2 - 1]))
            length1 -= 1
            length2 -= 1
        # different letter case
        elif length1 > 0 and length2 > 0 and matrix[length1][length2] == matrix[length1 - 1][length2 - 1] + 1:
            # length1 - 1, length2 - 1))
            print("Replace {} with {} at ({}, {})".format(text1[length1 - 1], text2[length2 - 1],
                                                          length1 - 1, length2 - 1))
            length1 -= 1
            length2 -= 1

        # this following two condition block will execute
        # when length of given two strings is not equal

        # case of length1 > length2
        elif length1 > 0 and matrix[length1][length2] == matrix[length1 - 1][length2] + 1:
            print("Delete {} at ({}, {})".format(text1[length1 - 1], length1 - 1, length2))
            length1 -= 1
        # case of length2 > length1
        else:
            print("Insert {} at ({}, {})".format(text2[length2 - 1], length1, length2 - 1))
            length2 -= 1
    print("----------------------------")

    return matrix[len_text1][len_text2]


# example (assignment 3 words)
source = "sub-section"
target = "subdivision"
result = min_edit_distance(source, target)
print()
print("--> Minimum edit distance between '{}' and '{}' words is : {}".format(source, target, result))
