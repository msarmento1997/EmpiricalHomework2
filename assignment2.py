# Michael Sarmento

# libraries
import pandas as pd
import matplotlib.pyplot as plt

# function to create pie chart for days of the week with percentages
def frequency_day(data_frame):
    ax1 = plt.subplot()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    total = 740
    monday = 0
    tuesday = 0
    wednesday = 0
    thursday = 0
    friday = 0
    for i in data_frame:
        if i == 2:
            monday += 1
        if i == 3:
            tuesday += 1
        if i == 4:
            wednesday += 1
        if i == 5:
            thursday += 1
        if i == 6:
            friday += 1

    frequency = [(monday/total), (tuesday/total), (wednesday/total), (thursday/total), (friday/total)]

    ax1.pie(frequency, labels=days, autopct='%1.1f%%')
    ax1.axis('equal')
    plt.title("Days of the Week of Absenteeism")
    plt.show()


# function to create a frequency table with percentages for education levels
def frequency_table(data_frame):
    total = 740
    highSchool = 0
    graduate = 0
    postGrad = 0
    mastersDoctor = 0

    for i in data_frame:
        if i == 1:
            highSchool += 1
        if i == 2:
            graduate += 1
        if i == 3:
            postGrad += 1
        if i == 4:
            mastersDoctor += 1
    print("Frequency Table for Education")
    print("HighSchool       | {:.2f}%".format((highSchool/total)*100))
    print("Graduate         | {:.2f}%".format((graduate/total)*100))
    print("Post-Grad        | {:.2f}%".format((postGrad/total)*100))
    print("Masters/Doctorate| {:.2f}%".format((mastersDoctor/total)*100))

# create dataframes
data = pd.read_excel("Absenteeism_at_work.xls")

# make lists from the dataframe
myList1 = data['Reason for absence'].tolist()
myList2 = data['Work load Average/day '].tolist()
myList3 = data["Day of the week"].tolist()
myList4 = data["Weight"].tolist()
myList5 = data["Body mass index"].tolist()
myList6 = data["Education"].tolist()

# setting up and creating histogram
plt.hist(myList1)
plt.title("Reason for Absence")
plt.xlabel("Reason")
plt.ylabel("Count per reason of absence")
plt.show()

# setting up and creating boxplot
plt.boxplot(myList2)
plt.title("Work load Average per day")
plt.xlabel("Day")
plt.ylabel("Work load")
plt.show()

# calling function
frequency_day(myList3)

# setting up and creating scatter plot
plt.scatter(myList5, myList4)
plt.xlabel("Body Mass Index")
plt.ylabel("Weight(kg)")
plt.title("Scatter plot")
plt.show()

# calling function
frequency_table(myList6)





