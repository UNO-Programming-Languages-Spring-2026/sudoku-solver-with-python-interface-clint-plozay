% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

values(1..9).
row(1..9).
col(1..9).

%deal with initial
sudoku(R,C,V) :- initial(R,C,V).

%every cell can only have one number assigned to it
%sudoku(1,1,1) sudoku(1,1,2)
1 { sudoku(R, C, V) : values(V) } 1 :- row(R), col(C).

%every row needs 1 of each number
%it is not the case that atoms with the same R and V values do not also have the same C values
:- sudoku(R, C1, V), sudoku(R, C2, V), C1 != C2.

%Every col needs 1 of a number
%it is not the case that for every column and number, that there should be more than one row with that number
:- sudoku(R1, C, V), sudoku(R2, C, V), R1 != R2.

%origin is top left, in subgrid(R, C) where R = row, C = col

subgrid(R, C, G) :- row(R), col(C), BR = (R-1)/3, BC = (C-1)/3, G = BR*3 + BC + 1.

%each subgrid may only have one of each number
%sudoku(1,1,1) sudoku(1,2,1)
:- sudoku(R, C, V), sudoku(R1, C1, V), subgrid(R, C, G), subgrid(R1, C1, G1), G = G1, R != R1, C != C1.


#show sudoku/3.