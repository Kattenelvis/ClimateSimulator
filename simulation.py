from math import cos, pi

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
                #The equation can be visualized here:
                # https://www.desmos.com/calculator/ogjhneip7o
                q = self.size[0]/2
                a = 20
                b = 5
                temperature = b + a * cos(y*pi/q + pi) 
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
                newTiles[x][y].temperature = self.avgNeighbourTemp(x,y)

        return newTiles