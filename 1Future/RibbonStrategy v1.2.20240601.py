// Shows Live Profit/Loss of Futures
// Copyleft OnePro
// V1.2.20240601
// 1Future -RibbonStrategy

//@version=5
//@strategy_alert_message {{strategy.order.action}} {{strategy.position_size}} {{ticker}} @ {{strategy.order.price}}
strategy("1Future -RibbonStrategy", overlay=true)

// Settings
fast_conv_ema_length = input(8, title='Fast Conviction EMA Length')
slow_conv_ema_length = input(48, title='Slow Conviction EMA Length')

// Calculate EMAs
fast_conv_ema = ta.ema(close, fast_conv_ema_length)
slow_conv_ema = ta.ema(close, slow_conv_ema_length)
//fast_conv_ema = ta.ema(close, 13)
//slow_conv_ema = ta.ema(close, 48)

// Determine bullish and bearish conviction
bullish_conviction = fast_conv_ema >= slow_conv_ema
bearish_conviction = fast_conv_ema < slow_conv_ema

// Determine if the bullish and bearish convictions are confirmed
bullish_conviction_confirmed = bullish_conviction and not bullish_conviction[1]
bearish_conviction_confirmed = bearish_conviction and not bearish_conviction[1]

// Plot arrows
plotshape(bullish_conviction_confirmed, style=shape.triangleup, color=#3afc3399, location=location.belowbar, size=size.small, text="")
plotshape(bearish_conviction_confirmed, style=shape.triangledown, color=#ff3ea599, location=location.abovebar, size=size.small, text="")

// Strategy
if (bullish_conviction_confirmed)
    strategy.entry("Long", strategy.long, comment ='')
    alert("Bullish Conviction!", alert.freq_once_per_bar_close)

if (bearish_conviction_confirmed)
    strategy.entry("Short", strategy.short, comment ='')
    alert("Bearish Conviction!", alert.freq_once_per_bar_close)
