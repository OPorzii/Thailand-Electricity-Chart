import pygal, csv, os
from pygal.style import RotateStyle
dark_rotate_style = RotateStyle('#3498db')
name_y = ['บ้านอยู่อาศัย', 'กิจการขนาดเล็ก', 'กิจการขนาดกลาง', 'กิจการขนาดใหญ่']
out_path = "./chart_f/"
mydir = "./data_csv/"
num = [str(i) for i in range(2549, 2559)]
names_data = ['all_avg', 'all_home', 'all_sgs', 'all_mgs', 'all_lgs']
data = {name:{key:[] for key in num} for name in names_data}

def data_for_prot(filename):  
    with open(mydir+filename) as fp:
        reader = csv.DictReader(fp)
        for i in names_data:
            read = next(reader)
            for year in data[i]:
                if year in reader.fieldnames and read[year] != 'None':
                    data[i][year].append(int(read[year]))

def prot_chart_avg():
    chart = pygal.StackedLine(fill=True, interpolate='cubic', style=dark_rotate_style, show_legend=False)
    chart.value_formatter = lambda x: "%gM" %(x/(10**6))
    chart.x_labels = num
    chart.add(None, [int(data['all_avg'][i]) for i in num], \
        allow_interruptions=True,  formatter=lambda y: "{:,.0f}".format(y))
    chart.render_to_file('allavg_chart.svg')
    print("Chart Success!", end='')

def prot_sub_chart():
    chart = pygal.Bar(legend_at_bottom=True)
    chart.value_formatter = lambda x: "%gM" %(x/(10**6))
    chart.x_labels = num
    for n in range(4):
        chart.add(name_y[n], [int(data[names_data[n+1]][i]) for i in num], \
            allow_interruptions=True,  formatter=lambda y: "{:,.0f}".format(y))
    chart.render_to_file('sub_avg_chart.svg')
    print("Chart Success2!", end='')



if not os.path.exists(out_path):
    os.makedirs(out_path)
# Loop for run list filenames in dir
for file in os.listdir(mydir):
    if file.endswith(".csv"):
        print("Opening.. "+file)
        data_for_prot(file)
# calculate for average
data = {key:{i:sum(data[key][i])//len(data[key][i]) for i in data[key]} for key in names_data}
# prot chart
prot_chart_avg()
prot_sub_chart()


