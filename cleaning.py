import csv
import copy
import numpy as np
from datetime import date

valid_education = ["Bachelors", "PhD", "Master", "High School"]
valid_marital_status = ["Single", "Together", "Divorced", "Married", "Widow"]

marketing_campaign_data = []

# open marketing campaign csv with fixed dates to read data
with open('data/marketing_campaign_DATEFIXED.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    n = 0
    sumIncome = 0
    incomeArr = []

    for row in reader:
        skip = False
        cleanRow = copy.deepcopy(row)

        if row['Education'] == "2n Cycle":
            cleanRow['Education'] = "Master"
        if row['Education'] == "Basic":
            cleanRow['Education'] = "High School"
        if row['Education'] == "Graduation":
            cleanRow['Education'] = "Bachelors"

        if row['Marital_Status'] == "Alone":
            cleanRow['Marital_Status'] = "Single"
        if row['Marital_Status'] == 'YOLO' or row['Marital_Status'] == 'Absurd':
            skip = True

        if row['Income'] == '':
            skip = True
        if row['Income'] == str(666666):
            skip = True

        if row['NumDealsPurchases'] == 0 and ['NumWebPurchases'] == 0 and ['NumCatalogPurchases'] == 0 and ['NumStorePurchases'] == 0:
            skip = True

        # Calculate age and days since customer join
        cleanRow['Age'] = 2021 - int(row['Year_Birth'])
        joinDate = row['Dt_Customer'].split('/')
        d = date(int(joinDate[2]), int(joinDate[0]), int(joinDate[1]))
        d1 = date.today()
        delta = d1 - d
        cleanRow['Days_Since_Customer'] = delta.days

        # Rank customer education numerically
        if cleanRow['Education'] == "High School":
            cleanRow['Education_Rank'] = 1
        elif cleanRow['Education'] == "Bachelors":
            cleanRow['Education_Rank'] = 2
        elif cleanRow['Education'] == "Master":
            cleanRow['Education_Rank'] = 3
        elif cleanRow['Education'] == "PhD":
            cleanRow['Education_Rank'] = 4

        del cleanRow['Z_CostContact']
        del cleanRow['Z_Revenue']

        if not skip:
            n += 1
            sumIncome += int(cleanRow['Income'])
            incomeArr.append(int(cleanRow['Income']))
            marketing_campaign_data.append(cleanRow)

# Calculate mean and standard deviation of income
meanIncome = sumIncome / n
print("mean income: " + str(meanIncome))
stdIncome = np.std(incomeArr)
print("std income: " + str(stdIncome))

# Create csv file to contain cleaned data
with open('data/marketing_campaign_CLEANED.csv', 'w', newline='') as csvfile:
    # The file is emptied if it contained anything
    csvfile.truncate(0)

    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ID'] + ['Year_Birth'] + ['Education'] + ['Marital_Status'] + ['Income'] + ['Kidhome'] + ['Teenhome'] + ['Dt_Customer'] + ['Recency'] + ['MntWines'] + ['MntFruits'] + ['MntMeatProducts'] + ['MntFishProducts'] + ['MntSweetProducts'] + ['MntGoldProds'] + ['NumDealsPurchases'] +
                    ['NumWebPurchases'] + ['NumCatalogPurchases'] + ['NumStorePurchases'] + ['NumWebVisitsMonth'] + ['AcceptedCmp3'] + ['AcceptedCmp4'] + ['AcceptedCmp5'] + ['AcceptedCmp1'] + ['AcceptedCmp2'] + ['Complain'] + ['Response'] + ['Age'] + ['Days_Since_Customer'] + ['Education_Rank'] + ['Income_Z'])
    for row in marketing_campaign_data:

        # Calculate income z-score and add the column
        row['Income_Z'] = (int(row['Income']) - meanIncome) / stdIncome

        writer.writerow([row['\ufeffID']] + [row['Year_Birth']] + [row['Education']] + [row['Marital_Status']] + [row['Income']] + [row['Kidhome']] + [row['Teenhome']] + [row['Dt_Customer']] + [row['Recency']] + [row['MntWines']] + [row['MntFruits']] + [row['MntMeatProducts']] + [row['MntFishProducts']] + [row['MntSweetProducts']] + [row['MntGoldProds']] + [row['NumDealsPurchases']] + [
                        row['NumWebPurchases']] + [row['NumCatalogPurchases']] + [row['NumStorePurchases']] + [row['NumWebVisitsMonth']] + [row['AcceptedCmp3']] + [row['AcceptedCmp4']] + [row['AcceptedCmp5']] + [row['AcceptedCmp1']] + [row['AcceptedCmp2']] + [row['Complain']] + [row['Response']] + [row['Age']] + [row['Days_Since_Customer']] + [row['Education_Rank']] + [row['Income_Z']])
