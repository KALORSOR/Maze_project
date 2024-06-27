# simple maze layout

class Maze:
    def __init__(self):
        self.layout = [
            "##########",
            "#        #",
            "# ###### #",
            "# #    # #",
            "# # ## # #",
            "# # ## # #",
            "#      # #",
            "##########"
        ]
    
    def is_wall(self, x, y):
        return self.layout[y][x] == '#'

