import xlsxwriter
from math import e, floor

def printGrid(book, grid):
    sheet = book.add_worksheet()
    for x in range(grid.size[0]-1):
        for y in range(grid.size[1]-1):
            temperature = grid.tiles[x+1][y+1].temperature

           
            red = (1 / (1 + e**temperature))
            color = f"#{floor(red)}00000" if red<10 else f"#{floor(red)}0000"

            
            format1 = book.add_format({'bg_color':color, 'font_color':'white'})
            sheet.write(x,y,temperature, format1)
        
    return sheet


def tempColor(book, temp):
    pass