import xlsxwriter
from math import e, floor

def printGrid(book, grid):
    sheet = book.add_worksheet()
    for x in range(grid.size[0]-1):
        for y in range(grid.size[1]-1):
            temperature = grid.tiles[x+1][y+1].temperature

            #Check out the color graph equation here https://www.desmos.com/calculator/vikit8n7zd
            amplitude = 99
            smoothFunction = 20
            red = (amplitude / (1 + e**(-temperature/smoothFunction))) + 10 
            blue = (amplitude / (1 + e**(temperature/smoothFunction))) + 10
            color = f"#{floor(red)}00{floor(blue)}"
            
            format1 = book.add_format({'bg_color':color, 'font_color':'white'})
            sheet.write(x,y,temperature, format1)
        
    return sheet


def outputFileManagment():
    from os import getcwd, mkdir, rmdir, path, remove
    from shutil import move

    if not path.exists(getcwd()+"/output"):
        mkdir(getcwd()+"/output")

    if path.exists(getcwd()+"/output/out.xlsx"):
        remove(getcwd()+"/output/out.xlsx")
    move(getcwd()+"/out.xlsx", getcwd()+"/output")