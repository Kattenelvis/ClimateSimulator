import xlsxwriter
from simulation import PlanetaryGrid
from excel import printGrid

grid = PlanetaryGrid(40,40,4)
book = xlsxwriter.Workbook("out.xlsx")

#Runs the simulation for b time ticks
b = 10
for _ in range(b):
    printGrid(book, grid)
    grid.tiles = grid.timeStep()


book.close()