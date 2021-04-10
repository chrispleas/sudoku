from copy import deepcopy

"""This is a 9x9 Sudoku solver that uses a basic DFS algorithm. This implementation is optimized to solve some 
particularly tricky puzzles (ones that would require considering 1+ million puzzle states) by considering each cell 
at each iteration and ensuring that a basic row + column + box check has not made any individual cell invalid. This 
dramatically cuts down on the number of states that need to be considered and ends up solving them much faster. """

SIZE = 9  # This is a 9x9 Sudoku


def print_board(board):
    def out(a):
        print(a, end='')

    if not board:
        out("There is no solution to this puzzle!")
        return
    for i in range(SIZE):
        for j in range(SIZE):
            cell = board[i][j]
            if cell == 0 or isinstance(cell, set):
                out('.')
            else:
                out(cell)
            if (j + 1) % 3 == 0 and j < 8:
                out(' |')
            if j != 8:
                out(' ')
        out('\n')
        if (i + 1) % 3 == 0 and i < 8:
            out("---------------------\n")


def board_to_state(board):
    """Take a board (9x9 list of numbers) and replace 0s (blanks) with the set of possible values"""

    state = deepcopy(board)
    for i in range(SIZE):
        for j in range(SIZE):
            cell = state[i][j]
            if cell == 0:
                state[i][j] = set(range(1, SIZE + 1))
    return state


def done(state):
    """We are done if there are no more sets in the state"""

    for row in state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True

def validate_state(state):
    """Basic validation of the state just to make sure that the initial board received is actually valid. Note that
    the iterate_step function does not actually check for invalid configurations like duplicate numbers in the same
    row"""

    # Validate rows
    for i in range(SIZE):
        row = state[i]
        values = [x for x in row if not isinstance(x, set)]
        if len(values) != len(set(values)):
            return False

    # Validate columns
    for j in range(SIZE):
        column = [state[x][j] for x in range(SIZE)]
        values = [x for x in column if not isinstance(x, set)]
        if len(values) != len(set(values)):
            return False

    # Validate boxes
    for x in range(3):
        for y in range(3):
            values = []
            for i in range(3 * x, 3 * x + 3):
                for j in range(3 * y, 3 * y + 3):
                    cell = state[i][j]
                    if not isinstance(cell, set):
                        values.append(cell)
            if len(values) != len(set(values)):
                return False

    return True

def iterate_step(state):
    """
    Iterate one step.

    @return:  A two element tuple that says whether the state
              is solvable and whether the iteration changed
              the state.
    """

    changed_state = False

    # update state using row rule
    for i in range(SIZE):
        row = state[i]
        values = set(x for x in row if not isinstance(x, set))
        for j in range(SIZE):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    val = state[i][j].pop()
                    state[i][j] = val
                    values.add(val)
                    changed_state = True
                elif len(state[i][j]) == 0:
                    return False, None

    # update state using column rule
    for j in range(SIZE):
        column = [state[x][j] for x in range(SIZE)]
        values = set([x for x in column if not isinstance(x, set)])
        for i in range(SIZE):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    val = state[i][j].pop()
                    state[i][j] = val
                    values.add(val)
                    changed_state = True
                elif len(state[i][j]) == 0:
                    return False, None

    # update state using box rule
    for x in range(3):
        for y in range(3):
            values = set()
            for i in range(3 * x, 3 * x + 3):
                for j in range(3 * y, 3 * y + 3):
                    cell = state[i][j]
                    if not isinstance(cell, set):
                        values.add(cell)
            for i in range(3 * x, 3 * x + 3):
                for j in range(3 * y, 3 * y + 3):
                    if isinstance(state[i][j], set):
                        state[i][j] -= values
                        if len(state[i][j]) == 1:
                            val = state[i][j].pop()
                            state[i][j] = val
                            values.add(val)
                            changed_state = True
                        elif len(state[i][j]) == 0:
                            return False, None

    return True, changed_state


def iterate(state):
    """Iterate until we know that the puzzle cannot be solved, or we are no longer making progress"""

    while True:
        solvable, changed_state = iterate_step(state)
        if not solvable:
            return False
        if not changed_state:
            return True


def solve(state):
    """Take a state (NOT a board) as input, and iterate on that state until it is solved"""

    solvable = iterate(state)
    if not solvable:
        return None
    if done(state):
        return state
    for i in range(SIZE):
        for j in range(SIZE):
            cell = state[i][j]
            if isinstance(cell, set):
                for value in sorted(cell):
                    new_state = deepcopy(state)
                    new_state[i][j] = value
                    solved = solve(new_state)
                    if solved is not None:
                        return solved
                return None


def solve_board(board):
    """Takes a board (9x9 list of numbers) and returns either a solved board or a message stating that the board is
    invalid"""
    state = board_to_state(board)
    if not validate_state(state):
        return 'Input board is invalid!'

    result = solve(state)
    if validate_state(result):
        return result
    else:
        return 'Input board is invalid!'
