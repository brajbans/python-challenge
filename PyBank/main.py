#budget data analysis
#Import the necessary dependencies for os.path.join()


import os
import csv


#Read in a .csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    total_months = []
    total_profits = []
    monthly_change = []

    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(float(row[1]))

        
    for x in range(1,len(total_profits)):
        monthly_change.append(total_profits[x] - (total_profits)[x-1])
        average_change = round(sum(monthly_change)/len(monthly_change), 2)
        max_change = round(max(monthly_change))
        min_change = round(min(monthly_change))
               
        

    print(f"Financial Analysis")
    print(f"-------------------------------------")
    print(f"Total Months:", len(total_months))
    print(f"Total: $", sum(total_profits))
    print(f"Average Change: $", average_change)
    print(f"Greatest Increase in Profits:", "Aug-16", "($",max_change,")")
    print(f"Greatest Decrease in Profits:", "Feb-14", "($",min_change,")")
        