// Shows Live Profit/Loss of Futures
// Copyleft OnePro
// V1.0.20240217
// 1Future -RibbonStrategy

//@version=5
strategy("1Future -RibbonStrategy", overlay=true)

// Settings
fast_ema_length = input(8, title='Fast EMA Length')
pivot_ema_length = input(21, title='Pivot EMA Length')
slow_ema_length = input(34, title='Slow EMA Length')
fast_conv_ema_length = input(13, title='Fast Conviction EMA Length')
slow_conv_ema_length = input(48, title='Slow Conviction EMA Length')

// Calculate EMAs
fast_ema = ta.ema(close, fast_ema_length)
pivot_ema = ta.ema(close, pivot_ema_length)
slow_ema = ta.ema(close, slow_ema_length)
fast_conv_ema = ta.ema(close, fast_conv_ema_length)
slow_conv_ema = ta.ema(close, slow_conv_ema_length)

// Determine bullish and bearish conviction
bullish_conviction = fast_conv_ema >= slow_conv_ema
bearish_conviction = fast_conv_ema < slow_conv_ema

// Determine if the bullish and bearish convictions are confirmed
bullish_conviction_confirmed = bullish_conviction and not bullish_conviction[1]
bearish_conviction_confirmed = bearish_conviction and not bearish_conviction[1]

// Plot arrows
plotshape(bullish_conviction_confirmed, style=shape.triangleup, color=color.green, location=location.belowbar, size=size.small, text="")
plotshape(bearish_conviction_confirmed, style=shape.triangledown, color=color.red, location=location.abovebar, size=size.small, text="")

// Strategy
if (bullish_conviction_confirmed)
    strategy.entry("Long", strategy.long)
    alert("Bullish Conviction detected!", alert.freq_once_per_bar_close)

if (bearish_conviction_confirmed)
    strategy.entry("Short", strategy.short)
    alert("Bearish Conviction detected!", alert.freq_once_per_bar_close)
