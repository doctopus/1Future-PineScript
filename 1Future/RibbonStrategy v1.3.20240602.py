// Sends Webhool Message Containing ATR Range
// Copyleft OnePro
// V1.0.20240602
// 1Future -RibbonStrategy

//@version=5

strategy("1Future -RibbonStrategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// Settings
fast_conv_ema_length = input(13, title='Fast Conviction EMA Length')
slow_conv_ema_length = input(48, title='Slow Conviction EMA Length')

use_current_close = input(false, 'Use Current Close')
timeframe = 'D'
atr_length = input(14, 'ATR Length')

// Calculate ATR
period_index = use_current_close ? 0 : 1
ticker = ticker.new(syminfo.prefix, syminfo.ticker, session=session.extended)
previous_close = request.security(ticker, timeframe, close[period_index], gaps=barmerge.gaps_off, lookahead=barmerge.lookahead_on)
atr = request.security(ticker, timeframe, ta.atr(atr_length)[period_index], gaps=barmerge.gaps_off, lookahead=barmerge.lookahead_on)
period_high = request.security(ticker, timeframe, high, gaps=barmerge.gaps_off, lookahead=barmerge.lookahead_on)
period_low = request.security(ticker, timeframe, low, gaps=barmerge.gaps_off, lookahead=barmerge.lookahead_on)
range_1 = period_high - period_low
upper_1000 = previous_close + atr
lower_1000 = previous_close - atr
//alertcondition(range_1, title='ATR Range')
plot(upper_1000, title="ATR +100", color=color.orange)
plot(period_high, title="ATR High", color=color.red)
plot(period_low, title="ATR Low", color=color.green)
plot(lower_1000, title="ATR -100", color=color.blue)

// Store the range_1 value in a variable that updates once per day
var float daily_range_1 = na
if (na(daily_range_1) or bool(ta.change(time("D"))))
    daily_range_1 := range_1

alert_message = "Range:" + str.tostring(daily_range_1)
//alert_message = str.tostring(daily_range_1)

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
    strategy.entry("Long", strategy.long, comment = alert_message)
    //alert("Bullish Conviction!", alert.freq_once_per_bar_close)
    alert(alert_message, alert.freq_once_per_bar)
    //alert("{{strategy.order.action}} {{ticker}} @{{interval}} ${{strategy.order.price}} #{{time}} *{{strategy.order.comment}} ^{{strategy.order.alert_message}}", alert.freq_once_per_bar)

if (bearish_conviction_confirmed)
    strategy.entry("Short", strategy.short, comment = alert_message)
    //alert("Bearish Conviction!", alert.freq_once_per_bar_close)
    alert(alert_message, alert.freq_once_per_bar)
    //alert("{{strategy.order.action}} {{ticker}} @{{interval}} ${{strategy.order.price}} #{{time}} *{{strategy.order.comment}} ^{{strategy.order.alert_message}}", alert.freq_once_per_bar)
