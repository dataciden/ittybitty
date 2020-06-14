# Sudoku
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
lines = "- - - - - - - - - - - - - - -"
counter = 0
for i in sudoku:
    counter += 1
    if counter % 3 == 1:
        print (lines)
    for j in range(9):
        print (i[j]," " ,end='')
        if j % 3 == 2 and j != 0 and j != 8:
            print ("| ",end='')
        if j == 8 :
            print()
print (lines)