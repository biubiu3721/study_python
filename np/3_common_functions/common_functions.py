import numpy as np

c, v = np.loadtxt("data.csv", delimiter=',', usecols=(6, 7), unpack=True)
print("median = ", np.median(c))
sorted = np.msort(c)
print("sorted = ", sorted)
N = len(c)
print("middle = ", sorted[(N - 1) // 2])
print("avg middle = ", (sorted[(N - 1) // 2] + sorted[(N // 2)]) / 2)
print("variance = ", np.var(c))
print("variance from definition = ", np.mean((c - c.mean()) ** 2))

"""
3.12 stock returns ratio.
"""
returns = np.diff(c) / c[: -1]
print("Standard deviation = ", np.std(returns))

log_returns = np.diff(np.log(c))

pos_ret_ids = np.where(returns > 0)
print("ids with positive returns: ", pos_ret_ids)
annual_volatility = np.std(log_returns) / np.mean(log_returns)
annual_volatility = annual_volatility / np.sqrt(1. / 252.)
print("annual_volability: ", annual_volatility)
print("Monthly volatility: ", annual_volatility * np.sqrt(1. / 12.))

"""
3.13,3.14 Analysis date data.
"""
import datetime


def date_str_2_num(s):
    return datetime.datetime.strptime(s.decode("ascii"), "%d-%m-%Y").date().weekday()


dates, open, high, low, close, volumn = np.loadtxt("data.csv", delimiter=",",
                                                   usecols=(1, 3, 4, 5, 6, 7),
                                                   converters={1: date_str_2_num}, unpack=True)

print("dates: ", dates)
avgs = np.zeros(5)
weighted_avgs = np.zeros(5)
for i in range(5):
    ids = np.where(dates == i)
    prices = np.take(close, ids)
    v = np.take(volumn, ids)
    avg = np.average(prices)
    weighted_avg = np.average(prices, weights=v)
    print("Day: ", i, "Prices: ", prices, "Average: ", avgs, "weighted_avgs: ", weighted_avgs)
    avgs[i] = avg
    weighted_avgs[i] = weighted_avg

top = np.max(avgs)
w_top = np.max(weighted_avgs)
print("Highest average by weekdays: ", top, "weighted: ", w_top)
print("Top day of the week: ", np.argmax(avgs), "weighted: ", np.argmax(weighted_avgs))
bottom = np.min(avgs)
w_bottom = np.min(weighted_avgs)
print("Lowest average by weekdays:", bottom, "weighted: ", w_bottom)
print("Bottom day of the week: ", np.argmin(avgs), "weighted", np.argmin(weighted_avgs))

"""
3.15, 3.16, sumup data
"""

close = close[:16]
dates = dates[:16]
first_monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is: ", first_monday)

last_friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is ", last_friday)

week_ids = np.arange(first_monday, last_friday + 1)
print("Weeks ids initial", week_ids)
week_ids = np.split(week_ids, 3)
print("Weeks ids after split: ", week_ids)


def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]
    return "APPL", monday_open, week_high, week_low, friday_close


week_summary = np.apply_along_axis(summarize, 1, week_ids, open, high, low, close)
print("week_summary: ", week_summary)
np.savetxt("week_summary.txt", week_summary, delimiter=",", fmt="%s")

"""
3.17, 1.18, ATR(Average True, Range)
"""
import numpy as np
import sys

h, l, c = np.loadtxt("data.csv", delimiter=",", usecols=(4, 5, 6), unpack=True)
N = int(10)
print("l_h", len(h), "l_l", len(l))
print("close:", c)
h = h[-N:]
l = l[-N:]
previous_close = c[-N - 1:-1]
print("previous_close, len: ", previous_close, len(previous_close))
true_range = np.maximum(h - l, h - previous_close, previous_close - l)
print("true range", true_range)

atr = np.zeros(N)
atr[0] = np.mean(true_range)

for i in range(1, N):
    atr[i] = (N - 1) * atr[i - 1] + true_range[i]
    atr[i] /= N
print("ATR: ", atr)

"""
3.19, 3.20 Simple Moving Average
"""
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

if 0:
    # floor((w + k - 1) / s)
    N = 5
    ws = np.ones(N) / N
    print("weights: ", ws)
    close = np.loadtxt("data.csv", delimiter=',', usecols=(6,), unpack=True)
    sma_all = np.convolve(ws, close)
    print("sma_all", sma_all, len(sma_all))  # len(close) = 30, len(ws) = 5, out = 30 + 5 - 1 = 34
    sma = sma_all[N - 1: -N + 1]  # weights, wave, len(sma) = len(sma_all) - 2 * (N - 1)  = 26
    print("sma", sma, len(sma))
    t = np.arange(N - 1, len(close))  # 4~30, 30 - 4 = 26
    print("t,", len(t))

    plot(t, close[N - 1:], lw=1.0)
    plot(t, sma, lw=2.0)  #
    show()

"""
3.21, 3.22 Exponential Moving Average
"""
if 0:
    x = np.arange(5)
    print("exp", np.exp(x))
    print("linespace", np.linspace(-1, 0, 5))
    N = 5
    ws = np.exp(np.linspace(-1., 0., N))
    ws /= ws.sum()
    print("weights", ws)

    close = np.loadtxt("data.csv", delimiter=",", usecols=(6,), unpack=True)
    ema = np.convolve(ws, close)[N - 1: -N + 1]
    t = np.arange(N - 1, len(close))
    plot(t, close[N - 1:], lw=1.0)
    plot(t, ema, lw=2.0)
    show()

"""
3.23, 3.24, Bollinger Band
"""

import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = 5
weights = np.ones(N) / N
print("weights", weights)
c = np.loadtxt("data.csv", delimiter=',', usecols=(6,), unpack=True)
sma = np.convolve(weights, c)[N - 1: -N + 1]

deviation = []
C = len(c)
for i in range(N - 1, C):  # [4,30)
    if i + N < C:  # spoil
        dev = c[i: i + N]
    else:
        dev = c[-N:]
    averages = np.zeros(N)
    averages.fill(sma[i - N - 1])
    dev = (dev - averages) ** 2  # deviation is not std.
    dev = np.sqrt(np.mean(dev))

    deviation.append(dev)
deviation = 2 * np.array(deviation)
print(len(deviation), len(sma))
upperBB = sma + deviation
lowerBB = sma - deviation
c_slice = c[N - 1:]

t = np.arange(N - 1, C)

# plot(t, c_slice, lw=1.0)
# plot(t, sma, lw=2.0)
# plot(t, upperBB, lw=3.0)
# plot(t, lowerBB, lw=4.0)
# show()

"""
3.25, 3.26
"""

N = 5
c = np.loadtxt("data.csv", delimiter=',', usecols=(6,), unpack=True)
print("c", c)
b = c[-N:]  # last N in c.
b = b[::-1]  # from -1 to -N.
print("b", b)
A = np.zeros((N, N), float)
print("Zeros N by N: ", A)
for i in range(N):
    start = -N - 1 - i
    end = -1 - i
    print("start, end: ", start, end)
    A[i,] = c[-N - 1 - i: -1 - i]
print("A", A)

(x, residuals, rank, s) = np.linalg.lstsq(A, b)  # line algebra, least square.
print("x:", x)  # solve vector.
print("rediduals: ", residuals)  # residual value.
print("rank: ", rank)  # rank of A
print("s:", s)  # special value of A.

print("b * x", np.dot(b, x))

"""
3.27, 3.28
Tending curve
"""

highest, lowest, close = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

pivots = (highest + lowest + close) / 3
print("Pivots", pivots)


def fit_line(t, y):
    print(t.shape)
    A = np.vstack([t, np.ones_like(t)]).T
    print(A.shape)
    return np.linalg.lstsq(A, y)[0]


t = np.arange(len(close))
sa, sb = fit_line(t, pivots - (highest - lowest))
ra, rb = fit_line(t, pivots + (highest - lowest))
support = sa * t + sb
resistance = ra * t + rb

condition = (close > support) & (close < resistance)
print("condition", condition)
between_bands = np.ravel(np.where(condition)) #ids
print("between_bands", between_bands, "len: ", len(between_bands), type(between_bands))
print("condition support", support[between_bands])
print("condition close", close[between_bands])
print("condition resistance", resistance[between_bands])
print("Number points of between bands:", between_bands)

print("Tomorrow support: ", sa * (t[-1] + 1) + sb)
print("Tomorrow resistance: ", ra * (t[-1] + 1) + rb)

a1 = close[close > support]
a2 = close[close < resistance]

print("Number of points between 2nd approach: ", len(np.intersect1d(a1, a2)))

# plot(t, close)
# plot(t, support)
# plot(t, resistance)
# show()

""""""
"""
3.30  ndarray trim and compress.
"""

print("3.30 ndarray trim and compress.")

a = np.arange(5)
print("a = ", a)
print("Clipped: ", a.clip(1, 2))

a = np.arange(4)
print(a)
print("Compressed: ", a.compress(a > 2))


"""
3.31, 3.32 Factorial.
"""
print("3.31 Factorial")

b = np.arange(1, 9)
print("b = ", b)
print("Factorial: ", b.prod())
print("Factorials: ", b.cumprod())
