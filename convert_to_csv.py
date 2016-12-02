import os, xlrd, csv
out_path = "./data_csv/"
region_folder = ["ภาคกลาง", "ภาคเหนือ", "ภาคตะวันออกเฉียงเหนือ", "ภาคใต้"]


if not os.path.exists(out_path):
    os.makedirs(out_path)

def convert_xls_to_csv(filename):
    """Convert xls file to CSV file in directory"""
    book = xlrd.open_workbook(mydir+filename)
    book_sheet = book.sheet_by_index(0)
    data = {}
    for i in range(2, book_sheet.ncols-1):
        if book_sheet.cell_type(3, i) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
            break
        data[book_sheet.cell_value(3, i)[:4]] = [int(book_sheet.cell_value(k, i)) if \
        type(book_sheet.cell_value(k, i)) == float else 'None' for k in range(6, 12)]
    with open(out_path+filename.replace('.xls', '.csv'), 'w', newline='') as fp:
        fieldnames = [i for i in sorted(data)]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(6):
            writer.writerow({k:data[k][i] for k in fieldnames})

# Loop for run list filenames in dir
for x in region_folder:
    mydir = "rows_data/"+x+"/"
    for file in os.listdir(mydir):
        if file.endswith(".xls"):
            convert_xls_to_csv(file)
            print("Convert-> "+file)

# Success Convert
print("============ All Converted Complete")
