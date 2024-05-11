import numpy as np
#in our game given following finctions that dictate the game moves and turns and ...
#S0 ===> The initial state, which specifies how the game is set up at the start
#in context of our game initial state would be an empty game board
#def toMove(s): --> The player whose turn it is to move in state s   
#def action(s): --> The set of legal moves in state s
#def result(s, a): ---> The transition model, which defines the state resulting from taking action a in state s
class ConnectFour:
    def __init__(self):
        self.Board = np.zeros((6, 7), dtype=int) #initial state or S0
        
    def toMove(self, who):
        if who=='Min': #player
            #for now im just adding some dummy values untill we figure our the GUI
            self.Board[-1,3] = -1 #because the player is minimizer
        else: 
            pass
            #construct tree
                #call minimax with defined bevth boundries
            #retrun board
    def available_moves(slef):#returns list of available moves
        pass
    