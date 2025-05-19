import csv
from collections import defaultdict
import matplotlib.pyplot as plt
def start4():
    with open("/home/dwipendu/Desktop/Project2/Data/second_task.csv",mode='r') as task_file:
        reader=csv.DictReader(task_file)
        dict_data=defaultdict(lambda:defaultdict(int))
        for row in reader:
            if int(row['CompanyRegistrationdate_date'][:4])>2015:
                dict_data[int(row['CompanyRegistrationdate_date'][:4])][row['CompanyIndustrialClassification']]+=1

        dict_data=dict(sorted(dict_data.items()))             
        for item in dict_data:
            dict_data[item]=dict(sorted(dict_data[item].items(),key= lambda X:X[1])[:-6:-1])
        # all_year=sorted(dict_data.keys())
        # all_sector=sorted({count for sect in dict_data.values() for count in sect})
        #print(dict_data)
        plot_sector_trends(dict_data)

        
def plot_sector_trends(sector_data):
    years = sorted(sector_data.keys())
    x_indexes = list(range(len(years)))
    bar_width = 0.15

    all_sectors = set()
    for year_data in sector_data.values():
        all_sectors.update(year_data.keys())
    all_sectors = sorted(all_sectors)

    color_list = plt.cm.tab20.colors
    sector_colors = {sector: color_list[i % len(color_list)] for i, sector in enumerate(all_sectors)}
    sector_year_values = {sector: [] for sector in all_sectors}
    sectors_per_year = []

    for year in years:
        year_data = sector_data[year]
        top5 = sorted(year_data.items(), key=lambda x: x[1], reverse=True)
        top5_sectors = [s for s, _ in top5]
        sectors_per_year.append(top5_sectors)

        for sector in all_sectors:
            if sector in top5_sectors:
                sector_year_values[sector].append(year_data.get(sector, 0))
            else:
                sector_year_values[sector].append(None)

    
    print(sector_year_values)
    print("*"*90)
    print(sectors_per_year)
    plt.figure(figsize=(18, 8))
    for sector in all_sectors:
        values = sector_year_values[sector]
        positions = []
        actual_values = []
        for j, val in enumerate(values):
            if val is not None:
                offset = sectors_per_year[j].index(sector)
                pos = x_indexes[j] - (bar_width * 2) + (offset * bar_width)
                positions.append(pos)
                actual_values.append(val)
        if positions:
            plt.bar(positions, actual_values, width=bar_width, label=sector, color=sector_colors[sector])

    plt.xticks(x_indexes, years)
    plt.xlabel("Year")
    plt.ylabel("Number of Registrations")
    plt.title("Top 5 Business Classifications per Year (Last 10 Years)")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()
start4()







# year=['2016','2017','2018','2019']
# b=[20,10,30,40]
# g=[10,20,30,40]
# w=0.4
# bar1=[i for i in range(len(year))]
# print(bar1)
# bar2=[i+w for i in bar1] 
# plt.bar(bar1,b,w,label='consumer')
# plt.bar(bar2,g,w,label='consumer')

# bar1=[i+0.2 for i in range(len(year))]
# plt.xticks(bar1,year)
# plt.show()



# # for y in year:
