import yfinance as yf
import lxml
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.ticker as mtick
import pandas as pd

# To Modify
# =======================================================
num_ports = 10000
start = datetime(2017,5,19)
end = datetime(2020,7,1)
labels = ['3140.HK', '3101.HK', '3141.HK', '3126.HK']

# Setting up the Data and Analytics
# ========================================================
df_list = []
for label in labels:
    data = yf.download(label, start=start, end=end)
    ticker = yf.Ticker(label)
    data = data.drop(labels=['Open', 'High', 'Low', 'Close', 'Volume'], axis=1)
    df_list.append(data)

df = pd.concat(df_list, axis=1)
df.columns = [[label+' - Adj Close' for label in labels]]

log_ret = np.log(df/df.shift(1))

(log_ret + 1).cumprod().plot()

plt.grid()
plt.show()

print('\n'+'Correlation Between Stocks - Arithmetically' )
print(df.pct_change(1).corr())





