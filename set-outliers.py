import csv
import copy
import numpy as np
from datetime import date

marketing_campaign_data = []

outliers_ids = [1,477,1150,1501,1665,2945,3520,4246,4303,4427,4619,4931,5376,5758,5848,5899,6237,6862,7829,8475,9931,9972,10089,10176,10311,10749,10971,11004]

# open marketing campaign csv with fixed dates to read data
with open('data/marketing_campaign_CLEANED.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        skip = False
        cleanRow = copy.deepcopy(row)

        cleanRow["Is_Outlier"] = "false"

        for id in outliers_ids:
            if id == int(row['ID']):
                cleanRow["Is_Outlier"] = "true"

        if not skip:
            marketing_campaign_data.append(cleanRow)

# Create csv file to contain cleaned data
with open('data/marketing_campaign_CLEANED_WITH_OUTLIERS.csv', 'w', newline='') as csvfile:
    # The file is emptied if it contained anything
    csvfile.truncate(0)

    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ID'] + ['Year_Birth'] + ['Education'] + ['Marital_Status'] + ['Income'] + ['Kidhome'] + ['Teenhome'] + ['Dt_Customer'] + ['Recency'] + ['MntWines'] + ['MntFruits'] + ['MntMeatProducts'] + ['MntFishProducts'] + ['MntSweetProducts'] + ['MntGoldProds'] + ['NumDealsPurchases'] +
                    ['NumWebPurchases'] + ['NumCatalogPurchases'] + ['NumStorePurchases'] + ['NumWebVisitsMonth'] + ['AcceptedCmp3'] + ['AcceptedCmp4'] + ['AcceptedCmp5'] + ['AcceptedCmp1'] + ['AcceptedCmp2'] + ['Complain'] + ['Response'] + ['Age'] + ['Days_Since_Customer'] + ['Education_Rank'] + ['Income_Z'] + ['Is_Outlier'])
    for row in marketing_campaign_data:

        writer.writerow([row['ID']] + [row['Year_Birth']] + [row['Education']] + [row['Marital_Status']] + [row['Income']] + [row['Kidhome']] + [row['Teenhome']] + [row['Dt_Customer']] + [row['Recency']] + [row['MntWines']] + [row['MntFruits']] + [row['MntMeatProducts']] + [row['MntFishProducts']] + [row['MntSweetProducts']] + [row['MntGoldProds']] + [row['NumDealsPurchases']] + [
                        row['NumWebPurchases']] + [row['NumCatalogPurchases']] + [row['NumStorePurchases']] + [row['NumWebVisitsMonth']] + [row['AcceptedCmp3']] + [row['AcceptedCmp4']] + [row['AcceptedCmp5']] + [row['AcceptedCmp1']] + [row['AcceptedCmp2']] + [row['Complain']] + [row['Response']] + [row['Age']] + [row['Days_Since_Customer']] + [row['Education_Rank']] + [row['Income_Z']] + [row['Is_Outlier']])