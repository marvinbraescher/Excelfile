# Import module
import xlrd


def main1():
    # Open excel
    wb = xlrd.open_workbook('BD1.xls')

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
                for x in range(0, coluns):
                    bd2 = sh.cell(i, x).value

        return bd2
