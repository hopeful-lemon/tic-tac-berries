
class Game:
    def __init__(self, first='o'):
        self.grid = [['.' for k in range(3)] for n in range(3)]
        self.turn = first
        self.first = first
        self.game_over = False
    def get_turn(self): 
        return self.turn
    
    def next_turn(self):
        turns = ['o', 'x']
        self.turn = turns[(turns.index(self.turn) + 1) % 2]

    def play(self, x, y):
        if(self.game_over): return
        if self.grid[x][y] != '.':
            return
        self.grid[x][y] = self.turn
        self.next_turn()

    def check_win(self):
        
        def check_lines(g):
            for line in g:
                if(line.count('.')): continue
                xs = line.count('x')
                if not xs:
                    return 'o'
                elif xs == 3:
                    return 'x'
            return '.'

        # Lines
        winner = check_lines(self.grid)
        if(winner != '.'): 
            self.game_over = True
            return winner

        # Columns
        grid_T = [[self.grid[i][j] for i in range(3)] for j in range(3)]
        
        winner = check_lines(grid_T)
        if(winner != '.'):
            self.game_over = True
            return winner

        # Diagonals
        diags = []
        diags.append([self.grid[i][i] for i in range(3)])
        diags.append([self.grid[i][2-i] for i in range(3)])
        
        winner = check_lines(diags)
        if(winner != '.'):
            self.game_over = True
            return winner

        return '.'
    def reset(self):
        self.grid = [['.' for k in range(3)] for n in range(3)]
        self.turn = self.first
        self.game_over = False
