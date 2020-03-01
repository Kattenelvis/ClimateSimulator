import xlsxwriter
import math

class gridTile():
    def __init__(self, x, y, z, temperature):
        self.position = (x,y,z) #Position Tuple
        self.temperature = temperature #Average grid tile temperature
        self.neighbours = []


    def __repr__(self):
        return "grid tile with position x="+str(self.position[0])+" y="+str(self.position[1])+" and temperature="+str(self.temperature)+"C"


class PlanetaryGrid():
    def __init__(self, x, y, z):
        self.size = (x,y,z)
        self.tiles = []
        self.__generateGrid()


    def __repr__(self):
        return "Earth Grid with size x="+str(self.size[0])+" y="+str(self.size[1])


    def __generateGrid(self):
        for y in range(self.size[1]):
            self.tiles.append([])
            for x in range(self.size[0]):
                tile = gridTile(x,y,0,15.0)#math.cos(y)) Gona use sine waves to represent the polar regions vs the equator
                self.tiles[y].append(tile)


    def findNeighbours(self, x, y):
        n = [-1, 0, 1]
        neighbors = []
        for y in range(3):
            for x in range(3):
                try:
                    neighbours.append(self.tiles[x+n[j]][y+n[i]])
                except:
                    pass
        return neighbors


def printGrid(grid, book):
    sheet = book.add_worksheet()
    for x in range(grid.size[0]-1):
        for y in range(grid.size[1]-1):
            sheet.write(x,y,grid.tiles[x+1][y+1].temperature)  
                    
    return sheet

book = xlsxwriter.Workbook("out.xlsx")
e = PlanetaryGrid(8,8,4)
sheet = printGrid(e, book)
book.close()
print(e.findNeighbours(3,3))