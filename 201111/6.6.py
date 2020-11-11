"""
## Author : Jajoon Koo
6.6. 삼중창 매매 시스템
​
  - 같은 시장이더라도 지표들이 내는 신호들이 서로 다를 수 있다.
    (ex) 시장이 상승 추세일 때, "추세 추종"형 지표는 매수 신호 / "오실레이터"는 매도 신호
​
  - 주식 시장의 중요한 딜레마: "시간의 관점에 따라 주가 차트가 오를 수도 있고 내릴 수도 있다"
    -> 삼중창은 서로 다른 시간 단위에서 신호를 비교함으로써 정확한 매매 시점을 파악하는 것이 목적
​
​
  (1) 첫 번째 창 - 시장 조류
​
      - 시장 조류(Market Tide), 즉 장기 차트를 분석
        (ex) 일봉 차트를 기준으로 매매하는 트레이더 -> 주봉 차트 분석
              5분 차트를 기준으로 매매하는 트레이더 -> 30분 차트 분석
​
      - 상승 추세라고 판단되면 (매수, 관망) 중 선택
        하락 추세라고 판단되면 (매도, 관망) 중 선택
​
      - 추세를 파악할 때는 26주 지수 이동평균을 사용
        (매매단위가 일봉인 트레이더 기준)
​
​
  (2) 두 번째 창 - 시장 파도
​
      - 첫 번째 창의 추세 방향과 역행하는 파도(Market Wave)를 파악하는 데 "오실레이터" 활용
        (ex) [주봉 추세: 상승, 일봉 추세: 하락] -> 매수
             [주봉 추세: 하락, 일봉 추세: 상승] -> 매도
​
      - 책 예제
        [26주 지수 이동평균: 상승, 스토캐스틱: 30 미만] -> 매수
        [26주 지수 이동평균: 하락, 스토캐스틱: 70 초과] -> 매도
​
​
  (3) 세 번째 창 - 진입 기술
​
      - 진입 시점을 찾아내는 기법 (차트나 지표 불필요)
​
      - Trailing Stop 기법
        매수 신호 발생 -> 전일 고점보다 한 틱 위에서 매수 주문
        매도 신호 발생 -> 전일 저점보다 한 틱 아래에서 매도 주문
"""
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from Investar import Analyzer
​
mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2017-01-01')
# df = mk.get_daily_price('삼성전자', '2019-01-01')
# df = mk.get_daily_price('LG화학', '2017-01-01')
# df = mk.get_daily_price('NAVER', '2019-01-01')
# df = mk.get_daily_price('현대자동차', '2017-01-01')
​
ema60 = df.close.ewm(span=60).mean()
ema130 = df.close.ewm(span=130).mean()
macd = ema60 - ema130
signal = macd.ewm(span=45).mean()
macd_hist = macd - signal
df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal,
               macdhist=macd_hist).dropna()
​
df['number'] = df.index.map(mdates.date2num)
ohlc = df[['number', 'open', 'high', 'low', 'close']]
​
ndays_high = df.high.rolling(window=14, min_periods=1).max()
ndays_low = df.low.rolling(window=14, min_periods=1).min()
​
fast_k = (df.close - ndays_low) / (ndays_high - ndays_low) * 100
slow_d = fast_k.rolling(window=3).mean()
df = df.assign(fast_k=fast_k, slow_d=slow_d).dropna()
​
plt.figure(figsize=(9, 9))
p1 = plt.subplot(3, 1, 1)
plt.title('Triple Screen Trading')
plt.grid(True)
candlestick_ohlc(p1, ohlc.values, width=.6, colorup='red', colordown='blue')
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
for i in range(1, len(df.close)):
    if df['ema130'].values[i-1] < df['ema130'].values[i] and \
            df['slow_d'].values[i-1] >= 20 and df['slow_d'].values[i] < 20:
        plt.plot(df.number.values[i], df.close.values[i], 'r^')
    elif df.ema130.values[i - 1] > df.ema130.values[i] and \
            df.slow_d.values[i - 1] <= 80 and df.slow_d.values[i] > 80:
        plt.plot(df.number.values[i], df.close.values[i], 'bv')
plt.legend(loc='best')
​
p2 = plt.subplot(3, 1, 2)
plt.grid(True)
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.bar(df.number, df['macdhist'], color='m', label='MACD-Hist')
plt.plot(df.number, df['macd'], color='b', label='MACD')
plt.plot(df.number, df['signal'], 'g--', label='MACD-Signal')
plt.legend(loc='best')
​
p3 = plt.subplot(3, 1, 3)
plt.grid(True)
p3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['fast_k'], color='c', label='%K')
plt.plot(df.number, df['slow_d'], color='k', label='%D')
plt.yticks([0, 20, 80, 100])
plt.legend(loc='best')
plt.show()
​
# 130일 지수 이동평균이 상승했다는 것만으로 시장이 상승추세라고 할 수 있나?
#
Collapse
