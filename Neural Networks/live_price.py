import datetime
import random
from yahoo_fin import stock_info as si


stock = "amzn"
filename = ""
filename = stock + "_stock_data" ".txt"
now = datetime.datetime.now()

print("creating new file",now,end="")
print(filename)
f = open(filename, "w")


print("streaming ", stock, " data into ", filename)
f.write(str(si.get_quote_table(stock)))