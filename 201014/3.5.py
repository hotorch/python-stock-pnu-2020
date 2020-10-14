# 3.5 최대 손실 낙폭 (MDD:Maximum Drawdown)
# MDD = (최저점 - 최고점)/최고점


# 3.5.2 서브프라임 당시의 MDD
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')
kospi

window = 252
peak = kospi['Adj Close'].rolling(window, min_periods=1).max()
drawdown = kospi['Adj Close']/peak - 1.0
max_dd = drawdown.rolling(window, min_periods = 1).min()

plt.figure(figsize=(9,7))
plt.subplot(211)
kospi['Close'].plot(label = 'KOSPI', title = 'KOSPI MDD', grid = True, legend = True)

plt.subplot(212)
drawdown.plot(c='blue', label = 'KOSPI DD', grid = True, legend = True)
max_dd.plot(c = 'red', label = 'KOSPI MDD', grid = True, legend= True)

max_dd.min()
max_dd[max_dd == max_dd.min()]