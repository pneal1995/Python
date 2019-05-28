from yahoofinancials import YahooFinancials
import pandas as pd
import random
import json
import csv
import os
import ast

yahoo_financials = YahooFinancials('AMZN')
yahoo_financials.get_historical_price_data("1997-05-01", "2019-05-24", "daily")

# # Select Tickers and stock history dates
# ticker = 'AMZN'
# freq = 'daily'
# start_date = '1997-05-01'
# end_date = '2017-05-24'


# # Function to clean data extracts
# def clean_stock_data(stock_data_list):
#     new_list = []
#     for rec in stock_data_list:
#         if 'type' not in rec.keys():
#             new_list.append(rec)
#     return new_list

# # Construct yahoo financials objects for data extraction
# amzn_financials = YahooFinancials(ticker)


# # Clean returned stock history data and remove dividend events from price history
# daily_amzn_data = clean_stock_data(amzn_financials
#                                      .get_historical_price_data(start_date, end_date, freq)[ticker]['prices'])


# # Function to construct data frame based on a stock and it's market index
# def build_data_frame(data_list2):
#     data_dict = {}
#     i = 0
#     for list_item in data_list2:
#         if 'type' not in list_item.keys():
#             data_dict.update( {list_item['formatted_date']: {'AMZN': list_item['close']}} )
#             i += 1
#     tseries = pd.to_datetime(list(data_dict.keys()))
#     df = pd.DataFrame(data=list(data_dict.values()), index=tseries,
#                       columns=['AMZN']).sort_index()
#     return df



# dataframe_file = build_data_frame(daily_amzn_data)

stock_data = str(yahoo_financials.get_historical_price_data("1997-05-01", "2019-05-24", "daily"))

stocks_data = stock_data.replace("'", '"')


# stock_data_parsed = stock_data

# stock_dat = stock_data_parsed['AMZN']

# s_d = open('/tmp/stockdata.csv', 'r+')


# csvwriter = csv.writer(s_d)
# count = 0

# for s in s_d:

#       if count == 0:

#              header = s.keys()

#              csvwriter.writerow(header)

#              count += 1

#       csvwriter.writerow(s.values())

# s_d.close()


stock = "AMZN"
filename = ""
filename = stock + "_data_" + str(random.randint(1,101)) + ".txt"
f = open(filename, "w")
f.write(stocks_data)

# os.system('python json_to_csv.py node json_in_file_path csv_out_file_path')