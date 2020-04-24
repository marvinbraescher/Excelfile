# Import module
from xlrd import open_workbook


bd2 = list(range(0,300))
# Open excel
wb = open_workbook('BD1.xls')

# Select table
sh = wb.sheet_by_name('Sheet1')

# Min and max row/column
coluns = sh.ncols
rows = sh.nrows

# Search word
word = input('Search: ')

# Load all table
for i in range(0, rows):
    for j in range(0, coluns):
        c = sh.cell(i, j)
        # Find the search
        if str(c.value).lower().find(word.lower()) != -1:
            cont = 0
            cont = cont + 1
            for x in range(0, coluns):
                bd2[cont] = sh.cell(i, x).value
                print(bd2[cont])

