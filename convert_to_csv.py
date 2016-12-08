import os, xlrd, csv
from iso3166th import *
out_path = "./data_csv/"
region_folder = ["ภาคกลาง", "ภาคเหนือ", "ภาคตะวันออกเฉียงเหนือ", "ภาคใต้"]
num_year = [str(i) for i in range(2549, 2559)]
names_data = ['all_avg', 'all_home', 'all_sgs', 'all_mgs', 'all_lgs']
top_10 = {'all':{}, 'business':{}}
data_all = {}
region_per = {key:{'first':[], 'last':[]} for key in ['region_central', 'region_north',\
 'region_northeast', 'region_east', 'region_west', 'region_south']}

# Create New Directory
if not os.path.exists(out_path):
    os.makedirs(out_path+'conclude')

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
    data_all[filename[:-4]] = {names_data[i]:{y:data[y][i] for y in sorted(data) if data[y][i] != 'None'} for i in range(5)}
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

# Success Provice Files Convert
print("============ All Converted Complete")

# -------------------------------- Conclude Data Convert ----------------------------------

avg = {name:{key:[data_all[i][name][key] for i in data_all if key in data_all[i][name]]\
        for key in num_year} for name in names_data}
avg = {key:{year:sum(avg[key][year])//len(avg[key][year]) for year in avg[key]} for key in avg}
top_10['all'] = {name:[data_all[name]['all_avg'][year] for year in data_all[name]['all_avg']] for name in data_all}
top_10['all'] = {key:sum(top_10['all'][key])//len(top_10['all'][key]) for key in data_all}
for i in data_all:
    for n in names_data[2:5]:
        for year in data_all[i][n]:
            if i in top_10['business']:
                top_10['business'][i].append(data_all[i][n][year])
            else:
                top_10['business'][i] = [(data_all[i][n][year])]
top_10['business'] = {key:sum(top_10['business'][key])//len(top_10['business'][key]) for key in top_10['business']}
top_all = sorted(top_10['all'], key=top_10['all'].get, reverse=1)[:10]
top_business = sorted(top_10['business'], key=top_10['business'].get, reverse=1)[:10]
for keyn in data_all:
    reg_n = sorted(list(data_all[keyn]['all_avg'].keys()))
    region_per[check_region(keyn)]['first'].append(data_all[keyn]['all_avg'][reg_n[0]])
    region_per[check_region(keyn)]['last'].append(data_all[keyn]['all_avg'][reg_n[-1]])
region_per = {n:((sum(region_per[n]['last'])-sum(region_per[n]['first']))*100)/sum(region_per[n]['first'])\
             for n in region_per}

# -------------------------------- Save Data To Files ----------------------
# Convert Data of All average
with open(out_path+'conclude/all_avg.csv', 'w', newline='') as fp:
        fieldnames = num_year
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(5):
            writer.writerow({y:avg[names_data[i]][y] for y in avg[names_data[i]]})
        print("All Average Created!")

# Convert Data of Top10 Rank
with open(out_path+'conclude/top10_avg.csv', 'w', newline='') as fp:
        fieldnames = [i for i in range(1, 11)]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({i:top_all[i-1] for i in range(1, 11)})
        writer.writerow({i:top_10['all'][top_all[i-1]] for i in range(1, 11)})
        writer.writerow({i:top_business[i-1] for i in range(1, 11)})
        writer.writerow({i:top_10['business'][top_business[i-1]] for i in range(1, 11)})
        print("Top10 Rank Created!")

# Convert Data of Increased rates by region
with open(out_path+'conclude/region_up_avg.csv', 'w', newline='') as fp:
        fieldnames = [convert_to_th(i) for i in region_per]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({convert_to_th(i):region_per[i] for i in region_per})
        print("Region Rank Created!")
