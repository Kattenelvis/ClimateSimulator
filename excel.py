import xlsxwriter

def printGrid(book, grid):
    sheet = book.add_worksheet()
    for x in range(grid.size[0]-1):
        for y in range(grid.size[1]-1):
            sheet.write(x,y,grid.tiles[x+1][y+1].temperature)  
                    
    return sheet


def tempColor(book, temp):
    pass