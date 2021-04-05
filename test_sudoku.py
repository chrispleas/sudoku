import unittest
import sudoku


class TestSudoku(unittest.TestCase):
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
    one_clue_board_solution = [
        [2, 1, 3, 4, 5, 6, 8, 9, 7],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [8, 9, 7, 1, 2, 3, 4, 5, 6],
        [1, 2, 4, 3, 9, 8, 6, 7, 5],
        [3, 8, 9, 5, 6, 7, 2, 1, 4],
        [6, 7, 5, 2, 1, 4, 9, 3, 8],
        [9, 3, 8, 6, 7, 1, 5, 4, 2],
        [5, 4, 1, 8, 3, 2, 7, 6, 9],
        [7, 6, 2, 9, 4, 5, 3, 8, 1]
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
    empty_board_solution = [
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

    sparse_board = [
        [0, 0, 1, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 5, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 8, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 4, 0],
        [3, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 5, 0, 0],
    ]
    sparse_board_solution = [
        [4, 2, 1, 5, 3, 8, 9, 6, 7],
        [5, 8, 9, 1, 7, 6, 4, 3, 2],
        [7, 3, 6, 9, 4, 2, 1, 8, 5],
        [8, 6, 3, 4, 1, 5, 2, 7, 9],
        [9, 5, 7, 2, 8, 3, 6, 1, 4],
        [1, 4, 2, 7, 6, 9, 8, 5, 3],
        [2, 7, 5, 3, 5, 1, 3, 4, 8],
        [3, 1, 4, 8, 9, 4, 7, 2, 6],
        [1, 4, 8, 6, 2, 7, 5, 9, 3]
    ]

    def test_board_to_state(self):
        state = sudoku.board_to_state(TestSudoku.one_clue_board)
        self.assertEqual(len(state[0]), 9)
        self.assertEqual(len(state[0][0]), 9)
        self.assertEqual(state[0][1], 1)
        state = sudoku.board_to_state(TestSudoku.sparse_board)
        self.assertEqual(state[8][8], set(i for i in range(1, 10)))
        self.assertEqual(state[8][6], 5)

    def test_blank(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.empty_board), TestSudoku.empty_board_solution)

    def test_one_clue(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.one_clue_board), TestSudoku.one_clue_board_solution)

    def test_sparse(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.sparse_board), TestSudoku.sparse_board_solution)

    def test_solve_completed(self):
        self.assertEqual(sudoku.solve_board(TestSudoku.sparse_board_solution), TestSudoku.sparse_board_solution)


if __name__ == '__main__':
    unittest.main()
