import xlrd
import csv
di_file = ["ภาคกลาง", "ภาคเหนือ"]
def convert_xls_to_csv(filenames):
    book = xlrd.open_workbook(filenames)
    book_sheet = book.sheet_by_index(0)
    data = {book_sheet.cell_value(3, i)[:4]:int(book_sheet.cell_value(6, i)) for i in range(2, book_sheet.ncols-1)}
    with open('names.csv', 'w', newline='') as fp:
        fieldnames = [i for i in sorted(data)]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
