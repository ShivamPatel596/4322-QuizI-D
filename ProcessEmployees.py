'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open("employee_data.csv", "r")
reader = csv.reader(infile)
next(reader)



#create an empty dictionary
new_emp = {}

#use a loop to iterate through the csv file
for row in reader:
    #check if the employee fits the search criteria
    if row[3] == 'Marketing' and row[4] == 'CSR':
        emp_name = row[1] + ' ' + row[2]
        print('Manager Name: ', emp_name, ' Current Salary: $', format(float(row[5]), ',.2f'), sep='')
        new_sal = float(row[5]) * 1.1
        new_emp[emp_name] = new_sal


print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for k, v in new_emp.items():
    print('Manager Name: ', k, ' New Salary: $', format(v, ',.2f'), sep='')

          