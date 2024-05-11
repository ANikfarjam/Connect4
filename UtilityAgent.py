class UtilityAgent:
    def __init__(self, board, Player, Agent):
        self.board = board 
        self.player = Player #state of players pieces
        self.agent =Agent #state od Agent pieces
    
class Node:
    def __init__(self, value = None, childeren=[]):
        self.max_value = value
        self.child = childeren
    def add_Node(self, Node):
        self.child.append(Node)
    def get_value(self):
        return self.max_value
def apha_beta_search(board, depth_limit, ):
    pass
def construct_tree(board):#new board state/return index of witch column we add the next peace
    pass

