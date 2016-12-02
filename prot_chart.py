import pygal, csv, os
from pygal.style import RotateStyle
dark_rotate_style = RotateStyle('#E86FA0')
name_y = ['บ้านอยู่อาศัย', 'กิจการขนาดเล็ก', 'กิจการขนาดกลาง', 'กิจการขนาดใหญ่', 'อื่นๆ']
out_path = "./chart_f/"
mydir = "./data_csv/"

def data_prot(filename):  
    with open(mydir+filename) as fp:
        reader = csv.DictReader(fp)
        num = [i for i in (reader.fieldnames)]

        chart_1 = pygal.StackedLine(fill=True, interpolate='cubic', style=dark_rotate_style, show_legend=False)
        chart_1.value_formatter = lambda x: "%gM" %(x/(10**6))
        chart_1.x_labels = num
        data = next(reader)
        chart_1.add(None, [int(data[i]) if data[i] != 'None' else None for i in num], \
            allow_interruptions=True,  formatter=lambda y: "{:,.0f}".format(y))
        chart_1.render_to_file(out_path+filename[:-4]+'_chart_1.svg')
        print("Chart1 Success!", end='')

        chart_2 = pygal.Bar(legend_at_bottom=True)
        chart_2.value_formatter = lambda x: "%gM" %(x/(10**6))
        chart_2.x_labels = num
        for i in range(5):
            data = next(reader)
            chart_2.add(name_y[i], [int(data[i]) if data[i] != 'None' else None for i in num], \
                allow_interruptions=True,  formatter=lambda y: "{:,.0f}".format(y))
        chart_2.render_to_file(out_path+filename[:-4]+'_chart_2.svg')
        print("Chart2 Success!")


if not os.path.exists(out_path):
    os.makedirs(out_path)
# Loop for run list filenames in dir
for file in os.listdir(mydir):
    if file.endswith(".csv"):
        print("Opening.. "+file, end='')
        data_prot(file)
