import pygal, csv, os
from pygal.style import RotateStyle
chart_style1 = RotateStyle('#E86FA0')
chart_style2 = RotateStyle('#81CFE0')
name_y = ['บ้านอยู่อาศัย', 'กิจการขนาดเล็ก', 'กิจการขนาดกลาง', 'กิจการขนาดใหญ่', 'อื่นๆ']
out_path = "./chart_f/"
mydir = "./data_csv/"

def data_prot(filename):
    """prot chart from input csv file"""
    with open(mydir+filename) as fp:
        reader = csv.DictReader(fp)
        num = [i for i in (reader.fieldnames)]

        chart_1 = pygal.StackedLine(fill=True, interpolate='cubic', style=chart_style1, show_legend=False)
        chart_1.value_formatter = lambda x: "%gM" %(x/(10**6))
        chart_1.x_labels = num
        data = next(reader)
        chart_1.add(None, [int(data[i]) if data[i] != 'None' else None for i in num], \
            allow_interruptions=True,  formatter=lambda y: "{:,.0f}(kWh)".format(y))
        chart_1.render_to_file(out_path+filename[:-4]+'_chart_1.svg')
        chart_2 = pygal.Bar(legend_at_bottom=True)
        chart_2.value_formatter = lambda x: "%gM" %(x/(10**6))
        chart_2.x_labels = num
        for i in range(5):
            data = next(reader)
            chart_2.add(name_y[i], [int(data[i]) if data[i] != 'None' else None for i in num], \
                allow_interruptions=True,  formatter=lambda y: "{:,.0f}(kWh)".format(y))
        chart_2.render_to_file(out_path+filename[:-4]+'_chart_2.svg')
        print("\tSuccess!")

# Create New Directory
if not os.path.exists(out_path):
    os.makedirs(out_path)
# Loop for run list filenames in dir
for file in os.listdir(mydir):
    if file.endswith(".csv"):
        print("Opening.. "+file, end='')
        data_prot(file)

# --------------------- Conclude Chart Prot ---------------------------

# Chart all average provice in Thailand use
with open(mydir+'conclude/all_avg.csv') as fp:
    reader = csv.DictReader(fp)
    num = [i for i in (reader.fieldnames)]
    chart_avg = pygal.StackedLine(fill=True, interpolate='cubic', style=chart_style2, show_legend=False)
    chart_avg.value_formatter = lambda x: "%gM" %(x/(10**6))
    chart_avg.x_labels = num
    data = next(reader)
    chart_avg.add(None, [int(data[i]) if data[i] != 'None' else None for i in num], \
        allow_interruptions=True,  formatter=lambda y: "{:,.0f}(kWh)".format(y))
    chart_avg.render_to_file(out_path+'allavg_chart.svg')
    print("Chart_All_Average Success!")

    chart_avg2 = pygal.Bar(legend_at_bottom=True)
    chart_avg2.value_formatter = lambda x: "%gM" %(x/(10**6))
    chart_avg2.x_labels = num
    for i in range(4):
        data = next(reader)
        chart_avg2.add(name_y[i], [int(data[i]) if data[i] != 'None' else None for i in num], \
            allow_interruptions=True,  formatter=lambda y: "{:,.0f}(kWh)".format(y))
    chart_avg2.render_to_file(out_path+'sub_avg_chart.svg')
    print("Chart_All_Type_Average Success!")

# Chart Top10 Rank all average and business use
with open(mydir+'conclude/top10_avg.csv') as fp:
    reader = csv.DictReader(fp)
    num = [i for i in (reader.fieldnames)]
    chart_top10 = pygal.Bar(legend_at_bottom=True)
    chart2_top10 = pygal.HorizontalBar()
    chart_top10.value_formatter = lambda x: "%gM" %(x/(10**6))
    chart2_top10.value_formatter = lambda x: "%gM" %(x/(10**6))
    data = next(reader)
    top_name = {int(k):v for k,v in data.items()}
    data = next(reader)
    top_val = {int(k):v for k,v in data.items()} 
    for i in range(1, 11):
        chart_top10.add(top_name[i], int(top_val[i]), allow_interruptions=True,  formatter=lambda y: "{:,.0f}(kWh)".format(y))
    data = next(reader)
    top_name = {int(k):v for k,v in data.items()}
    data = next(reader)
    top_val = {int(k):v for k,v in data.items()} 
    for i in range(1, 11):
        chart2_top10.add(top_name[i], int(top_val[i]), allow_interruptions=True,  formatter=lambda y: "{:,.0f}(kWh)".format(y))
    chart_top10.render_to_file(out_path+'rank_chart.svg')
    print("Chart_Rank Success!")
    chart2_top10.render_to_file(out_path+'rank_chart_business.svg')
    print("Chart_Rank_Business Success!")

# Chart Increased rates by region
with open(mydir+'conclude/region_up_avg.csv') as fp:
    reader = csv.DictReader(fp)
    rname = ['ภาคกลาง', 'ภาคตะวันออก', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคใต้', 'ภาคตะวันตก', 'ภาคเหนือ']
    chart_region = pygal.Bar(legend_at_bottom=True)
    chart_region.value_formatter = lambda x: "%d%%" %x
    data = next(reader)
    for i in rname:
        chart_region.add(i, float(data[i]), allow_interruptions=True,  formatter=lambda y: "%.2f%%"%y)
    chart_region.render_to_file(out_path+'region_chart.svg')
    print("Chart_Region Success!")
