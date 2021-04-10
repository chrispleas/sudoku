import unittest
import sudoku


class TestSudoku(unittest.TestCase):
    easy_board_1 = [
        [0, 0, 4, 9, 0, 3, 7, 2, 5],
        [5, 6, 2, 7, 0, 8, 3, 1, 9],
        [3, 9, 7, 5, 0, 2, 8, 6, 4],
        [2, 3, 9, 6, 0, 7, 1, 4, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 1, 8, 2, 0, 9, 6, 5, 7],
        [9, 4, 1, 3, 0, 6, 5, 8, 2],
        [6, 2, 3, 8, 0, 5, 4, 7, 1],
        [8, 7, 5, 4, 0, 1, 9, 3, 6],
    ]
    easy_board_2 = [
        [1, 8, 4, 9, 0, 3, 7, 2, 0],
        [5, 6, 2, 7, 0, 8, 3, 0, 9],
        [3, 9, 7, 5, 0, 2, 0, 6, 4],
        [2, 3, 9, 6, 0, 7, 1, 4, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 1, 8, 2, 0, 9, 6, 5, 7],
        [9, 4, 1, 3, 0, 6, 5, 8, 2],
        [6, 2, 3, 8, 0, 5, 4, 7, 1],
        [8, 7, 5, 4, 0, 1, 9, 3, 6],
    ]
    easy_board_3 = [
        [1, 8, 4, 9, 0, 3, 7, 2, 5],
        [5, 6, 2, 7, 0, 8, 3, 1, 9],
        [3, 9, 7, 5, 0, 2, 8, 6, 4],
        [2, 3, 9, 6, 0, 7, 1, 4, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 1, 8, 2, 0, 9, 6, 5, 7],
        [9, 4, 1, 3, 0, 6, 5, 8, 2],
        [6, 2, 3, 8, 0, 5, 4, 7, 1],
        [8, 7, 5, 4, 0, 1, 0, 0, 0],
    ]
    easy_board_4 = [
        [1, 8, 4, 9, 6, 3, 7, 2, 5],
        [5, 6, 2, 7, 4, 8, 3, 1, 9],
        [3, 9, 7, 5, 1, 2, 8, 6, 4],
        [2, 3, 9, 6, 5, 7, 1, 4, 8],
        [7, 5, 6, 1, 8, 4, 2, 9, 3],
        [4, 1, 8, 2, 3, 9, 6, 5, 7],
        [9, 4, 1, 3, 7, 6, 5, 8, 2],
        [6, 2, 0, 0, 9, 5, 4, 7, 1],
        [8, 7, 5, 4, 2, 1, 9, 3, 6],
    ]
    easy_board_5 = [
        [0, 8, 4, 9, 6, 3, 7, 2, 0],
        [5, 6, 2, 7, 4, 8, 3, 1, 9],
        [3, 9, 7, 5, 1, 2, 8, 6, 4],
        [2, 3, 9, 6, 5, 7, 1, 4, 8],
        [7, 5, 6, 1, 8, 4, 2, 9, 3],
        [4, 1, 8, 2, 3, 9, 6, 5, 7],
        [9, 4, 1, 3, 7, 6, 5, 8, 2],
        [6, 2, 3, 8, 9, 5, 4, 7, 1],
        [0, 7, 5, 4, 2, 1, 9, 3, 0],
    ]
    easy_board_solution = [
        [1, 8, 4, 9, 6, 3, 7, 2, 5],
        [5, 6, 2, 7, 4, 8, 3, 1, 9],
        [3, 9, 7, 5, 1, 2, 8, 6, 4],
        [2, 3, 9, 6, 5, 7, 1, 4, 8],
        [7, 5, 6, 1, 8, 4, 2, 9, 3],
        [4, 1, 8, 2, 3, 9, 6, 5, 7],
        [9, 4, 1, 3, 7, 6, 5, 8, 2],
        [6, 2, 3, 8, 9, 5, 4, 7, 1],
        [8, 7, 5, 4, 2, 1, 9, 3, 6],
    ]

    one_clue_board = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    solved_board = [
        [1, 2, 3, 4, 5, 6, 8, 9, 7],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [8, 9, 7, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 3, 9, 8, 6, 7, 5],
        [3, 8, 9, 5, 6, 7, 2, 1, 4],
        [6, 7, 5, 2, 1, 4, 9, 3, 8],
        [9, 3, 8, 6, 7, 1, 5, 4, 2],
        [5, 4, 1, 8, 3, 2, 7, 6, 9],
        [7, 6, 2, 9, 4, 5, 3, 8, 1]
    ]

    # invalid first row
    invalid_board_1 = [
        [1, 0, 1, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 5, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 8, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 4, 0],
        [3, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 5, 0, 0],
    ]

    # invalid first column
    invalid_board_2 = [
        [1, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 5, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 8, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 4, 0],
        [3, 0, 0, 0, 9, 0, 0, 0, 0],
        [2, 0, 0, 6, 0, 0, 5, 0, 0],
    ]

    # invalid middle box
    invalid_board_3 = [
        [1, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 2, 0, 9],
        [0, 5, 0, 0, 9, 3, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 8, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 4, 0],
        [3, 0, 0, 0, 9, 0, 0, 0, 0],
        [2, 0, 0, 6, 0, 0, 5, 0, 0],
    ]

    empty_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    almost_empty_board_1 = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    almost_empty_board_2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    almost_empty_board_3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0]
    ]

    almost_empty_board_4 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0]
    ]

    almost_empty_board_5 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0]
    ]

    left_board = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    bot_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    outside_board_1 = [
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 9, 0, 4, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    outside_board_2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 6, 0, 0, 0, 0, 4, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def test_board_to_state(self):
        state = sudoku.board_to_state(TestSudoku.one_clue_board)
        self.assertEqual(len(state[0]), 9)
        self.assertEqual(len(state[0][0]), 9)
        self.assertEqual(state[0][1], 1)

    def test_invalid_1(self):
        state = sudoku.solve_board(TestSudoku.invalid_board_1)
        self.assertEqual(state, 'Input board is invalid!')

    def test_invalid_2(self):
        state = sudoku.solve_board(TestSudoku.invalid_board_2)
        self.assertEqual(state, 'Input board is invalid!')

    def test_invalid_3(self):
        state = sudoku.solve_board(TestSudoku.invalid_board_3)
        self.assertEqual(state, 'Input board is invalid!')

    def test_easy_1(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.easy_board_1), TestSudoku.easy_board_solution)

    def test_easy_2(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.easy_board_2), TestSudoku.easy_board_solution)

    def test_easy_3(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.easy_board_3), TestSudoku.easy_board_solution)

    def test_easy_4(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.easy_board_4), TestSudoku.easy_board_solution)

    def test_easy_5(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.easy_board_5), TestSudoku.easy_board_solution)

    def test_empty(self):
        sudoku.solve_board(TestSudoku.empty_board)

    def test_solve_completed(self):
        sudoku.solve_board(TestSudoku.solved_board)

    def test_almost_empty_1(self):
        sudoku.solve_board(TestSudoku.almost_empty_board_1)

    def test_almost_empty_2(self):
        sudoku.solve_board(TestSudoku.almost_empty_board_2)

    def test_almost_empty_3(self):
        sudoku.solve_board(TestSudoku.almost_empty_board_3)

    def test_almost_empty_4(self):
        sudoku.solve_board(TestSudoku.almost_empty_board_4)

    def test_almost_empty_5(self):
        sudoku.solve_board(TestSudoku.almost_empty_board_5)

    def test_left(self):
        sudoku.solve_board(TestSudoku.left_board)

    def test_bot(self):
        sudoku.solve_board(TestSudoku.bot_board)

    def test_outside_1(self):
        sudoku.solve_board(TestSudoku.outside_board_1)

    def test_outside_2(self):
        sudoku.solve_board(TestSudoku.outside_board_2)

if __name__ == '__main__':
    unittest.main()
