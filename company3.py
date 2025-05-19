import csv
import matplotlib.pyplot as plt
from collections import defaultdict
def start3():
    #i take the file as task_file as reader mode 
    with open("/home/dwipendu/Desktop/Project2/Data/second_task.csv",mode='r') as task_file:
        task_reader=csv.DictReader(task_file)         #take the file in dictionary
        pincodes=defaultdict(int)
        
        #get the 2015 pincodes and there count
        for row in task_reader:
            if row['CompanyRegistrationdate_date'][:4]=='2015':
                pincodes[row['Registered_Office_Address'][-12:-6:]]+=1
    with open("/home/dwipendu/Desktop/Project2/Data/ZipCode_dist.csv",mode='r') as zip_file:
        zip_reader=csv.DictReader(zip_file)         #take the file in dictionary 
        district_count=defaultdict(int)
        
        # get district and their picode counts from pincodes dictionary
        for row in zip_reader:
            district_count[row['District']]+=pincodes[row['Pin Code']]
    #send it to graph3 function
    graph3(district_count)
def graph3(district_data):
    #taking the keys list into distict names and values in count
    district_name=district_data.keys()
    count=district_data.values()
    #plotting
    plt.bar(district_name,count)
    plt.xticks(rotation=45)
    
    #here i am giving the title and label names and then show the bar graph
    plt.title("Bar graph of counts of registration by the district in 2015")
    plt.xlabel("District")
    plt.ylabel("Number of Registration")
    plt.tight_layout()
    plt.show()

start3()

# {pin:count}
# {district:number}
# {'district':cuont}
