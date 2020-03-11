class GridTile():
    def __init__(self, x, y, z, temperature):
        self.position = (x,y,z) #Position Tuple
        self.temperature = temperature #Average grid tile temperature
        self.neighbours = []


    def __repr__(self):
        return "grid tile with position x="+str(self.position[0])+" y="+str(self.position[1])+" and temperature="+str(self.temperature)+"C"

