import csv
import matplotlib.pyplot as plt


AUTHORIZED_CAPITAL = 'AuthorizedCapital'


def start1(file_path):
    # i take the file as file as reader mode
    with open(file_path, mode='r') as file:
        # taking in dictionary
        reader = csv.DictReader(file)

        # taking variables for all
        lessthan_1Lakh = 0  # <= 1L
        _1lakh_to_10lakh = 0  # 1L to 10L
        _10lakh_to_1crore = 0  # 10L to 1Cr
        _1crore_to_10crore = 0  # 1Cr to 10Cr
        greater_than_10crore = 0  # > 10Cr

        # counting the counts of specidic range
        for row in reader:
            capital = float(row[AUTHORIZED_CAPITAL])
            if capital <= 100000:
                lessthan_1Lakh += 1
            elif capital <= 1000000:
                _1lakh_to_10lakh += 1
            elif capital <= 10000000:
                _10lakh_to_1crore += 1
            elif capital <= 100000000:
                _1crore_to_10crore += 1
            else:
                greater_than_10crore += 1

        # take that in list and send it to graph function
        return [lessthan_1Lakh, _1lakh_to_10lakh, _10lakh_to_1crore, _1crore_to_10crore, greater_than_10crore]


def graph1(list_of_labels):

    # takung labels for x axis
    x_labels = ['lessthan_1Lakh', '1lakh_to_10lakh',
                '10lakh_to_1crore', '1crore_to_10crore', 'greater_than_10crore']
    # plotting
    plt.bar(x_labels, list_of_labels, width=1)

    # taking titlle and label names then show
    plt.title("Histogram of Authorized Capital")
    plt.xlabel("Authorized capital range")
    plt.ylabel("Number of companies")
    plt.tight_layout()
    plt.show()


def execute1():
    file_path = "/home/dwipendu/Desktop/Project2/Data/second_task.csv"
    list_labels = start1(file_path)
    graph1(list_labels)


if __name__ == "__main__":
    execute1()
