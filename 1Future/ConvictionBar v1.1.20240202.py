//@version=5
indicator('OneFuture: Conviction Scale', overlay=true)

// Conviction EMA settings
fast_conviction_ema = input(13, 'Fast Conviction EMA Length')
slow_conviction_ema = input(48, 'Slow Conviction EMA Length')
bullish_conviction_color = input(color.aqua, 'Bullish Conviction Arrow Color')
bearish_conviction_color = input(color.yellow, 'Bearish Conviction Arrow Color')

// EMA Calculations
fast_conviction_ema_value = ta.ema(close, fast_conviction_ema)
slow_conviction_ema_value = ta.ema(close, slow_conviction_ema)

// Conviction Logic
bullish_conviction = fast_conviction_ema_value > slow_conviction_ema_value
bearish_conviction = fast_conviction_ema_value < slow_conviction_ema_value
bullish_conviction_confirmed = bullish_conviction and not bullish_conviction[1]
bearish_conviction_confirmed = bearish_conviction and not bearish_conviction[1]

// Plot Arrows
plotshape(series=bullish_conviction_confirmed, style=shape.triangleup, color=bullish_conviction_color, location=location.belowbar, size=size.small)
plotshape(series=bearish_conviction_confirmed, style=shape.triangledown, color=bearish_conviction_color, location=location.abovebar, size=size.small)

// Label Logic
var label marketConditionLabel = na // Declare the label variable at the top
if na(marketConditionLabel)
    marketConditionLabel := label.new(x=bar_index, y=close, text="", style=label.style_label_right, size=size.normal)

// Update the label every bar
label.set_text(marketConditionLabel, bullish_conviction ? "Bullish" : "Bearish")
label.set_color(marketConditionLabel, bullish_conviction ? color.green : color.red)
label.set_y(marketConditionLabel, close)
label.set_x(marketConditionLabel, bar_index)

// Optional: Adjust label visibility or positioning if necessary
//label.set_textalign(marketConditionLabel, label.align_center)
