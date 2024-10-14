#!/usr/bin/env python
# coding: utf-8

# In[9]:


from io import StringIO
import yfinance as yf
import pandas as pd
from datetime import datetime
tickers = ['2222.SR', '2381.SR', '2030.SR', '2380.SR', '2382.SR', '4030.SR', '4200.SR', '1201.SR', '1202.SR', '1210.SR', '1211.SR', '1301.SR', '1304.SR', '1320.SR', '1321.SR', '1322.SR', '2001.SR', '2010.SR', '2020.SR', '2060.SR', '2090.SR', '2150.SR', '2170.SR', '2180.SR', '2200.SR', '2210.SR', '2220.SR', '2223.SR', '2240.SR', '2250.SR', '2290.SR', '2300.SR', '2310.SR', '2330.SR', '2350.SR', '2360.SR', '3002.SR', '3003.SR', '3004.SR', '3005.SR', '3007.SR', '3008.SR', '3010.SR', '3020.SR', '3030.SR', '3040.SR', '3050.SR', '3060.SR', '3080.SR', '3090.SR', '3091.SR', '3092.SR', '1212.SR', '1214.SR', '1302.SR', '1303.SR', '2040.SR', '2110.SR', '2160.SR', '2320.SR', '2370.SR', '4110.SR', '4140.SR', '4141.SR', '4142.SR', '4143.SR', '1831.SR', '1832.SR', '1833.SR', '1834.SR', '4270.SR', '6004.SR', '2190.SR', '4031.SR', '4040.SR', '4260.SR', '4261.SR', '4262.SR', '4263.SR', '1213.SR', '2130.SR', '2340.SR', '4011.SR', '4012.SR', '4180.SR', '1810.SR', '1820.SR', '1830.SR', '4170.SR', '4290.SR', '4291.SR', '4292.SR', '6002.SR', '6012.SR', '6013.SR', '6014.SR', '6015.SR', '4070.SR', '4071.SR', '4072.SR', '4210.SR', '4003.SR', '4008.SR', '4050.SR', '4051.SR', '4190.SR', '4191.SR', '4192.SR', '4240.SR', '4001.SR', '4006.SR', '4061.SR', '4160.SR', '4161.SR', '4162.SR', '4163.SR', '4164.SR', '2050.SR', '2100.SR', '2270.SR', '2280.SR', '2281.SR', '2282.SR', '2283.SR', '2284.SR', '4080.SR', '6001.SR', '6010.SR', '6020.SR', '6040.SR', '6050.SR', '6060.SR', '6070.SR', '6090.SR', '2140.SR', '2230.SR', '4002.SR', '4004.SR', '4005.SR', '4007.SR', '4009.SR', '4013.SR', '4014.SR', '4017.SR', '2070.SR', '4015.SR', '4016.SR', '1010.SR', '1020.SR', '1030.SR', '1050.SR', '1060.SR', '1080.SR', '1120.SR', '1140.SR', '1150.SR', '1180.SR', '1111.SR', '1182.SR', '1183.SR', '2120.SR', '4081.SR', '4082.SR', '4130.SR', '4280.SR', '8010.SR', '8012.SR', '8020.SR', '8030.SR', '8040.SR', '8050.SR', '8060.SR', '8070.SR', '8100.SR', '8120.SR', '8150.SR', '8160.SR', '8170.SR', '8180.SR', '8190.SR', '8200.SR', '8210.SR', '8230.SR', '8240.SR', '8250.SR', '8260.SR', '8270.SR', '8280.SR', '8300.SR', '8310.SR', '8311.SR', '8313.SR', '7200.SR', '7201.SR', '7202.SR', '7203.SR', '7204.SR', '7010.SR', '7020.SR', '7030.SR', '7040.SR', '2080.SR', '2081.SR', '2082.SR', '2083.SR', '2084.SR', '5110.SR', '4330.SR', '4331.SR', '4332.SR', '4333.SR', '4334.SR', '4335.SR', '4336.SR', '4337.SR', '4338.SR', '4339.SR', '4340.SR', '4342.SR', '4344.SR', '4345.SR', '4346.SR', '4347.SR', '4348.SR', '4349.SR', '4350.SR', '4020.SR', '4090.SR', '4100.SR', '4150.SR', '4220.SR', '4230.SR', '4250.SR', '4300.SR', '4310.SR', '4320.SR', '4321.SR', '4322.SR', '4323.SR']  
tickers = sorted(tickers)

all_balance_sheets = pd.DataFrame()

# Function to fetch the latest available balance sheet data for a given ticker
def fetch_latest_balance_sheet(ticker):
    # Fetch the data for the company
    company = yf.Ticker(ticker)
    balance_sheet = company.balance_sheet.T  # Transpose to get years as rows

    # Add a column for the ticker symbol
    balance_sheet['Ticker'] = ticker

    # Select the latest year or the second latest year if the latest is not available
    if not balance_sheet.empty:
        latest_years = balance_sheet.index[:2]  # Get the latest two years if available
        if len(latest_years) > 0:
            latest_balance_sheet = balance_sheet.loc[[latest_years[0]]]
        if len(latest_years) > 1:
            latest_balance_sheet = balance_sheet.loc[[latest_years[0]]] if not balance_sheet.loc[[latest_years[0]]].empty else balance_sheet.loc[[latest_years[1]]]
    else:
        latest_balance_sheet = pd.DataFrame()

    return latest_balance_sheet

# Loop through each ticker and fetch the balance sheet
for ticker in tickers:
    balance_sheet_df = fetch_latest_balance_sheet(ticker)
    all_balance_sheets = pd.concat([all_balance_sheets, balance_sheet_df], ignore_index=True)

# Save the combined balance sheets to a CSV file

all_cash_flows = pd.DataFrame()

# Function to fetch the latest available cash flow statement data for a given ticker
def fetch_latest_cash_flow(ticker):
    # Fetch the data for the company
    company = yf.Ticker(ticker)
    cash_flow = company.cashflow.T  # Transpose to get years as rows

    # Add a column for the ticker symbol

    # Select the latest year or the second latest year if the latest is not available
    if not cash_flow.empty:
        latest_years = cash_flow.index[:2]  # Get the latest two years if available
        if len(latest_years) > 0:
            latest_cash_flow = cash_flow.loc[[latest_years[0]]]
        if len(latest_years) > 1:
            latest_cash_flow = cash_flow.loc[[latest_years[0]]] if not cash_flow.loc[[latest_years[0]]].empty else cash_flow.loc[[latest_years[1]]]
    else:
        latest_cash_flow = pd.DataFrame()

    # Fetch the latest 'Close' price
    try:
        close_price = company.history(period="1d")['Close'].iloc[-1]
    except (IndexError, KeyError):
        close_price = None

    # Add 'Close' price to the DataFrame
    if not latest_cash_flow.empty:
        latest_cash_flow['Close'] = close_price

    return latest_cash_flow

# Loop through each ticker and fetch the cash flow statement
for ticker in tickers:
    cash_flow_df = fetch_latest_cash_flow(ticker)
    all_cash_flows = pd.concat([all_cash_flows, cash_flow_df], ignore_index=True)

# Save the combined cash flow statements to a CSV file
all_income_statements = pd.DataFrame()

# Function to fetch the latest available income statement data for a given ticker
def fetch_latest_income_statement(ticker):
    # Fetch the data for the company
    company = yf.Ticker(ticker)
    income_statement = company.financials.T  # Transpose to get years as rows

    # Add a column for the ticker symbol
    income_statement['Ticker'] = ticker

    # Select the latest year or the second latest year if the latest is not available
    if not income_statement.empty:
        latest_years = income_statement.index[:2]  # Get the latest two years if available
        if len(latest_years) > 0:
            latest_income_statement = income_statement.loc[[latest_years[0]]]
        if len(latest_years) > 1:
            latest_income_statement = income_statement.loc[[latest_years[0]]] if not income_statement.loc[[latest_years[0]]].empty else income_statement.loc[[latest_years[1]]]
    else:
        latest_income_statement = pd.DataFrame()

    return latest_income_statement

# Loop through each ticker and fetch the income statement
for ticker in tickers:
    income_statement_df = fetch_latest_income_statement(ticker)
    all_income_statements = pd.concat([all_income_statements, income_statement_df], ignore_index=True)

# Save the combined income statements to a CSV file
data=pd.concat([all_balance_sheets,all_income_statements,all_cash_flows],axis=1)
data=data.fillna(0)
data['NET_profit']=data['Total Revenue'] - data['Total Expenses']
data['EPS']=data['Basic EPS']
data['Free Shares'] =data['Ordinary Shares Number']-data['Treasury Shares Number']
data['Profit Margin Ratio']=data['Net Income']/data['Total Revenue']
data['Free Cash Flow Margin']=data['Free Cash Flow']/data['Total Revenue']
data['Return on Assets']= data['Net Income']/data['Total Assets']
data['Cash Ratio']= data['Cash And Cash Equivalents']/data['Current Liabilities']
data['Dept Ratio']= data['Total Debt']/data['Total Assets']
data['Operating Cash Flow Sales Ratio']=data['Operating Cash Flow']/data['Total Revenue']
data['SGA to Revenue']=data['Selling General And Administration']/data['Total Revenue']
data['R&D to Revenue']=data['Research And Development']/data['Total Revenue']
data['(P/E) Ratio']= data['Close']/data['Basic EPS']
data['Capex to Revenue']=(data['Capital Expenditure']/data['Total Revenue'])*-1
data['Current Ratio']=data['Current Assets']/data['Current Liabilities']
tickers = ['2222.SR', '2381.SR', '2030.SR', '2380.SR', '2382.SR', '4030.SR', '4200.SR', '1201.SR', '1202.SR', '1210.SR', '1211.SR', '1301.SR', '1304.SR', '1320.SR', '1321.SR', '1322.SR', '2001.SR', '2010.SR', '2020.SR', '2060.SR', '2090.SR', '2150.SR', '2170.SR', '2180.SR', '2200.SR', '2210.SR', '2220.SR', '2223.SR', '2240.SR', '2250.SR', '2290.SR', '2300.SR', '2310.SR', '2330.SR', '2350.SR', '2360.SR', '3002.SR', '3003.SR', '3004.SR', '3005.SR', '3007.SR', '3008.SR', '3010.SR', '3020.SR', '3030.SR', '3040.SR', '3050.SR', '3060.SR', '3080.SR', '3090.SR', '3091.SR', '3092.SR', '1212.SR', '1214.SR', '1302.SR', '1303.SR', '2040.SR', '2110.SR', '2160.SR', '2320.SR', '2370.SR', '4110.SR', '4140.SR', '4141.SR', '4142.SR', '4143.SR', '1831.SR', '1832.SR', '1833.SR', '1834.SR', '4270.SR', '6004.SR', '2190.SR', '4031.SR', '4040.SR', '4260.SR', '4261.SR', '4262.SR', '4263.SR', '1213.SR', '2130.SR', '2340.SR', '4011.SR', '4012.SR', '4180.SR', '1810.SR', '1820.SR', '1830.SR', '4170.SR', '4290.SR', '4291.SR', '4292.SR', '6002.SR', '6012.SR', '6013.SR', '6014.SR', '6015.SR', '4070.SR', '4071.SR', '4072.SR', '4210.SR', '4003.SR', '4008.SR', '4050.SR', '4051.SR', '4190.SR', '4191.SR', '4192.SR', '4240.SR', '4001.SR', '4006.SR', '4061.SR', '4160.SR', '4161.SR', '4162.SR', '4163.SR', '4164.SR', '2050.SR', '2100.SR', '2270.SR', '2280.SR', '2281.SR', '2282.SR', '2283.SR', '2284.SR', '4080.SR', '6001.SR', '6010.SR', '6020.SR', '6040.SR', '6050.SR', '6060.SR', '6070.SR', '6090.SR', '2140.SR', '2230.SR', '4002.SR', '4004.SR', '4005.SR', '4007.SR', '4009.SR', '4013.SR', '4014.SR', '4017.SR', '2070.SR', '4015.SR', '4016.SR', '1010.SR', '1020.SR', '1030.SR', '1050.SR', '1060.SR', '1080.SR', '1120.SR', '1140.SR', '1150.SR', '1180.SR', '1111.SR', '1182.SR', '1183.SR', '2120.SR', '4081.SR', '4082.SR', '4130.SR', '4280.SR', '8010.SR', '8012.SR', '8020.SR', '8030.SR', '8040.SR', '8050.SR', '8060.SR', '8070.SR', '8100.SR', '8120.SR', '8150.SR', '8160.SR', '8170.SR', '8180.SR', '8190.SR', '8200.SR', '8210.SR', '8230.SR', '8240.SR', '8250.SR', '8260.SR', '8270.SR', '8280.SR', '8300.SR', '8310.SR', '8311.SR', '8313.SR', '7200.SR', '7201.SR', '7202.SR', '7203.SR', '7204.SR', '7010.SR', '7020.SR', '7030.SR', '7040.SR', '2080.SR', '2081.SR', '2082.SR', '2083.SR', '2084.SR', '5110.SR', '4330.SR', '4331.SR', '4332.SR', '4333.SR', '4334.SR', '4335.SR', '4336.SR', '4337.SR', '4338.SR', '4339.SR', '4340.SR', '4342.SR', '4344.SR', '4345.SR', '4346.SR', '4347.SR', '4348.SR', '4349.SR', '4350.SR', '4020.SR', '4090.SR', '4100.SR', '4150.SR', '4220.SR', '4230.SR', '4250.SR', '4300.SR', '4310.SR', '4320.SR', '4321.SR', '4322.SR', '4323.SR']  

# Define companies for each sector
sector_companies = {
    'Energy': ['2222.SR', '2381.SR', '2030.SR', '2380.SR', '2382.SR', '4030.SR', '4200.SR'],  # Add more tickers for Energy sector
    'Insurance': ['8010.SR', '8012.SR', '8020.SR', '8030.SR', '8040.SR', '8050.SR', '8060.SR', '8070.SR', '8100.SR', '8120.SR', '8150.SR', '8160.SR', '8170.SR', '8180.SR', '8190.SR', '8200.SR', '8210.SR', '8230.SR', '8240.SR', '8250.SR', '8260.SR', '8270.SR', '8280.SR', '8300.SR', '8310.SR', '8311.SR', '8313.SR'],      # Add more tickers for Insurance sector
    'Telecom_Performance':['7010.SR', '7020.SR', '7030.SR', '7040.SR'],
    'Healthcare_Performance':['2140.SR', '2230.SR', '4002.SR', '4004.SR', '4005.SR', '4007.SR', '4009.SR', '4013.SR', '4014.SR', '4017.SR'],
    'Transport_Performance':['2190.SR', '4031.SR', '4040.SR', '4260.SR', '4261.SR', '4262.SR', '4263.SR'],
    'RealEstate_Performance':['4020.SR', '4090.SR', '4100.SR', '4150.SR', '4220.SR', '4230.SR', '4250.SR', '4300.SR', '4310.SR', '4320.SR', '4321.SR', '4322.SR', '4323.SR'],
    'Media_Performance':['4070.SR', '4071.SR', '4072.SR', '4210.SR'],
    'BusinessServices_Performance':['1831.SR', '1832.SR', '1833.SR', '1834.SR', '4270.SR', '6004.SR'],
    'DurableGoods_Performance':['1213.SR', '2130.SR', '2340.SR', '4011.SR', '4012.SR', '4180.SR'],
    'Bank_Performance':['1010.SR', '1020.SR', '1030.SR', '1050.SR', '1060.SR', '1080.SR', '1120.SR', '1140.SR', '1150.SR', '1180.SR'],
    'Industry_Performance':['1201.SR', '1202.SR', '1210.SR', '1211.SR', '1301.SR', '1304.SR', '1320.SR', '1321.SR', '1322.SR', '2001.SR', '2010.SR', '2020.SR', '2060.SR', '2090.SR', '2150.SR', '2170.SR', '2180.SR', '2200.SR', '2210.SR', '2220.SR', '2223.SR', '2240.SR', '2250.SR', '2290.SR', '2300.SR', '2310.SR', '2330.SR', '2350.SR', '2360.SR', '3002.SR', '3003.SR', '3004.SR', '3005.SR', '3007.SR', '3008.SR', '3010.SR', '3020.SR', '3030.SR', '3040.SR', '3050.SR', '3060.SR', '3080.SR', '3090.SR', '3091.SR', '3092.SR'],
    'Luxury_Goods_Retail_Performance':['4003.SR', '4008.SR', '4050.SR', '4051.SR', '4190.SR', '4191.SR', '4192.SR', '4240.SR'],
    'Consumer_Goods_Retail_Performance':['4001.SR', '4006.SR', '4061.SR', '4160.SR', '4161.SR', '4162.SR', '4163.SR', '4164.SR'],
    'Food_Production_Performance':['2050.SR', '2100.SR', '2270.SR', '2280.SR', '2281.SR', '2282.SR', '2283.SR', '2284.SR', '4080.SR', '6001.SR', '6010.SR', '6020.SR', '6040.SR', '6050.SR', '6060.SR', '6070.SR', '6090.SR'],
    'Pharmaceuticals_Performance':['2070.SR', '4015.SR', '4016.SR'],
    'Financial_Services_Performance':['1111.SR', '1182.SR', '1183.SR', '2120.SR', '4081.SR', '4082.SR', '4130.SR', '4280.SR'],
    'Tech_Services_Performance':['7200.SR', '7201.SR', '7202.SR', '7203.SR', '7204.SR'],
    'Utilities_Performance':['2080.SR', '2081.SR', '2082.SR', '2083.SR', '2084.SR', '5110.SR'],
    'REITs_Performance':['4330.SR', '4331.SR', '4332.SR', '4333.SR', '4334.SR', '4335.SR', '4336.SR', '4337.SR', '4338.SR', '4339.SR', '4340.SR', '4342.SR', '4344.SR', '4345.SR', '4346.SR', '4347.SR', '4348.SR', '4349.SR', '4350.SR'],
    'Capital_Goods_Performance': ['1212.SR', '1214.SR', '1302.SR', '1303.SR', '2040.SR', '2110.SR', '2160.SR', '2320.SR', '2370.SR', '4110.SR', '4140.SR', '4141.SR', '4142.SR', '4143.SR']
    # Add more sectors and their respective tickers
}

# Create a DataFrame to store the results
results = pd.DataFrame()

# Function to classify companies
def classify_company(data, sector_conditions):
    # Apply sector-specific conditions and calculate how many conditions each company meets
    data['Conditions Met'] = data.apply(lambda row: sum(sector_conditions(row)), axis=1)
    total_conditions = len(sector_conditions(data.iloc[0]))


    # Classify the company based on the number of conditions met
    def classify(row):
        if row == total_conditions:
            return 'Leader Company'
        elif row == total_conditions - 1:
            return 'Advanced Company'
        elif row >= total_conditions - 2:
            return 'Stable Company'
        elif row>= total_conditions - 3:
            return 'Stable Company'
        elif row>=total_conditions - 4:
            return 'Growing Company'
        elif row >= total_conditions - 5:
            return 'Growing Company'
        else:
            return 'Risky Company'

    data['Company Classification'] = data['Conditions Met'].apply(classify)
    return data

# Conditions for various sectors
conditions = {
    'Energy': lambda row: [
        row['EPS'] > 1.5,
        row['Profit Margin Ratio'] > 0.2,
        row['Current Ratio'] > 1.4,
        row['Return on Assets'] > 0.05,
        row['(P/E) Ratio'] < 18,
        row['Dept Ratio'] < 0.6
    ],
    'Insurance': lambda row: [
        row['EPS'] > 0.7,
        row['Profit Margin Ratio'] > 0.08,
        row['Current Ratio'] > 1.6,
        row['Return on Assets'] > 0.03,
        row['(P/E) Ratio'] < 16,
        row['Dept Ratio'] < 0.45
    ],
    # Add conditions for other sectors here...
    'Telecom_Performance': lambda row: [
        row['EPS'] > 0.9,
        row['Profit Margin Ratio'] > 0.12,
        row['Current Ratio'] > 1.5,
        row['Return on Assets'] > 0.04,
        row['(P/E) Ratio'] < 18,
        row['Dept Ratio'] < 0.5,
        row['Capex to Revenue'] > 0.08
    ],
    'Healthcare_Performance': lambda row: [
        row['EPS'] > 0.8,
        row['Profit Margin Ratio'] > 0.1,
        row['Current Ratio'] > 1.8,
        row['Return on Assets'] > 0.03,
        row['(P/E) Ratio'] < 20,
        row['Dept Ratio'] < 0.4,
        row['R&D to Revenue'] > 0.06
    ],
    'Transport_Performance':lambda row:[
        row['EPS'] > 0.5,
        row['Profit Margin Ratio'] > 0.07,
        row['Current Ratio'] > 1.4,
        row['Return on Assets'] > 0.02,
        row['(P/E) Ratio'] < 17,
        row['Dept Ratio'] < 0.6,
        row['Capex to Revenue'] >  0.12
        
    ],
    'RealEstate_Performance':lambda row:[
        row['EPS'] > 0.6 ,  # ربحية معقولة
        row['Profit Margin Ratio'] > 0.09 , # هامش ربحية مقبول
        row['Current Ratio'] > 1.5 ,# السيولة متوسطة
        row['Return on Assets'] > 0.03 , # العائد على الأصول
        row['(P/E) Ratio'] < 18 ,# نسبة السعر إلى الأرباح معتدلة
        row['Dept Ratio'] < 0.7
    ],
    'Media_Performance':lambda row:[
        row['EPS'] > 0.4,  # ربحية معقولة
        row['Profit Margin Ratio'] > 0.08, # هامش ربحية متوسط
        row['Current Ratio'] > 1.4, # السيولة متوسطة
        row['Return on Assets'] > 0.03,  # العائد على الأصول
        row['(P/E) Ratio'] < 22,  # P/E أعلى نسبيًا
        row['Dept Ratio'] < 0.4
        
    ],
    'BusinessServices_Performance':lambda row:[
        row['EPS'] > 0.5 ,  # ربحية معتدلة
        row['Profit Margin Ratio'] > 0.1, # هامش ربحية متوسط
        row['Current Ratio'] > 1.5, # السيولة متوسطة
        row['Return on Assets'] > 0.04, # العائد على الأصول
        row['(P/E) Ratio'] < 18,  # P/E معتدل
        row['Dept Ratio'] < 0.45  # نسبة ديون  
    ],
    'DurableGoods_Performance':lambda row:[
        row['EPS'] > 0.7, # ربحية معتدلة
        row['Profit Margin Ratio'] > 0.09,  # هامش ربحية مقبول
        row['Current Ratio'] > 1.7,  # السيولة مهمة
        row['Return on Assets'] > 0.035, # العائد على الأصول معتدل
        row['(P/E) Ratio'] < 18
    ],
    'Bank_Performance':lambda row:[
        row['EPS'] > 1.0,  # البنوك تحتاج إلى ربحية عالية
        row['Profit Margin Ratio'] > 0.15, # عادةً ما يكون هامش الربحية للبنوك أعلى
        row['Current Ratio'] > 1.2,  # نسبة السيولة تكون أقل من القطاعات الأخرى
        row['Return on Assets'] > 0.02,  # العائد على الأصول مهم للبنوك
        row['(P/E) Ratio'] < 15, # P/E عادة ما يكون أقل نسبيًا للبنوك
        row['Dept Ratio'] < 0.9 # نسبة الديون تكون مرتفعة نسبيًا في البنوك

    ],
    'Industry_Performance':lambda row:[
        row['EPS'] > 0.6,
        row['Profit Margin Ratio'] > 0.08,
        row['Current Ratio'] > 1.8,
        row['Return on Assets'] > 0.04,
        row['(P/E) Ratio'] < 20,
        row['Dept Ratio'] < 0.4,
        row['Capex to Revenue'] > 0.07
    ],
    'Luxury_Goods_Retail_Performance':lambda row:[
        row['EPS'] > 1.0,  # ربحية جيدة
        row['Profit Margin Ratio'] > 0.15 ,  # هامش ربحية مرتفع
        row['Current Ratio'] > 1.3,  # سيولة جيدة
        row['Return on Assets'] > 0.04,  # عائد جيد على الأصول
        row['(P/E) Ratio'] < 22, # نسبة السعر إلى الأرباح معتدلة
        row['Dept Ratio'] < 0.5  # نسبة ديون مت
    ],
    'Consumer_Goods_Retail_Performance':lambda row:[
        row['EPS'] > 0.5, # ربحية معقولة
        row['Profit Margin Ratio'] > 0.08,  # هامش ربحية مقبول
        row['Current Ratio'] > 1.4,  # سيولة متوسطة
        row['Return on Assets'] > 0.02,  # عائد على الأصول معقول
        row['(P/E) Ratio'] < 18 ,# نسبة السعر إلى الأرباح منخفضة
        row['Dept Ratio'] < 0.6  # 
        
    ],
    'Food_Production_Performance':lambda row:[
        row['EPS'] > 0.7,  # ربحية جيدة
        row['Profit Margin Ratio'] > 0.12,  # هامش ربحية مقبول
        row['Current Ratio'] > 1.5, # سيولة جيدة
        row['Return on Assets'] > 0.03,  # عائد على الأصول معقول
        row['(P/E) Ratio'] < 16,  # نسبة السعر إلى الأرباح منخفضة
        row['Dept Ratio'] < 0.55    
    ],
    'Pharmaceuticals_Performance':lambda row:[
        row['EPS'] > 1.5,  # ربحية مرتفعة
        row['Profit Margin Ratio'] > 0.2,  # هامش ربحية مرتفع
        row['Current Ratio'] > 2.0, # سيولة عالية
        row['Return on Assets'] > 0.05, # عائد مرتفع على الأصول
        row['(P/E) Ratio'] < 25,# نسبة السعر إلى الأرباح معتدلة
        row['Dept Ratio'] < 0.4  #  
    ],
    'Financial_Services_Performance':lambda row:[
        row['EPS'] > 1.3 ,# ربحية مرتفعة
        row['Profit Margin Ratio'] > 0.15 , # هامش ربحية جيد
        row['Current Ratio'] > 1.8 ,  # سيولة جيدة
        row['Return on Assets'] > 0.04 , # عائد على الأصول جيد
        row['(P/E) Ratio'] < 17 , # نسبة السعر إلى الأرباح متوسطة
        row['Dept Ratio'] < 0.5
    ],
    'Tech_Services_Performance':lambda row:[
        row['EPS'] > 0.9,  # ربحية جيدة
        row['Profit Margin Ratio'] > 0.12,  # هامش ربحية مقبول
        row['Current Ratio'] > 1.3,  # سيولة معقولة
        row['Return on Assets'] > 0.03, # عائد على الأصول معقول
        row['(P/E) Ratio'] < 30 , # نسبة السعر إلى الأرباح مرتفعة نسبيًا
        row['Dept Ratio'] < 0.4 
    ],
    'Utilities_Performance':lambda row:[
        row['EPS'] > 0.5,  # ربحية منخفضة
        row['Profit Margin Ratio'] > 0.08,  # هامش ربحية مقبول
        row['Current Ratio'] > 1.2, # سيولة معقولة
        row['Return on Assets'] > 0.02,# عائد على الأصول منخفض
        row['(P/E) Ratio'] < 15, # نسبة السعر إلى الأرباح معتدلة
        row['Dept Ratio'] < 0.65  
    ],
    'REITs_Performance':lambda row:[
        row['EPS'] > 0.3 ,  # ربحية منخفضة
        row['Profit Margin Ratio'] > 0.06,  # هامش ربحية منخفض
        row['Current Ratio'] > 1.0,  # سيولة مقبولة
        row['Return on Assets'] > 0.015,  # عائد منخفض على الأصول
        row['(P/E) Ratio'] < 20,  # نسبة السعر إلى الأرباح مقبولة
        row['Dept Ratio'] < 0.75
    ],
    'Capital_Goods_Performance':lambda row:[
        row['EPS'] > 0.5 ,  # ربحية منخفضة
        row['Profit Margin Ratio'] > 0.06,  # هامش ربحية منخفض
        row['Current Ratio'] > 1.1,  # سيولة مقبولة
        row['Return on Assets'] > 0.05,  # عائد منخفض على الأصول
        row['(P/E) Ratio'] < 20,  # نسبة السعر إلى الأرباح مقبولة
        row['Dept Ratio'] < 0.7

        
    ],
    
    # Continue adding other sectors as needed...
}

# Loop through each sector and its companies
for sector, tickers in sector_companies.items():
    for ticker in tickers:
        # Fetch historical data (replace with actual financial data fetching logic)
       
        
        # Classify each company based on sector conditions
        classified_data = classify_company(data, conditions[sector])

from datetime import datetime, timedelta
import pandas as pd

given_date =datetime.now().date()

previous_date = given_date - timedelta(days=60)
given_date

def combined_signals(row):
    # تحقق من التقاطع الصعودي (MACD Crosses Above Signal Line)
    if ((row['macd_cross_up']==True) and row['RSI'] <= 50 and row['Close'] > row['50_MA'] and row['Close'] > row['9_MA'] and row['Close'] > row['21_MA']  and row['Volume'] > row['Volume_MA']):
        return "Strong Buy"
    
    # تحقق من تقاطع صعودي قوي (Very Strong Buy)
    elif (row['macd_cross_up']==True and 50 < row['RSI'] < 70  and (row['9_MA'] > row['21_MA'] or row['21_MA'] > row['9_MA'] or row['50_MA']>row['9_MA'] or row['21_MA']>row['50_MA']) and row['Volume'] > row['Volume_MA'] and row['Close'] > row['50_MA'] and (row['Close'] > row['9_MA'] and row['Close'] > row['21_MA'])):
        return "Very Strong Buy"
    
    # تحقق من التقاطع الهبوطي (MACD Crosses Below Signal Line)
    elif (row['macd_cross_down']==True and row['RSI'] <= 50  and (row['Close'] < row['50_MA'] and row['Close'] < row['9_MA'] and row['Close'] < row['21_MA'])and (row['9_MA'] < row['21_MA'] or row['21_MA']< row['9_MA'] or row['50_MA']<row['9_MA'] or row['21_MA']<row['50_MA']) and row['Volume'] < row['Volume_MA']):
        return "Very Strong Sell"
    
    # تحقق من تقاطع هبوطي قوي (Strong Sell)
    elif (row['macd_cross_down']==True  and 50 < row['RSI'] < 70  and row['Volume'] < row['Volume_MA'] and row['Close'] < row['50_MA'] and row['Close'] < row['9_MA'] and row['Close'] < row['21_MA']):
        return  "Strong Sell"
    
    else:
        return  "no signal"
import pandas as pd
import yfinance as yf
import talib

# List of stock tickers
# Dictionary to store dataframes for each ticker
tickers = ['2222.SR', '2381.SR', '2030.SR','2380.SR','2382.SR','4030.SR','4200.SR','1201.SR','1202.SR','1210.SR','1211.SR','1301.SR','1304.SR','1320.SR','1321.SR','1322.SR','2001.SR','2010.SR','2020.SR','2060.SR','2090.SR','2150.SR','2170.SR','2180.SR','2200.SR','2210.SR','2220.SR','2223.SR','2240.SR','2250.SR','2290.SR','2300.SR','2310.SR','2330.SR','2350.SR','2360.SR','3002.SR','3003.SR','3004.SR','3005.SR','3007.SR','3008.SR','3010.SR','3020.SR','3030.SR','3040.SR','3050.SR','3060.SR','3080.SR','3090.SR','3091.SR','3092.SR','1212.SR','1214.SR','1302.SR','1303.SR','2040.SR','2110.SR','2160.SR','2320.SR','2370.SR','4110.SR','4140.SR','4141.SR','4142.SR','4143.SR','1831.SR','1832.SR','1833.SR','1834.SR','4270.SR','6004.SR','2190.SR','4031.SR','4040.SR','4260.SR','4261.SR','4262.SR','4263.SR','1213.SR','2130.SR','2340.SR','4011.SR','4012.SR','4180.SR','1810.SR','1820.SR','1830.SR','4170.SR','4290.SR','4291.SR','4292.SR','6002.SR','6012.SR','6013.SR','6014.SR','6015.SR','4070.SR','4071.SR','4072.SR','4210.SR','4003.SR','4008.SR','4050.SR','4051.SR','4190.SR','4191.SR','4192.SR','4240.SR','4001.SR','4006.SR','4061.SR','4160.SR','4161.SR','4162.SR','4163.SR','4164.SR','2050.SR','2100.SR','2270.SR','2280.SR','2281.SR','2282.SR','2283.SR','2284.SR','4080.SR','6001.SR','6010.SR','6020.SR','6040.SR','6050.SR','6060.SR','6070.SR','6090.SR','2140.SR','2230.SR','4002.SR','4004.SR','4005.SR','4007.SR','4009.SR','4013.SR','4014.SR','4017.SR','2070.SR','4015.SR','4016.SR','1010.SR','1020.SR','1030.SR','1050.SR','1060.SR','1080.SR','1120.SR','1140.SR','1150.SR','1180.SR','1111.SR','1182.SR','1183.SR','2120.SR','4081.SR','4082.SR','4130.SR','4280.SR','8010.SR','8012.SR','8020.SR','8030.SR','8040.SR','8050.SR','8060.SR','8070.SR','8100.SR','8120.SR','8150.SR','8160.SR','8170.SR','8180.SR','8190.SR','8200.SR','8210.SR','8230.SR','8240.SR','8250.SR','8260.SR','8270.SR','8280.SR','8300.SR','8310.SR','8311.SR','8313.SR','7200.SR','7201.SR','7202.SR','7203.SR','7204.SR','7010.SR','7020.SR','7030.SR','7040.SR','2080.SR','2081.SR','2082.SR','2083.SR','2084.SR','5110.SR','4330.SR','4331.SR','4332.SR','4333.SR','4334.SR','4335.SR','4336.SR','4337.SR','4338.SR','4339.SR','4340.SR','4342.SR','4344.SR','4345.SR','4346.SR','4347.SR','4348.SR','4349.SR','4350.SR','4020.SR','4090.SR','4100.SR','4150.SR','4220.SR','4230.SR','4250.SR','4300.SR','4310.SR','4320.SR','4321.SR','4322.SR','4323.SR']  
data_dict = {}
all_data=pd.DataFrame()
for ticker in tickers:
    dh= yf.download(ticker, start=previous_date, end=given_date)
    dh['ticker']=ticker
    dh.reset_index(inplace=True)
    dh['date_'] = pd.to_datetime(dh['Date'])
    dh['year'] = dh['date_'].dt.year
    dh['month'] = dh['date_'].dt.month
    dh['day'] = dh['date_'].dt.day
    dh=dh.drop(['Date','date_'],axis=1)
    dh['50_MA'] = talib.SMA(dh['Close'], timeperiod=50)
    dh['100_MA'] = talib.SMA(dh['Close'], timeperiod=100)
    dh['200_MA'] = talib.SMA(dh['Close'], timeperiod=200)
    dh['RSI'] = talib.RSI(dh['Close'], timeperiod=14)
    dh['9_MA'] = talib.SMA(dh['Close'], timeperiod=9)
    dh['21_MA'] = talib.SMA(dh['Close'], timeperiod=21)
    dh['MACD'], dh['MACD_Signal'], dh['MACD_Hist'] = talib.MACD(dh['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    dh['Volume_MA'] = talib.SMA(dh['Volume'], timeperiod=10)
    dh['9_MA']=dh['9_MA'].fillna(dh['9_MA'].median())
    dh['21_MA']=dh['21_MA'].fillna(dh['21_MA'].median())
    dh['MACD']=dh['MACD'].fillna(dh['MACD'].median())
    dh['MACD_Signal']=dh['MACD_Signal'].fillna(dh['MACD_Signal'].median())
    dh['MACD_Hist']=dh['MACD_Hist'].fillna(dh['MACD_Hist'].median())
    dh['Volume_MA']=dh['Volume_MA'].fillna(dh['Volume_MA'].median())
    dh['50_MA']=dh['50_MA'].fillna(dh['50_MA'].median())
    dh['100_MA']=dh['100_MA'].fillna(dh['100_MA'].median())
    dh['200_MA']=dh['200_MA'].fillna(dh['200_MA'].median())
    dh['RSI']=dh['RSI'].fillna(dh['RSI'].median())
    dh=dh.fillna(0)
    dh['macd_cross_up'] = (dh['MACD'] > dh['MACD_Signal']) & (dh['MACD'].shift(1) <= dh['MACD_Signal'].shift(1))
    dh['macd_cross_down']=(dh['MACD'] < dh['MACD_Signal']) & (dh['MACD'].shift(1) >= dh['MACD_Signal'].shift(1))
    dh['Signal'] = dh.apply(combined_signals, axis=1)
    all_data=pd.concat([all_data,dh])
dict_={'no signal':0,'Very Strong Buy':1,'Strong Buy':2,'Very Strong Sell':3,'Strong Sell':4}
all_data['Signal'] = all_data['Signal'].map(dict_)
X_new =all_data[['Open','Low','Close','50_MA','RSI','9_MA','21_MA','Signal','Volume','Volume_MA']]
import joblib
# Example: If models are saved as separate files for each ticker
models = {}
tickers = all_data['ticker'].unique()

for ticker in tickers:
    models[ticker] = joblib.load('trained_model.pkl')  # Adjust the file naming convention as needed

all_predictions = []
for ticker in tickers:
    # Filter the new data for the current ticker
    ticker_data = all_data[all_data['ticker'] == ticker]

    # Ensure to drop the ticker column and any other non-feature columns
    X_new =ticker_data[['Open','Low','Close','50_MA','RSI','9_MA','21_MA','Signal','Volume','Volume_MA']]
    # Make predictions
    if ticker in models:
        predictions = models[ticker].predict(X_new)
    else:
        predictions = None  # Handle cases where model is not found

    # Append predictions with corresponding ticker
    for pred in predictions:
        all_predictions.append({'ticker': ticker, 'prediction': pred})
predictions_df = pd.DataFrame(all_predictions)
last_predictions = predictions_df.groupby('ticker').last().reset_index()
last_days = all_data.groupby('ticker').last().reset_index()
last_predictions=last_predictions.rename(columns={
    'ticker':'الشركة',
    'prediction':'التوقع',})
prediction=last_predictions
final_data=last_days.rename(columns={
    'Close':'السعر',
    'day':'اليوم',
    'month':'الشهر',
    'year':'السنة',
    'Signal':'الاشارة',})
final=final_data[['اليوم','الشهر','السنة','السعر','الاشارة']]
df=pd.concat([final,prediction],axis=1)
df['وقت التوقع تقريبا'] = df['اليوم'].where(
    (df['الاشارة'] == 1) | 
    (df['الاشارة'] == 2) | 
    (df['الاشارة'] == 3) | 
    (df['الاشارة'] == 4)  # Close the parentheses here
)

df['وقت التوقع تقريبا'] = df['وقت التوقع تقريبا'].fillna(method='ffill')
df['مده تحقق الهدف'] = (df['اليوم'] - df['وقت التوقع تقريبا'])
df['التحقق']= df['التوقع']==df['السعر']
df['التحقق']=df['التحقق'].replace({True:'تحقق',False:'لم يتحقق'})
df=pd.concat([pd.DataFrame(classified_data['Company Classification']),df],axis=1)
df=df.rename(columns={
    'Company Classification':'الأداء المالي للشركة'})
df['الاشارة'] = df['الاشارة'].replace({
    0: 'لاتوجد اشارة',
    1:'اشارة شراء قوية جدا',
    2: 'اشارة شراء عادية',
    3: 'اشارة بيع قوية جدا',
    4: 'اشارة بيع عادية' })
df_filtered = df[df['الاشارة'] == 1]

new_order=['الشركة','الأداء المالي للشركة','السعر','التوقع','اليوم','الشهر','السنة','الاشارة','وقت التوقع تقريبا','مده تحقق الهدف','التحقق']
df=df[new_order]
df_filtered = df[(df['الاشارة'] == 'اشارة شراء قوية جدا') | (df['الاشارة'] == 'اشارة شراء عادية')| (df['الاشارة'] == 'اشارة بيع قوية جدا')| (df['الاشارة']=='اشارة بيع عادية')]

csv_output = StringIO()
df_filtered.to_csv(csv_output, index=False)
print(csv_output.getvalue())


telegram_bot_token = '7492829533:AAG_q7d1cDrLYXOuUyfp8oipsPND7lCYTd0'

# REPLACE this with your actual chat ID
chat_id = '1388399007'

# Function to send the message to the Telegram bot
def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Message sent to Telegram bot successfully')
    else:
        print(f'Failed to send message. Status code: {response.status_code}')

# Send the output to Telegram
send_to_telegram(csv_output.getvalue())