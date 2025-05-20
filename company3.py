import csv
import matplotlib.pyplot as plt
from collections import defaultdict


COMPANY_REGISTRATION_DATE = 'CompanyRegistrationdate_date'
REGISTERED_OFFICE_ADDRESS = 'Registered_Office_Address'
DISTRICT = 'District'
PIN_CODE = 'Pin Code'


def start3(taskfile_path, zipfile_path):
    # i take the file as task_file as reader mode
    with open(taskfile_path, mode='r') as task_file:
        task_reader = csv.DictReader(task_file)  # take the file in dictionary
        pincodes = defaultdict(int)

        # get the 2015 pincodes and there count
        for row in task_reader:
            if row[COMPANY_REGISTRATION_DATE][:4] == '2015':
                pincodes[row[REGISTERED_OFFICE_ADDRESS][-12:-6:]] += 1
    with open(zipfile_path, mode='r') as zip_file:
        zip_reader = csv.DictReader(zip_file)  # take the file in dictionary
        district_count = defaultdict(int)

        # get district and their picode counts from pincodes dictionary
        for row in zip_reader:
            district_count[row[DISTRICT]] += pincodes[row[PIN_CODE]]
    # send it to graph3 function
    return district_count


def graph3(district_data):
    # taking the keys list into distict names and values in count
    district_name = district_data.keys()
    count = district_data.values()
    # plotting
    plt.bar(district_name, count)
    plt.xticks(rotation=45)

    # here i am giving the title and label names and then show the bar graph
    plt.title("Bar graph of counts of registration by the district in 2015")
    plt.xlabel("District")
    plt.ylabel("Number of Registration")
    plt.tight_layout()
    plt.show()


def execute3():
    taskfile_path = "/home/dwipendu/Desktop/Project2/Data/second_task.csv"
    zipfile_path = "/home/dwipendu/Desktop/Project2/Data/ZipCode_dist.csv"
    district_count_dict = start3(taskfile_path, zipfile_path)
    graph3(district_count_dict)


if __name__ == "__main__":
    execute3()


# {pin:count}
# {district:number}
# {'district':cuont}
