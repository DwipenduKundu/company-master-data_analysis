import csv
import matplotlib.pyplot as plt
from collections import defaultdict

COMPANY_REGISTRATION_DATE = 'CompanyRegistrationdate_date'


def start2(file_path):
    # i take the file as file as reader mode
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)  # take the file in dictionary
        date = defaultdict(int)

        # counting the date count from 'CompanyRegistrationdate_date'
        for row in reader:
            date[row[COMPANY_REGISTRATION_DATE][:4]] += 1

        # sorting the dictionary according to the dates
        date_main = dict(sorted(date.items(), key=lambda x: int(x[0])))
        # send to graph2 fuction
        return date_main


def graph2(date):

    # taking the list of year from the date dictionary
    date_year = date.keys()

    # taking the list of counts
    date_count = date.values()

    # plotting
    plt.bar(date_year, date_count)
    # set the size of x axis labels and rotate it to 90 deg for bettter view
    plt.xticks(rotation=90, fontsize=7)

    # taking titlle and label names then show
    plt.title("bar graph of company registration by year")
    plt.xlabel("company registration year")
    plt.ylabel("Number of company registered")
    plt.tight_layout()
    plt.show()


def execute2():
    file_path = "/home/dwipendu/Desktop/Project2/Data/second_task.csv"
    date_dict = start2(file_path)
    graph2(date_dict)


if __name__ == "__main__":
    execute2()
