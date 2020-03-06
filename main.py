import xlsxwriter
from simulation import PlanetaryGrid
from excel import printGrid

e = PlanetaryGrid(40,40,4)
book = xlsxwriter.Workbook("out.xlsx")
for _ in range(10):
    printGrid(e, book)
    e.tiles = e.timeStep()


book.close()