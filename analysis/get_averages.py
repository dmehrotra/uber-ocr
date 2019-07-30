from flow import *
import pandas as pd
import sys
import numpy as np
# Get/Transform Data
if (len(sys.argv) > 2):

	vetted_ids = pd.read_csv(sys.argv[2])
	non_vetted = pd.read_csv(sys.argv[1])
	non_vetted = non_vetted.replace([np.inf], np.nan).dropna(subset=[company_col, rider_col], how="all")
	data = non_vetted[non_vetted['#'].isin(vetted_ids['id'])]
	data = data.replace([np.inf], np.nan).dropna(subset=[company_col, rider_col], how="all")
else:
	data = pd.read_csv(sys.argv[1])
	data = data.replace([np.inf], np.nan).dropna(subset=[company_col, rider_col], how="all")

# Get Vars
company = get_company()
opts = str(get_surge()) + "," + str(get_metro())
# Build cases

case={
	'0,0': data.loc[(data[company_col] == company) & (data[surge_col] == False) & (data[metro_col] == False)],
	'0,1': data.loc[(data[company_col] == company) & (data[surge_col]== False) & (data[metro_col]== True)],
	'0,None': data.loc[(data[company_col] == company) & (data[surge_col]== False)],
	'1,0': data.loc[(data[company_col] == company) & (data[surge_col]== True) & (data[metro_col]== False)],
	'1,1': data.loc[(data[company_col] == company) & (data[surge_col]== True) & (data[metro_col]== True)],
	'1,None': data.loc[(data[company_col] == company) & (data[surge_col]== True)],
	'None,0': data.loc[(data[company_col] == company) & (data[metro_col]== False)],
	'None,1': data.loc[(data[company_col] == company) & (data[metro_col]==True)],
	'None,None': data.loc[data[company_col] == company]
}


company_made = case.get(opts)[ul_col] 
total = case.get(opts)[rider_col]
cuts = company_made.div(total).replace(np.inf, np.nan).dropna()

print("Mean: "+str(cuts[cuts<=1].mean()))









