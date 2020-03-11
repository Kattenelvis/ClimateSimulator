from math import cos, pi
from simulation.GridTile import GridTile

class PlanetaryGrid():
    
    def __init__(self, x=20, y=20, z=10, tempAmplitude=30, baseTemp=5):
        self.size = (x,y,z)
        self.tiles = []
        self.tempAmplitude = tempAmplitude
        self.baseTemp = baseTemp
        self.coolingAmplitude = 5
        self.__generateGrid()


    def __repr__(self):
        return "Earth Grid with size x="+str(self.size[0])+" y="+str(self.size[1])


    def __generateGrid(self):
        #Generates the grid
        for y in range(self.size[1]):
            self.tiles.append([])
            for x in range(self.size[0]):
                #The equation can be visualized here:
                # https://www.desmos.com/calculator/ogjhneip7o
                equator = self.size[0]/2
                temperature = self.baseTemp + self.tempAmplitude * cos(y*pi/equator + pi)
                tile = GridTile(x,y,0, temperature)
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


    def avgNeighbourTemp(self, x, y):
        tile = self.tiles[x][y]
        _sum = 0
        #Take the average temperature of sourrunding tiles and give that temperature to the tile
        for i in range(len(tile.neighbours)):
            _sum += tile.neighbours[i].temperature

        avg = _sum/len(tile.neighbours)
        return avg


    def timeStep(self):
        newTiles = self.tiles
        for y in range((self.size[1])):
            for x in range((self.size[0])):
                pass
                #Basic Thermodynamics
                newTiles[x][y].temperature = self.avgNeighbourTemp(x,y) - self.coolingAmplitude

        return newTiles