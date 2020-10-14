# 3.4

# 3.4.1 야후 파이낸스로 주식 시세 구하기

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


sec = pdr.get_data_yahoo('005930.KS', start = '2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start = '2018-05-04')

sec.head(10)

tmp_msft = msft.drop(columns = 'Volume')
tmp_msft.tail()

sec.index
sec.columns

import matplotlib.pyplot as plt

plt.plot(sec.index, sec.Close, 'b', label = 'Samsung Electronics')
plt.plot(msft.index, msft.Close, 'r--', label = 'Microsoft')
plt.legend(loc = 'best')
plt.show()



# 이중축 그래프

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.set_xlabel('DATE')
ax1.set_ylabel('Samsung Electronics')
ax1.plot(sec.index, sec.Close, 'b', label = 'Samsung Electronics')
ax1.legend(loc='upper right')

ax2 = ax1.twinx()
ax2.set_ylabel('Microsoft')
ax2.plot(msft.index, msft.Close, 'r--', label = 'Microsoft')
ax2.legend(loc='lower right')

plt.show()


# 범례 합치기

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.set_xlabel('DATE')
ax1.set_ylabel('Samsung Electronics')
line1 = ax1.plot(sec.index, sec.Close, 'b', label = 'Samsung Electronics')

ax2 = ax1.twinx()
ax2.set_ylabel('Microsoft')
line2 = ax2.plot(msft.index, msft.Close, 'r--', label = 'Microsoft')

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower right')
plt.show()

# 3.4.2 일간 변동률로 주가 비교하기

type(sec['Close'])

sec['Close']
sec['Close'].shift(1)

sec_dpc = (sec['Close']/sec['Close'].shift(1) - 1) * 100
sec_dpc.head()

sec_dpc.iloc[0] = 0
sec_dpc.head()


# 3.4.3 주간 일간 변동률 히스토그램

import matplotlib.pyplot as plt
sec_dpc = (sec['Close'] - sec['Close'].shift(1))/sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
plt.hist(sec_dpc, bins = 18)
plt.grid(True)
plt.show()

sec_dpc.describe()


# 3.4.4 일간 변동률 누적합 구하기

sec_dpc_cs = sec_dpc.cumsum()
sec_dpc_cs

msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()

plt.plot(sec.index, sec_dpc_cs, 'b', label = 'Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--', label = 'Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc = 'best')
plt.show()
