import xlsxwriter
from simulation.PlanetaryGrid import PlanetaryGrid
from excel import printGrid
from shutil import move

grid = PlanetaryGrid(x=25,y=25,z=4,tempAmplitude=22.0,baseTemp=3.0)
book = xlsxwriter.Workbook("out.xlsx")

#Runs the simulation for b time ticks
b = 20
for _ in range(b):
    printGrid(book, grid)
    grid.tiles = grid.timeStep()

book.close()

from os import getcwd, mkdir, rmdir, removedirs


removedirs(getcwd()+"/output")