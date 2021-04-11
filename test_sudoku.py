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

    @staticmethod
    def fits(board, solution):
        if isinstance(solution, str):
            return False
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if solution[i][j] != val:
                        return False
        return True

    def test_fits(self):
        self.assertFalse(TestSudoku.fits(self.easy_board_1, self.outside_board_1))
        self.assertTrue(TestSudoku.fits(self.easy_board_1, self.easy_board_solution))

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
        result = sudoku.solve_board(TestSudoku.empty_board)
        self.assertTrue(TestSudoku.fits(TestSudoku.empty_board, result))

    def test_solve_completed(self):
        result = sudoku.solve_board(TestSudoku.solved_board)
        self.assertTrue(TestSudoku.fits(TestSudoku.solved_board, result))

    def test_almost_empty_1(self):
        result = sudoku.solve_board(TestSudoku.almost_empty_board_1)
        self.assertTrue(TestSudoku.fits(TestSudoku.almost_empty_board_1, result))

    def test_almost_empty_2(self):
        result = sudoku.solve_board(TestSudoku.almost_empty_board_2)
        self.assertTrue(TestSudoku.fits(TestSudoku.almost_empty_board_2, result))

    def test_almost_empty_3(self):
        result = sudoku.solve_board(TestSudoku.almost_empty_board_3)
        self.assertTrue(TestSudoku.fits(TestSudoku.almost_empty_board_3, result))

    def test_almost_empty_4(self):
        result = sudoku.solve_board(TestSudoku.almost_empty_board_4)
        self.assertTrue(TestSudoku.fits(TestSudoku.almost_empty_board_4, result))

    def test_almost_empty_5(self):
        result = sudoku.solve_board(TestSudoku.almost_empty_board_5)
        self.assertTrue(TestSudoku.fits(TestSudoku.almost_empty_board_5, result))

    def test_left(self):
        result = sudoku.solve_board(TestSudoku.left_board)
        self.assertTrue(TestSudoku.fits(TestSudoku.left_board, result))

    def test_bot(self):
        result = sudoku.solve_board(TestSudoku.bot_board)
        self.assertTrue(TestSudoku.fits(TestSudoku.bot_board, result))

    def test_outside_1(self):
        result = sudoku.solve_board(TestSudoku.outside_board_1)
        self.assertTrue(TestSudoku.fits(TestSudoku.outside_board_1, result))

    def test_outside_2(self):
        result = sudoku.solve_board(TestSudoku.outside_board_2)
        self.assertTrue(TestSudoku.fits(TestSudoku.outside_board_2, result))

    @unittest.skip
    def test_lots(self):
        text_boards = [
            '050083017000100400304005608000030009090824500006000070009000050007290086103607204',
            '206030000001065070047108050500000029008019406000420001000042800609300005070000013',
            '004502178100090030000800004600450000070900012801203500400000009350060807090300620',
            '590000147000900008072000030700040290020030806800170050005764009036005000100800002',
            '900084060604005207030070080760001500053000001000409603105026090002040000800003710',
            '680905000003000508402108703390720800000000010045006900060804002001002075700013000',
            '000340002006082073700100450082005014000098300670000005140700000905030020030000806',
            '600050000073008020854027000201700530400069007080000900027301084060540009300000001',
            '007500904000082305001600002800036070016004200430190050540008000029071030000000609',
            '000000008003000400090020060000079000000061200060502070008000500010000020405000003',
            '000000002008010900500003040000109300060030080003700000040000005301070800200000000',
            '002000700010000060500000018000037000000049000004102300003020900080000050600000002',
            '000000007004020600800000310000002900040090030009506000010000008006050200700000060',
            '004003000070080000208100006003000090080020000100700003000000450000800900009005008',
            '006001000050030000900400007001000020030090000400500001300000680000300200002008003',
            '000000003001009060050080400000900080008670000010000200006007020030800500400000008',
            '000000005006008700300000090000107040007000800040006000090080003001600400500020000',
            '000005003009000040081040000000700000004002006800014030000000200040006007900050010',
        ]
        for text_board in text_boards:
            board = sudoku.text_to_board(text_board)
            result = sudoku.solve_board(board)
            self.assertTrue(TestSudoku.fits(board, result))
            print(result)


if __name__ == '__main__':
    unittest.main()
