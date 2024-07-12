from sector_analysis import Sector,report
import pandas as pd
import calendar
import os
import pandas as pd  

# Read the sector data
stock_symbols = []
sector = pd.read_csv('sectors/energy.csv')
for symbol in sector['Symbol']:
    stock_symbols.append(symbol)

# Iterate over each month
for i in range(1, 13):
    month = i
    print("------------" + calendar.month_name[month] + "-------------")
    
    data = report(stock_symbols=stock_symbols, month=i)
    
    # Create a directory for each month with a numeric prefix
    dir_name = f'{i:02d}_{calendar.month_name[month]}'
    os.makedirs(f'energy data/{dir_name}', exist_ok=True)
    
    # Save the data to a CSV file
    file_path = f'energy data/{dir_name}/data.csv'
    data.to_csv(file_path, index=False)
    print('--------SUCCESSFUL--------------')



