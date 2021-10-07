import csv
import copy

valid_education = ["Graduation", "PhD", "Master", "2n Cycle", "Basic"]
valid_marital_status = ["Single", "Together", "Divorced", "Married", "Widow"]

marketing_campaign_data = []

with open('data/marketing_campaign.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', quotechar='|')
    for row in reader:
        skip = False
        cleanRow = copy.deepcopy(row)
        
        if row['Education'] not in valid_education:
            print("Education invalid in " + " ".join(row.values()))

        if row['Marital_Status'] not in valid_marital_status:
            print("Marital_Status invalid in " + " ".join(row.values()))
        if row['Marital_Status'] == "Alone":
            cleanRow['Marital_Status'] = "Single"
        if row['Marital_Status'] == "Together":
            a = 0
            # What to do?
        
        if row['Income'] == '':
            a = 0
            # What to do?

        if '' in row.values():
            print(row.values())

        if not skip:
            marketing_campaign_data.append(cleanRow)

with open('data/marketing_campaign_CLEANED.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ID'] + ['Year_Birth'] + ['Education'] + ['Marital_Status'] + ['Income'] + ['Kidhome'] + ['Teenhome'] + ['Dt_Customer'] + ['Recency'] + ['MntWines'] + ['MntFruits'] + ['MntMeatProducts'] + ['MntFishProducts'] + ['MntSweetProducts'] + ['MntGoldProds'] + ['NumDealsPurchases'] + ['NumWebPurchases'] + ['NumCatalogPurchases'] + ['NumStorePurchases'] + ['NumWebVisitsMonth'] + ['AcceptedCmp3'] + ['AcceptedCmp4'] + ['AcceptedCmp5'] + ['AcceptedCmp1'] + ['AcceptedCmp2'] + ['Complain'] + ['Z_CostContact'] + ['Z_Revenue'] + ['Response'])
    for row in marketing_campaign_data:
        # ID	Year_Birth	Education	Marital_Status	Income	Kidhome	Teenhome	Dt_Customer	Recency	MntWines	MntFruits	MntMeatProducts	MntFishProducts	MntSweetProducts	MntGoldProds	NumDealsPurchases	NumWebPurchases	NumCatalogPurchases	NumStorePurchases	NumWebVisitsMonth	AcceptedCmp3	AcceptedCmp4	AcceptedCmp5	AcceptedCmp1	AcceptedCmp2	Complain	Z_CostContact	Z_Revenue	Response
        writer.writerow([row['ID']] + [row['Year_Birth']] + [row['Education']] + [row['Marital_Status']] + [row['Income']] + [row['Kidhome']] + [row['Teenhome']] + [row['Dt_Customer']] + [row['Recency']] + [row['MntWines']] + [row['MntFruits']] + [row['MntMeatProducts']] + [row['MntFishProducts']] + [row['MntSweetProducts']] + [row['MntGoldProds']] + [row['NumDealsPurchases']] + [row['NumWebPurchases']] + [row['NumCatalogPurchases']] + [row['NumStorePurchases']] + [row['NumWebVisitsMonth']] + [row['AcceptedCmp3']] + [row['AcceptedCmp4']] + [row['AcceptedCmp5']] + [row['AcceptedCmp1']] + [row['AcceptedCmp2']] + [row['Complain']] + [row['Z_CostContact']] + [row['Z_Revenue']] + [row['Response']])