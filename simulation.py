import xlsxwriter
from math import sin, pi

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
        #Generates the grid
        for y in range(self.size[1]):
            self.tiles.append([])
            for x in range(self.size[0]):
                temperature = 15.0+5*sin(y-pi*0.9)
                tile = gridTile(x,y,0, temperature)
                self.tiles[y].append(tile)

        #The neighbors need to be scanned after the grid is done
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.tiles[x][y].neighbours = self.getNeighbours(x,y)


    def getNeighbours(self, x, y):
        n = [-1, 0, 1]
        neighbors = []
        for i in range(3):
            for j in range(3):
                try:
                    if (self.tiles[x+n[i]][y+n[j]] != self.tiles[x][y]):
                        neighbors.append(self.tiles[x+n[i]][y+n[j]])
                except:
                    continue
        return neighbors


    def avgTemperature(self, x, y):
        tile = self.tiles[x][y]
        tile.neighbours


    def timeStep(self, dt):
        pass



def printGrid(grid, book):
    sheet = book.add_worksheet()
    for x in range(grid.size[0]-1):
        for y in range(grid.size[1]-1):
            sheet.write(x,y,grid.tiles[x+1][y+1].temperature)  
                    
    return sheet


def timeStep(book):
    sheet = printGrid(e, book)
    return sheet



e = PlanetaryGrid(8,8,4)
book = xlsxwriter.Workbook("out.xlsx")
timeStep(book)
timeStep(book)
timeStep(book)
book.close()