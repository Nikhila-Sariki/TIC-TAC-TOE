import random
# Win detecting algorithm
def win_algo(grid, computer, player):
    win = [[(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)], [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)]]
    
    for i in range(0,8):
        count =0
        flag=0
        for j in range(0,3):
            a,b = win[i][j]
            if grid[a][b] == computer:
                count+=1
            elif grid[a][b]== '?':
                x,y = a,b
                flag = 1
            else:
                flag = 0
        if count==2 and flag==1:
                grid[x][y]= computer
                
                return 1
    
    for i in range(0,8):
            count =0
            flag=0
            for j in range(0,3):
                a,b = win[i][j]
                if grid[a][b] == player:
                    count+=1
                elif grid[a][b]== '?':
                    x,y = a,b
                    flag = 1
                else:
                    flag = 0
            if count==2 and flag==1:
                    grid[x][y]= computer
                    flag_2 = 1
                    return 1

    available = []
    for i in range(0,3):
        for j in range(0,3):
            if grid[i][j] =='?':
               available.append((i,j))
        if available:
            i,j = random.choice(available)
            grid[i][j]= computer
        else:
            return -1
          

    
    


