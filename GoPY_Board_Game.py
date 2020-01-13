#   github.com/bscihsan

def show(matrix, size):  # This function shows game board.
    for i in range(size):
        for j in range(size):
            print("%4s" % (matrix[i][j]), end="")
        print()


while True:  # For taking board size from user, prints error if there is errornous input and asks for size again.
    size = int(input("What Size Game GoPy?"))
    if size <= 2:
        print("Please enter a valid number")
        continue
    else:
        break
matrix = []  # Creating game board's database.
for i in range(size):  # Generating a new game board.
    matrix.append([])
    for j in range(size):
        matrix[i].append(i * size + j)
show(matrix, size)  # Shows game board after initialization.
counter = 1  # For following that which player's turn it is.
while True:  # Game play loop
    decision = -1
    if counter % 2 == 1:  # Which means it is Player 1's turn.
        counter += 1  # Increasing counter since it is next player's turn after making decision.
        decision = int(input("Player 1 turn--> "))  # Taking users decision and printing error if there is errornous input.
        if decision < 0 or decision >= size * size:
            print("Please enter a valid number")
            show(matrix, size)  # Showing game board after errornous input.
            continue
        if matrix[decision // size][decision % size] == "X":
            print("You have made this choice before")
            show(matrix, size)  # Showing game board after errornous input.
            continue
        elif matrix[decision // size][decision % size] == "O":
            print("The other player select this cell before.")
            show(matrix, size)  # Showing game board after errornous input.
            continue
    else:  # If it is not Player 1's turn, then it means it is Player 2's turn.
        counter += 1  # Increasing counter since it is next player's turn after making decision.
        decision = int(input("Player 2 turn--> "))  # Taking users decision and printing error if there is errornous input.
        if decision < 0 or decision >= size * size:
            print("Please enter a valid number")
            show(matrix, size)  # Showing game board after errornous input.
            continue
        if matrix[decision // size][decision % size] == "O":
            print("You have made this choice before")
            show(matrix, size)  # Showing game board after errornous input.
            continue
        elif matrix[decision // size][decision % size] == "X":
            print("The other player select this cell before.")
            show(matrix, size)  # Showing game board after errornous input.
            continue
    if counter % 2 == 0:  # Since program incremented counter, now this means it is Player 1's turn.
        matrix[decision // size][decision % size] = "X"  # Putting X to desired area.
    else:  # If it is not Player 1's turn, then it means it is Player 2's turn.
        matrix[decision // size][decision % size] = "O"  # Putting O to desired area.
    show(matrix, size)  # Showing game board after move.
    for i in matrix:  # This loop controls if there is a win in horizontal axis.
        xCounter = False
        oCounter = False
        for j in i:
            if not (xCounter or oCounter):
                if j == "X":
                    xCounter = True
                    continue
                elif j == "O":
                    oCounter = True
                    continue
                break
            if xCounter:
                if j == "X":
                    continue
                xCounter = False
                break
            elif oCounter:
                if j == "O":
                    continue
                oCounter = False
                break
        if xCounter:
            print("Winner: X")
            exit(0)
        elif oCounter:
            print("Winner: O")
            exit(0)
    for i in range(size):  # This loop controls if there is a win in vertical axis.
        xCounter = False
        oCounter = False
        for j in range(size):
            if not (xCounter or oCounter):
                if matrix[j][i] == "X":
                    xCounter = True
                    continue
                elif matrix[j][i] == "O":
                    oCounter = True
                    continue
                break
            if xCounter:
                if matrix[j][i] == "X":
                    continue
                xCounter = False
                break
            elif oCounter:
                if matrix[j][i] == "O":
                    continue
                oCounter = False
                break
        if xCounter:
            print("Winner: X")
            exit(0)
        if oCounter:
            print("Winner: O")
            exit(0)
    if matrix[0][0] == "X":  # This loop controls if there is a win for X in diagonal axis(from upper left to lower right).
        statement = True
        for i in range(1, size):
            if matrix[i][i] == "X":
                continue
            else:
                statement = False
                break
        if statement:
            print("Winner: X")
            exit(0)
    elif matrix[0][0] == "O":  # This loop controls if there is a win for O in diagonal axis(from upper left to lower right).
        statement = True
        for i in range(1, size):
            if matrix[i][i] == "O":
                continue
            else:
                statement = False
                break
        if statement:
            print("Winner: O")
            exit(0)
    if matrix[0][size - 1] == "X":  # This loop controls if there is a win for X in diagonal axis(from upper right to lower left).
        statement = True
        for i in range(1, size):
            if matrix[i][size - i - 1] == "X":
                continue
            else:
                statement = False
                break
        if statement:
            print("Winner: X")
            exit(0)
    elif matrix[0][size - 1] == "O": # This loop controls if there is a win for O in diagonal axis(from upper right to lower left).
        statement = True
        for i in range(1, size):
            if matrix[i][size - i - 1] == "O":
                continue
            else:
                statement = False
                break
        if statement:
            print("Winner: O")
            exit(0)
    endGame = True  # For checking if there is any empty place at the board.
    for i in matrix:
        for j in i:
            if not (j == "X" or j == "O"):
                endGame = False
                break
    if endGame:  # If there is no empty space, which means game over but there is no winner, which means tie. Program prints "Tie" and exits.
        print("No Winner!")
        exit(0)