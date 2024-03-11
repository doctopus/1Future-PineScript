//@version=5
indicator("OneFuture: Conviction Table", overlay=true)

// Conviction EMA settings
fast_conviction_ema = input.int(13, 'Fast Conviction EMA Length')
slow_conviction_ema = input.int(48, 'Slow Conviction EMA Length')

// Function to calculate market condition for a given timeframe
marketCondition(timeframe) =>
    price = request.security(syminfo.tickerid, timeframe, close, lookahead=barmerge.lookahead_on)
    fastEma = ta.ema(price, fast_conviction_ema)
    slowEma = ta.ema(price, slow_conviction_ema)
    condition = fastEma > slowEma ? "Bullish" : "Bearish"
    color = fastEma > slowEma ? color.green : color.red
    [condition, color]

// Manually process each timeframe
[condition1m, color1m] = marketCondition("1")
[condition3m, color3m] = marketCondition("3")
[condition10m, color10m] = marketCondition("10")
[condition30m, color30m] = marketCondition("30")
[condition60m, color60m] = marketCondition("60")

// Initialize table
var table maTable = table.new(position.top_right, 6, 2, border_width = 1)
table.cell(maTable, 0, 0, "Timeframe", bgcolor=color.gray)
table.cell(maTable, 0, 1, "Condition", bgcolor=color.gray)

// Populate table manually for each timeframe
table.cell(maTable, 1, 0, "1m", bgcolor=color.new(color.gray, 90))
table.cell(maTable, 1, 1, condition1m, bgcolor=color1m)

table.cell(maTable, 2, 0, "3m", bgcolor=color.new(color.gray, 90))
table.cell(maTable, 2, 1, condition3m, bgcolor=color3m)

table.cell(maTable, 3, 0, "10m", bgcolor=color.new(color.gray, 90))
table.cell(maTable, 3, 1, condition10m, bgcolor=color10m)

table.cell(maTable, 4, 0, "30m", bgcolor=color.new(color.gray, 90))
table.cell(maTable, 4, 1, condition30m, bgcolor=color30m)

table.cell(maTable, 5, 0, "60m", bgcolor=color.new(color.gray, 90))
table.cell(maTable, 5, 1, condition60m, bgcolor=color60m)
