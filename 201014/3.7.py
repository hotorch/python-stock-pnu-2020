# author : Jajoon Koo

import pandas as pd
import seaborn as sns
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from scipy import stats
​
yf.pdr_override()
​
# 참조: https://finance.yahoo.com/
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
​
df = pd.DataFrame({'KOSPI': kospi['Close'], 'DOW': dow['Close']})
​
# 결측치 채우기
df = df.fillna(method='ffill')
df = df.fillna(method='bfill')
​
# 상관계수 구하기
df.corr()
r_value = df['KOSPI'].corr(df['DOW'])
​
# 결정계수 구하기
r_squared = r_value ** 2
​
# 회귀분석
rg_model = stats.linregress(df.DOW, df.KOSPI)
rg_line = f'Y = {rg_model.slope:.2f} * X + {rg_model.intercept:.2f}'
​
plt.figure(figsize=(7, 7))
plt.plot(df.DOW, df.KOSPI, '.')
plt.plot(df.DOW, rg_model.slope * df.DOW + rg_model.intercept, 'r')
plt.legend(['DOW x KOSPI', rg_line])
plt.title(f'DOW x KOSPI (R = {rg_model.rvalue:2f})')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()
​
​
​
# 지수
kospi = pdr.get_data_yahoo('^KS11', '2001-01-04')
dow = pdr.get_data_yahoo('^DJI', '2001-01-04')
nikkei225 = pdr.get_data_yahoo('^N225', '2001-01-04')  # 니케이 225 (엔화)
​
# 대체투자
crude_oil = pdr.get_data_yahoo('CL=F', '2001-01-04')  # 원유
gold = pdr.get_data_yahoo('GC=F', '2001-01-04')  # 금
silver = pdr.get_data_yahoo('SI=F', '2001-01-04')  # 은
​
# 환율
usd_krw = pdr.get_data_yahoo('KRW=X', '2001-01-04')  # 환율(USD/KRW)
jpy_krw = pdr.get_data_yahoo('JPYKRW=X', '2001-01-04')  # 환율(JPY/KRW)
​
df = pd.DataFrame({'kospi': kospi['Close'],
                   'dow': dow['Close'],
                   'nikkei225': nikkei225['Close'],
                   'crude_oil': crude_oil['Close'],
                   'gold': gold['Close'],
                   'silver': silver['Close'],
                   'usd_krw': usd_krw['Close'],
                   'jpy_krw': jpy_krw['Close']})
​
df = df.fillna(method='ffill')
df = df.fillna(method='bfill')
​
corr = df.corr()
ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0,
                 cmap=sns.diverging_palette(20, 220, n=200), square=True)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45,
                   horizontalalignment='right')
​
# https://www.youtube.com/watch?v=QgChUxo27L0&ab_channel=%EC%8A%88%EC%B9%B4%EC%9B%94%EB%93%9C (자산배분 관련 내용, 8~16분)
