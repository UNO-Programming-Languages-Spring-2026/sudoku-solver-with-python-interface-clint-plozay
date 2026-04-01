from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        board = [[0 for j in range(9)] for i in range(9)]
        for k, v in self.sudoku.items():
            board[k[0] - 1][k[1] - 1] = v 
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                s = s + str(board[r][c])
                if (c + 1) % 3 == 0:
                    s = s + '  '
                else:
                    s = s + ' '
            if (r + 1) % 3 == 0:
                s = s + '\n\n'
            else:
                s = s + '\n'

        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        print(s)
        val_rows = [ r.strip() for r in s.split('\n') if len(r) > 0]
        val_rows2 = []
        for row in val_rows:
            values = [ v for v in row.split(' ') if v != '' ]
            val_rows2.append(values)

        val_rows = val_rows2
        print(val_rows)
        for r in range(len(val_rows)):
            for c in range(len(val_rows[0])):
                if val_rows[r][c] != '-':
                    sudoku[(r + 1,c + 1)] = int(val_rows[r][c])
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        atoms = model.symbols(shown=True)
        board = {}
        for atom in atoms:
            args = atom.arguments
            board[(args[0].number, args[1].number)] = args[2].number
        
        return cls(board)
    
   
