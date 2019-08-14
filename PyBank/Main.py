import os
import csv

#Initializing the file locations on my machine
file_name = os.path.join("budget_data.csv")

#Create lists for the compilier to iterate through rows for given variables
total_months = []
total_profit = []
change_in_monthly_profit = []

#Opem/read CSV in default
with open (file_name,newline="",encoding="utf-8") as budget_data:
    #Store contents of csv file in variable in csv-reader
    csvreader = csv.reader(budget_data,delimiter=",")

    #Neglet Headers
    header = next(csvreader)

    #Loop through rows in csv file
    for row in csvreader: 

    #Append Variables to their assigned lists 
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    #Calculating the chnage in monthly profits
    for G in range(len(total_profit)-1):

        #Arithmetic and Append
        change_in_monthly_profit.append(total_profit[G+1]-total_profit[G])
    
#Calculating the max and the min values of monthly profit change 
max_increase_value = max(change_in_monthly_profit)
max_decrease_value = min(change_in_monthly_profit)

#We use an index to and month list to calculate and relate the max/min value for each month 
max_increase_of_month = change_in_monthly_profit.index(max(change_in_monthly_profit)) + 1
max_decrease_of_month = change_in_monthly_profit.index(min(change_in_monthly_profit)) + 1 

#Print/PRIOR TO OUTPUT
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(change_in_monthly_profit)/len(change_in_monthly_profit),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_of_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_of_month]} (${(str(max_decrease_value))})")

#Initializing the output file locations on my machine ".txt"
file_to_output = os.path.join("budget_data_out_gaith.csv")

#Utilizing the 'W' to write our outputs
with open(file_to_output, "w") as file:

    #Write and Record to budget_data2.txt
    file.write("budget_data2")
    file.write("\n")
    file.write("-----------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change_in_monthly_profit)/len(change_in_monthly_profit),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_of_month]} (${(str(max_increase_value))}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_of_month]} (${(str(max_decrease_value))}")


