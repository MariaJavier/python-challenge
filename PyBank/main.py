import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('budget_data.csv')

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    month_line_count = 0
    profit_losses_total = 0
    average_profitloss_change = 0
    new_profit_losses_array = []
    new_date_array = []
    for row in csvreader:
        
        # assign variables to each of the rows based on columns
        dates = (row[0])
        profit_losses = (row[1]) 
        # print(profit_losses) prints out the entire series of profit/losses per line

        # create a searchable list for date column and profit / losses column
        new_date_array.append(dates)
        new_profit_losses_array.append(profit_losses)
        
        # calculation for total number of months
        month_line_count +=1
        month_line_count = int(month_line_count)
              
        # calculation for sum of all profits / losses 
        profit_losses_total += float(profit_losses)
    
    # Do NOT add 1 to total rows as list index will range out beyond the array
    total_rows = int(month_line_count)

   # calculation for greatest increase / decrease / average w/ dates
    difference_list = []
    greatest_increase = 0
    minimum = 0
    sum_of_differences = 0
    average_change = 0
    # must subtract 1 from total rows to avoid IndexError: list index out of range
    calculation_range = int(total_rows - 1)
    for i in range (calculation_range):
        diff = int(new_profit_losses_array[i + 1]) - int(new_profit_losses_array[i])
        sum_of_differences = sum_of_differences + diff
        difference_list.append(diff)
        greatest_increase = (max(difference_list))
        minimum = (min(difference_list)) 
        if diff == greatest_increase:
            final_greatest_increase = int(greatest_increase)
            date_maximum_increase = new_date_array[i + 1]
        if diff == minimum:
            final_greatest_decrease = int(minimum)   
            date_greatest_decrease = new_date_array[i+1]
    average_change = round((sum_of_differences / month_line_count), 2)

# This prints the results to the screen
print(' ')
print('Financial Analysis')
print('--------------------------------------------')
print(f'Total number of months: ' + str(month_line_count))
print(f'Total profit loss: $' + str(profit_losses_total))
print(f'Average Profit Losses Change is: $' + str(average_change))
print(f'Greatest Increase in Profits: ' + str(date_maximum_increase) + ' ' + '$' + str(final_greatest_increase))
print(f'Greatest Decrease in Profits: ' + str(date_greatest_decrease) + ' ' + '$' + str(final_greatest_decrease))


# create results.txt file with ouput 

import sys
sys.stdout = open('results.txt', 'w')

print(' ')
print('Financial Analysis')
print('--------------------------------------------')
print(f'Total number of months: ' + str(month_line_count))
print(f'Total profit loss: $' + str(profit_losses_total))
print(f'Average Profit Losses Change is: $' + str(average_change))
print(f'Greatest Increase in Profits: ' + str(date_maximum_increase) + ' ' + '$' + str(final_greatest_increase))
print(f'Greatest Decrease in Profits: ' + str(date_greatest_decrease) + ' ' + '$' + str(final_greatest_decrease))

sys.stdout.close()