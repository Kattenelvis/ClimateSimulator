import xlsxwriter


class gridTile():
    def __init__(self, x, y, z, temperature):
        self.position = (x,y,z) #Position Tuple
        self.temperature = temperature #Average grid tile temperature
        self.neighbours = []

    def __repr__(self):
        return "grid tile with position x="+str(self.position[0])+" y="+str(self.position[1])+" and temperature="+str(self.temperature)+"C"


class earthGrid():
    def __init__(self, x, y, z):
        self.size = (x,y,z)
        self.tiles = []
        self.__generateGrid()

    def __repr__(self):
        return "Earth Grid with size x="+str(self.size[0])+" y="+str(self.size[1])


    def __generateGrid(self):
        for x in range(self.size[0]):
            self.tiles.append([])
            for y in range(self.size[1]):
                tile = gridTile(x,y,0,15+x+y)
                self.tiles[x].append(tile)


def printGrid(grid, book):
    sheet = book.add_worksheet()
    for x in range(grid.size[0]-1):
        for y in range(grid.size[1]-1):
            sheet.write(x,y,grid.tiles[x+1][y+1].temperature)  
                    
    return sheet

book = xlsxwriter.Workbook("out.xlsx")
e = earthGrid(8,8,4)
sheet = printGrid(e, book)
book.close()