from math import inf

AIMoveRow = -1
AIMoveCol = -1
depth = 9


def displayBoard(state):
    # this function is to display the tic tac toe board (state)
    for i in range(3):
        print('             |     |')
        print('          ' + state[i][0] + '  |  ' + state[i][1] + '  |  ' + state[i][2])
        print('             |     |')
        if not i == 2:
            print('        ----- ----- -----')


def evaluate(state):
    # this function is to check if and how the game ends
    # check row winning conditions
    # used as the static evaluation values for leaf nodes:
    # AI wins is 1 (hence maximizer), human wins is -1, tie game is 0 */

    # check row winning conditions
    for i in range(3):
        if state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            if state[i][0] == 'O':
                return 1
            elif state[i][0] == 'X':
                return -1

    # check column winning conditions
    for j in range(3):
        if state[0][j] == state[1][j] and state[0][j] == state[2][j]:
            if state[0][j] == 'O':
                return 1
            elif state[0][j] == 'X':
                return -1

    # check diagonal winning conditions
    if (state[0][0] == state[1][1] and state[0][0] == state[2][2]) or (
            state[0][2] == state[1][1] and state[0][2] == state[2][0]):
        if state[1][1] == 'O':
            return 1
        elif state[1][1] == 'X':
            return -1

    # return 0 if no winner
    return 0


def isFull(state):
    # this function is to check whether the board is full
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                return False
    return True


def minimax(state, depth, alpha, beta, isAI):
    # this is a fascinating recursive algorithm that the AI uses to ensure never losing
    # as shown in the function parameters, alpha-beta pruning is also used to algorithmic efficiency
    # Base case: return after the AI evaluate the leaf nodes
    if evaluate(state) != 0 or depth == 0:
        return evaluate(state)
    if isFull(state):
        return 0

    # it is the maximizer's move (maximize static evaluation of game tree branches)
    if isAI:
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'O'
                    alpha = max(alpha, minimax(state, depth - 1, alpha, beta, False))
                    state[i][j] = ' '
                    if alpha >= beta:
                        break
        return alpha
    else:
    # it is the minimizer's move (minimize static evaluation of game tree branches)
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'X'
                    beta = min(beta, minimax(state, depth - 1, alpha, beta, True))
                    state[i][j] = ' '
                    if alpha >= beta:
                        break
        return beta


def findAIMove(state):
    # this function is to find the game tree branch with the highest evaluation (move position)
    # it passes every validated (empty) cell position into the minimax algorithm for evaluation
    maxEval = -inf
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                state[i][j] = 'O'
                eval = minimax(state, depth, -inf, inf, False)
                state[i][j] = ' '
                if eval > maxEval:
                    global AIMoveRow, AIMoveCol
                    AIMoveRow = i
                    AIMoveCol = j
                    maxEval = eval


def humanMove(state):
    # this function is to get where the human wants to place 'X' (user input)
    # while loop for user validation
    while True:
        try:
            position = int(input('Please enter your move (1-9): '))
        except ValueError:
            print('Please choose a number.')
            continue

        if position > 9 or position < 1:
            print('Invalid input. Please try again.')
            continue
        
        # convert the position to row and column
        row = int((position - 1) / 3)
        col = int((position - 1) % 3)

        if state[row][col] == ' ':
            state[row][col]='X'
            break
        else:
            print('Position occupied. Please try again.')
            continue


def AIMove(state):
    # this function is to place the AI's next move on the board
    findAIMove(state)
    
    state[AIMoveRow][AIMoveCol] = 'O'
    displayBoard(state)
    
    # convert the row and column to positions 1-9
    position = 3 * AIMoveRow + AIMoveCol + 1
    print('The AI has chosen position', position, '.')


def main():
    global board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    displayBoard(board)
    
    # the game stops either when the board is full or one side wins. The human moves first since
    # giving the AI first move advantage does not contribute to proving the effectiveness of
    # minimax algorithm
    while evaluate(board) == 0 and not isFull(board):
        humanMove(board)
        AIMove(board)
        global depth
        # the value of depth is updated based on the height of game tree nodes
        depth = depth - 1

    # display winner / tie
    if evaluate(board) == 1:
        print('The AI win.')
    elif evaluate(board) == -1:
        print('You win. The AI needs some fixing.')
    else:
        print('Tie game. You must be a careful player.')


while True:
    # game title
    print('\nWelcome to Tic Tac Toe. The game has a fascinating algorithm but is boring to play.\n')
    print('     Impossible Tic Tac Toe')
    print('----------------------------------')
    main()
    
    # giving user the choice of starting a new game
    again = input('Type y to play again or anything else to exit: ')
    if again.lower() == 'y':
        print('\n            NEW GAME')
        print('----------------------------------')
        board = [' ' for x in range(10)]
        main()
    else:
        print('Goodbye, hope you had some fun playing.')
        break
