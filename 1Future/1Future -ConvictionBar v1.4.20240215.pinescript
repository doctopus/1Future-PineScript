//@version=5
indicator("1F: ConvictionScale", overlay=true)

// User Inputs
fast_conviction_ema = input.int(13, 'Fast Conviction EMA Length')
slow_conviction_ema = input.int(48, 'Slow Conviction EMA Length')
tablePositionInput = input.string("Bottom left", title="Table Position", options=["Top left", "Top right", "Bottom left", "Bottom right", "Middle left", "Middle right"])

// Function to calculate market condition for a given timeframe
marketCondition(timeframe) =>
    price = request.security(syminfo.tickerid, timeframe, close, lookahead=barmerge.lookahead_off)
    fastEma = ta.ema(price, fast_conviction_ema)
    slowEma = ta.ema(price, slow_conviction_ema)
    condition = fastEma > slowEma ? "↑" : "↓"
    color = fastEma > slowEma ? color.green : color.red
    [condition, color]

// Manually process each timeframe
[condition1m, color1m] = marketCondition("1")
[condition3m, color3m] = marketCondition("3")
[condition10m, color10m] = marketCondition("10")
[condition30m, color30m] = marketCondition("30")
[condition60m, color60m] = marketCondition("60")


// Setting table position
tablePosition = position.bottom_right
if tablePositionInput == "Top left"
    tablePosition := position.top_left
else if tablePositionInput == "Top right"
    tablePosition := position.top_right
else if tablePositionInput == "Bottom left"
    tablePosition := position.bottom_left
else if tablePositionInput == "Bottom right"
    tablePosition := position.bottom_right
else if tablePositionInput == "Middle left"
    tablePosition := position.middle_left
else if tablePositionInput == "Middle right"
    tablePosition := position.middle_right

// Initialize table
var table maTable = table.new(tablePosition, 6, 2, bgcolor = color.rgb(0, 0, 0, 50), border_width = 1)
table.cell(maTable, 0, 0, "Time", bgcolor = color.rgb(0, 0, 0, 50), text_color=color.white)
table.cell(maTable, 0, 1, "Trend", bgcolor = color.rgb(0, 0, 0, 50), text_color=color.white)

// Populate table manually for each timeframe
table.cell(maTable, 1, 0, "1m", bgcolor = color.rgb(0, 0, 0, 50), text_color=color.white)
table.cell(maTable, 1, 1, condition1m, bgcolor=color1m)

table.cell(maTable, 2, 0, "3m", bgcolor = color.rgb(0, 0, 0, 50), text_color=color.white)
table.cell(maTable, 2, 1, condition3m, bgcolor=color3m)

table.cell(maTable, 3, 0, "10m", bgcolor = color.rgb(0, 0, 0, 50), text_color=color.white)
table.cell(maTable, 3, 1, condition10m, bgcolor=color10m)

table.cell(maTable, 4, 0, "30m", bgcolor = color.rgb(0, 0, 0, 50), text_color=color.white)
table.cell(maTable, 4, 1, condition30m, bgcolor=color30m)

table.cell(maTable, 5, 0, "60m", bgcolor = color.rgb(0, 0, 0, 50), text_color=color.white)
table.cell(maTable, 5, 1, condition60m, bgcolor=color60m)
