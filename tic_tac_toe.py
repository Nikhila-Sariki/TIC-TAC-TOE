import random
def decide_winner(grid):
    if (grid[0][0]== grid[1][1]== grid[2][2]=='X') or (grid[0][2]== grid[1][1]== grid[2][0]=='X') or (grid[0][0]==grid[0][1]==grid[0][2]== 'X') or (grid[1][0]==grid[1][1]==grid[1][2]== 'X') or (grid[2][0]==grid[2][1]==grid[2][2]=='X') or(grid[0][0]==grid[1][0]==grid[2][0]=='X') or (grid[0][1]== grid[1][1]== grid[2][1]=='X') or (grid[0][2]==grid[1][2]==grid[2][2]=='X') :
        return 'X'
    elif (grid[0][0]== grid[1][1]== grid[2][2]=='O') or (grid[0][2]== grid[1][1]== grid[2][0]=='O') or (grid[0][0]==grid[0][1]==grid[0][2]=='O') or (grid[1][0]==grid[1][1]==grid[1][2]=='O') or (grid[2][0]==grid[2][1]==grid[2][2]=='O') or (grid[0][0]==grid[1][0]==grid[2][0]=='O') or (grid[0][1]== grid[1][1]== grid[2][1]=='O') or (grid[0][2]==grid[1][2]==grid[2][2]=='O'):
       return 'O'
    else:
        return 0
def display_grid(grid):
    for row in grid:
        print(*row)
    print("\n")
play= 'Y'
while play == 'Y' or play == 'y' :
 print("----------TIC TAC TOE----------")
 
 grid = [['?','?', '?'], ['?', '?', '?'], ['?', '?', '?']]
 choice= input("Choose an option, O or X ")
 if choice== 'X':
    player= 'X'
    computer= 'O'
 else:
    player= 'O'
    computer= 'X'
 while any('?' in row for row in grid):
  display_grid(grid)
  r= int(input("Enter the row you want to select:"))
  c= int(input("Enter the column you want to select:"))
  while(grid[r-1][c-1]!= '?') or (r<1) or (r>3) or (c<1) or (c>3):
     print("INVALID MOVE, please enter your choice again")
     r= int(input("Enter the row you want to select:"))
     c= int(input("Enter the column you want to select:"))
  grid[r-1][c-1]= player
   
  display_grid(grid)
  if(decide_winner(grid)== player):
     break
  available = []
  for i in range(0,3):
   for j in range(0,3):
     if grid[i][j] =='?':
       available.append((i,j))
  if available:
    i,j = random.choice(available)
    grid[i][j]= computer
  else: 
     break
  
  if(decide_winner(grid)== computer):
       display_grid(grid)
       break
     
 if decide_winner(grid)== computer:
    print("Oops, you lost the game!")
 elif decide_winner(grid)== player:
    print("Congratulations! You won!")
 else:
    print("IT'S A TIE!")
 play= input("Do you wanna play again: (Y/N):")



       