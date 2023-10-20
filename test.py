import pandas as pd
import numpy as np

# learn about the pandas data frame

# 1. Read the sample.xls in the pandas dataframe
# 2. Read the desired column in panda df as mentioned above/(non-coloured columns)
# 3. convert the cols_to_float --> Float datatype, cols_to_string--> String datatype, cols_to_date --> date datatype 
# 4. updated df should be write in the csv format

cols_to_consider = ['Timeperiod', 'Reporting_Year', 'Contribution_Type', 'Contribution_Subtype', 'Tactic', 'SubTactic',
 'Brand',
 'Sub-Brand', 'Campaign_Name', 'Campaign_Start_Date', 'Campaign_End_Date', 'Quarter', 'Unit_Size',
 '_06s',
 '_15s', '_30s', '_60s', 'Reair', 'Tactical_Media_Target', 'Broad_Target', 'Driver', 'Insignificant',
 'LBS',
 'Direct LBS', 'Halo LBS', 'Impressions', 'Profit_Per_LBS', 'GSV_Per_LBS', 'Production_Costs',
 'Media_Costs',
 'Total_Spend', 'Margin_Dollars', 'GSV_Dollars', 'Trade_Subsidization_Rate', 'FSI_Face_Value',
 'FSI_Shared_vs_Solo', 'FSI_Unit_requirement', 'Equity or Innovation', 'Category', 'Shopper Retailer',
 'Shopper Event', 'Tent Pole Event', 'Channel', 'SM Classification', 'Line Lookup', 'Model',
 'Tent Pole Execution', 'Shopper Execution']

df = pd.read_excel('/home/sigmoid/Nancy/',sheet_name='Master_Dataset',usecols=cols_to_consider)

cols_to_float = ['_15s', '_30s','_60s', 'Driver', 'LBS', 'Direct LBS', 'Halo LBS', 'Impressions',
 'Profit_Per_LBS', 'GSV_Per_LBS',
 'Production_Costs', 'Media_Costs', 'Total_Spend', 'Margin_Dollars', 'GSV_Dollars', 'Line Lookup']

cols_to_string = ['_06s','Timeperiod', 'Reporting_Year', 'Contribution_Type', 'Contribution_Subtype', 'Tactic', 'SubTactic',
 'Brand',
 'Sub-Brand', 'Campaign_Name', 'Quarter', 'Unit_Size', 'Reair', 'Tactical_Media_Target',
 'Broad_Target', 'Insignificant',
 'Direct LBS', 'Trade_Subsidization_Rate', 'FSI_Face_Value',
 'FSI_Shared_vs_Solo', 'FSI_Unit_requirement', 'Equity or Innovation', 'Category', 'Shopper Retailer',
 'Shopper Event', 'Tent Pole Event', 'Channel', 'SM Classification', 'Model',
 'Tent Pole Execution', 'Shopper Execution']

cols_to_date = ['Campaign_Start_Date', 'Campaign_End_Date']

df[cols_to_float] = df[cols_to_float].apply(pd.to_numeric, errors='coerce')
df[cols_to_string] = df[cols_to_string].astype(str)
df[cols_to_date] = df[cols_to_date].apply(pd.to_datetime, errors='coerce')

#----------------------------Task 2------------------------------
# Insignificant,Tent Pole Execution
# X->Y and blank-> N
# cols_to_float -> 0
# cols_to_string -> blank
# all nan values

df['Insignificant'].replace('x','y',inplace=True)
df['Insignificant'].replace('nan','N',inplace=True)

df['Tent Pole Execution'].replace('X','Y',inplace=True)
df['Tent Pole Execution'].replace('nan','N',inplace=True)

df[cols_to_float] = df[cols_to_float].replace(np.nan, 0)
df[cols_to_string] = df[cols_to_string].replace('nan', '')

df.to_csv('updated_file.csv',index=False)