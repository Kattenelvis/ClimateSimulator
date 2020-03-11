import xlsxwriter
from simulation.PlanetaryGrid import PlanetaryGrid
from excel import printGrid, outputFileManagment


grid = PlanetaryGrid(x=30,y=30,z=4,tempAmplitude=22.0,baseTemp=3.0)
book = xlsxwriter.Workbook("out.xlsx")

#Runs the simulation for b time ticks
b = 300 #100 per day if delta T is 0.01
for _ in range(b):
    printGrid(book, grid)
    grid.tiles = grid.timeStep()

book.close()
outputFileManagment()
