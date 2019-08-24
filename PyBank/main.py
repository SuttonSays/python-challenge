#Import modules
import os
import csv

#Write a function that does:
def getthestff(csv):
    months=0
    next_month=0
    total=0
    maxrev=0
    minrev=0
    change=0
    avgchange=0
    avgchangetotal=0
    maxmonth=""
    minmonth=""
    for row in csv:
        current_month = row[0]
        next_month = row[0] + 1
        change=next_month - current_month
        avgchangetotal+=change
        avgchange=avgchangetotal / months   #Sets Average Change
        pnl=row[1]
        total+=pnl          #Total Amount
        months+=1           #Number of Months
        if pnl > maxrev:   #Greatest Profit and Month
            maxrev=pnl
            maxmonth=current_month

        if pnl < minrev:   #Greatest Loss and Month
            minrev=pnl
            minmonth=current_month

    return[months,total,maxrev,minrev,avgchange]

    print("Finacial Analysis")
    print("------------------------------")
    print("Total Months:  "months)
    print("Total:  "total)
    print("Average Change:  " avgchange)
    print("Greatest Increase in Profits:  "maxmonth "  ("maxrev")")
    print("Greatest Decrease in Profits:  "minmonth "  ("minrev")")




# Set the path from the Resources folder
budget_path = os.path.join('..', 'Resources', 'budget_data.csv')

#Set output file path

with open(budget_path) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    analysis = getthestuff(csvreader)

print(analysis)  #Print the stuff

#Save the stuff to a text file
f=open("PyBankNew.txt","w+")  
f.write(analysis)
f=close()




