# import necessary dependecies to the library
import csv
import os

# declare the path to retrieve the file using python
file_csv = os.path.join("/Users/russ/Desktop/python_challenge/PyBank/Resources/budget_data.csv")

# open and read the file 
with open(file_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # skip the header
    header = next(csvreader)
    
    #create empty lists to add the csv values to 
    month_count = []
    revenue = []
    change_in_revenue = []
    
    #iterate through the values and add them to the empty list 
    for row in csvreader:
        # adds a list to the end of the rows using list.append() method
        month_count.append(row[0])
        revenue .append(int(row[1]))
        
        # get the change in revenue 
    for i in range(len(revenue )-1):
        change_in_revenue.append(revenue [i+1] - revenue [i])

# find the max and min from the list made using python built in functions
greatest_increase = max(change_in_revenue)
greatest_decrease = min(change_in_revenue)

# using the index to return the highest or lowest changes in revenue
# sourced from class tutorials and https://www.programiz.com/python-programming/methods/list/index
month_increase = change_in_revenue.index(max(change_in_revenue))+1
month_decrease = change_in_revenue.index(min(change_in_revenue))+1

# find month associated with the highest revenue change
a = month_count[month_increase]
b = month_count[month_decrease]

c = int(greatest_increase)
d = int(greatest_decrease)
# counts total months in the list created before using len() function
k = len(month_count) 
# finds average of the change in revenue and rounds off to two decimal places
l = round(sum(change_in_revenue)/len(change_in_revenue),2)
n = sum(revenue)


# prints
print("Financial Analysis")
print("----------------------------------------------")
print(f"Total Months:{k}")
print(f"Total: ${n}")
print(f"Average Change: {l}")
print(f"Greatest Increase in Profits: {a} (${c})")
print(f"Greatest Decrease in Profits: {b} (${d})")

# declare the output file location 
# in this case i used absolute path
# not sure if this will open in TA computer since its relative to my computer root directory
output = os.path.join("/Users/russ/Desktop/python_challenge/PyBank/Analysis/analysis.txt")
with open(output,"w") as analysis:

    # user writer to print to the desired txt file
    writer = csv.writer(analysis)
    analysis.write("Financial Analysis")
    # used "\n" to skip a line in the txt file
    # sourced the code from grepper https://www.codegrepper.com/search.php?answer_removed=1&q=how%20to%20print%20in%20python%20and%20skip%20a%20line
    analysis.write("\n")
    analysis.write("----------------------------------------")
    analysis.write("\n")
    analysis.write(f"Total Months:{k}")
    analysis.write("\n")
    analysis.write(f"Total: ${n}")
    analysis.write("\n")
    analysis.write(f"Average Change: {l}")
    analysis.write("\n")
    analysis.write(f"Greatest Increase in Profits: {a} (${c})")
    analysis.write("\n")
    analysis.write(f"Greatest Decrease in Profits: {b} (${d})")