//@version=5
indicator('OneFuture Conviction Scale', overlay=true)

// Conviction EMA settings
fast_conviction_ema = input(13, 'Fast Conviction EMA Length')
slow_conviction_ema = input(48, 'Slow Conviction EMA Length')
bullish_conviction_color = input(color.aqua, 'Bullish Conviction Arrow Color')
bearish_conviction_color = input(color.yellow, 'Bearish Conviction Arrow Color')

// EMA Calculations
fast_conviction_ema_value = ta.ema(close, fast_conviction_ema)
slow_conviction_ema_value = ta.ema(close, slow_conviction_ema)

// Conviction Logic
bullish_conviction = fast_conviction_ema_value >= slow_conviction_ema_value
bearish_conviction = fast_conviction_ema_value < slow_conviction_ema_value
bullish_conviction_confirmed = bullish_conviction[1] == false and bullish_conviction
bearish_conviction_confirmed = bearish_conviction[1] == false and bearish_conviction

// Plot Arrows
plotshape(series=bullish_conviction_confirmed, style=shape.triangleup, color=bullish_conviction_color, location=location.belowbar, size=size.small)
plotshape(series=bearish_conviction_confirmed, style=shape.triangledown, color=bearish_conviction_color, location=location.abovebar, size=size.small)
