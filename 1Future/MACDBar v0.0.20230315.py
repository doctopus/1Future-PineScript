//@version=5
indicator("1Future: MACDBar", overlay=true)
fastLength = input(12)
slowlength = input(26)
signalLength = input(9)

MACD = ta.ema(close, fastLength) - ta.ema(close, slowlength)
aMACD = ta.ema(MACD, signalLength)
delta = MACD - aMACD
if (ta.crossover(delta, 0))
	strategy.entry("MacdLE", strategy.long, comment="MacdLE")
if (ta.crossunder(delta, 0))
	strategy.entry("MacdSE", strategy.short, comment="MacdSE")
//plot(strategy.equity, title="equity", color=color.red, linewidth=2, style=plot.style_areabr)



//A MACD Indicator for inspiration
study(title="CM_MacD_Ult_MTF", shorttitle="CM_Ult_MacD_MTF")
source = close
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input(title="Use Different Timeframe? Uncheck Box Above", type=resolution, defval="60")
smd = input(true, title="Show MacD & Signal Line? Also Turn Off Dots Below")
sd = input(true, title="Show Dots When MacD Crosses Signal Line?")
sh = input(true, title="Show Histogram?")
macd_colorChange = input(true,title="Change MacD Line Color-Signal Line Cross?")
hist_colorChange = input(true,title="MacD Histogram 4 Colors?")

res = useCurrentRes ? period : resCustom

fastLength = input(12, minval=1), slowLength=input(26,minval=1)
signalLength=input(9,minval=1)

fastMA = ema(source, fastLength)
slowMA = ema(source, slowLength)

macd = fastMA - slowMA
signal = sma(macd, signalLength)
hist = macd - signal

outMacD = security(tickerid, res, macd)
outSignal = security(tickerid, res, signal)
outHist = security(tickerid, res, hist)

histA_IsUp = outHist > outHist[1] and outHist > 0
histA_IsDown = outHist < outHist[1] and outHist > 0
histB_IsDown = outHist < outHist[1] and outHist <= 0
histB_IsUp = outHist > outHist[1] and outHist <= 0

//MacD Color Definitions
macd_IsAbove = outMacD >= outSignal
macd_IsBelow = outMacD < outSignal

plot_color = hist_colorChange ? histA_IsUp ? aqua : histA_IsDown ? blue : histB_IsDown ? red : histB_IsUp ? maroon :yellow :gray
macd_color = macd_colorChange ? macd_IsAbove ? lime : red : red
signal_color = macd_colorChange ? macd_IsAbove ? yellow : yellow : lime

circleYPosition = outSignal

plot(smd and outMacD ? outMacD : na, title="MACD", color=macd_color, linewidth=4)
plot(smd and outSignal ? outSignal : na, title="Signal Line", color=signal_color, style=line ,linewidth=2)
plot(sh and outHist ? outHist : na, title="Histogram", color=plot_color, style=histogram, linewidth=4)
plot(sd and cross(outMacD, outSignal) ? circleYPosition : na, title="Cross", style=circles, linewidth=4, color=macd_color)
hline(0, '0 Line', linestyle=solid, linewidth=2, color=white)