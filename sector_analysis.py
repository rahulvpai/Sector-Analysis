import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import os
warnings.filterwarnings("ignore", category=FutureWarning)




class Sector:

    def __init__(self, symbol, month):
        self.symbol = symbol
        self.month = month

    def get_data(self):
        symbol_ns = self.symbol + '.NS'
        data = yf.download(symbol_ns,progress=False)
        data.loc[:, 'Month'] = data.index.month
        data.loc[:, 'Year'] = data.index.year
        data = data[['Close', 'Month', 'Year']]
        return data

    def trade_by_month(self):
        df = self.get_data()
        month_df = df[df['Month'] == self.month]
            
        trades = []
            
        for year, group in month_df.groupby('Year'):
            start_date = group.index.min()
            end_date = group.index.max()
                
            start_close = df.loc[start_date, 'Close']
            end_close = df.loc[end_date, 'Close']
                
            trade_result = ((end_close - start_close) / start_close) * 100  # Calculate percentage based on start price
            trades.append({
                'Year': year,
                'Start Date': start_date,
                'End Date': end_date,
                'Start Close': start_close,
                'End Close': end_close,
                'Trade Result': trade_result
            })
            
        trades_df = pd.DataFrame(trades)
        return trades_df
    

    def stats(self):

        trades=self.trade_by_month()

        winning_trades=0
        losing_trades=0
        returns=0.00
        for i in range(len(trades)):
            returns+=round(trades['Trade Result'][i],2)

            if trades['Trade Result'][i]>0:
                winning_trades+=1
            else:
                losing_trades+=1

        total_trades=winning_trades+losing_trades
        accuracy=round((winning_trades/total_trades)*100,2)

        return [winning_trades,losing_trades,accuracy,round(returns/total_trades,2)]
    
    



#report

def report(stock_symbols, month):



    results = []
    for symbol in stock_symbols:
        sector_obj = Sector(symbol, month)
        stats = sector_obj.stats()
        results.append({
            'Symbol': symbol,
            'Winning Trades': stats[0],
            'Losing Trades': stats[1],
            'Accuracy': stats[2],
            'Average Returns': stats[3]
        })
    result_df=pd.DataFrame(results)
    return result_df







    

