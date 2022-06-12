'''
Imagine working on software that determines the winner 
of a game of Tic Tac Toe. Create a function named 
tic_tac_toe_winner that is responsible for determing 
the state of a Tic Tac Toe board - Either there's no 
winner, it's a tie, 'X' won, or 'O' won. This function 
should take in 3x3 board as a parameter. Each element 
is either an 'X', 'O', or empty string ''. This function 
should have a return value of the winner 'X' or 'O', 'Tie' 
(for a full board with no winner), 
or None (for a game that is still in progress).

tablero= [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]
respuesta= "tie"

tablero=[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', '']
]
respuesta= "0"

tablero= [
    ['X', '', 'O'],
    ['O', 'X', 'X'],
    ['', '', '']
]
respuesta="None"
'''
'''
create a counter
create a tider
In a nested loop iterathe inner loop and compare
the first with the rest to the element in the same inner array are equals.
if all of them are equals, return the element is getting compare.
if found " " update a counter
if no one is equals and counter>4 return None
Else compare if in all arrays in the same position the element is equal
if one of them true return the elemen is iterating.
if no one is equals and counter>4 return None
else if elem in [1][1]==[2][2]==[3][3] of [1][3]==[2][2]=[3][1]
return the element is in those positions.


'''
'''
Board looks like

[
    [0,0  0,1  0,2],
    [1,0  1,1  1,2],
    [2,0  2,1  2,2]
]
'''



board =[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', 'O']
]


#horizontal
for row in range(len(board)):
    current = board[row][0]
    for col in range(1, len(board)):
        if current == board[row][col] and board[row][col]!='':
            current=board[row][col]
            if col+1==len(board[row]):
                print (f'The winner isw {current}')
                break
        else:
            break
#vertical
for col in range(len(board)):
    current = board[0][col]
    for row in range(1, len(board)):
        if current == board[row][col] and board[row][col]!='':
            current=board[row][col]
            if row+1==len(board[col]):
                print (f'The winner isa {current}')
                break
        else:
            break
        
#diag incrementing        
diag=board[0][0]
for coor in range(1, len(board)):
    if board[coor][coor]==diag and board[coor][coor]!='':
        diag=board[coor][coor]
        if coor+1==len(board):
            print (f'The winner isd {diag}')
            break
    else:
        break


#diag decrementing
diag=board[len(board)-1][0]
forw=1
for coor in range(len(board)-2, -1, -1):
    if board[coor][forw]==diag and board[coor][forw]!='':
        diag=board[coor][forw]
        if coor==0:
            print (f'The winner isc {diag}')
            break
    else:
        break
    forw+=1 

for rows in board:
    for empty in rows:
        if empty=='':
            print('None')
print('Tie')


'''
the time complexity of this problem is O(n^2) where n is the numer fo columns and rows
and the space complexity is lineal because this is not creating a new matrix or increasing the size of the original one.
'''