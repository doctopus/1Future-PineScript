//@version=5
indicator("EMA Ratings", overlay = true)

TRANSP = 80
TABLE_WIDTH = 6
var CELL_TOOLTIP = "Cell color depends on the EMA direction: green for rising EMAs, red for falling ones"

// Initialize EMA series for each length
ema10 = ta.ema(close, 10)
ema20 = ta.ema(close, 20)
ema50 = ta.ema(close, 50)
ema100 = ta.ema(close, 100)
ema200 = ta.ema(close, 200)
ema500 = ta.ema(close, 500)

// Store EMA values in an array
emaValues = array.new_float()
array.push(emaValues, ema10)
array.push(emaValues, ema20)
array.push(emaValues, ema50)
array.push(emaValues, ema100)
array.push(emaValues, ema200)
array.push(emaValues, ema500)

// EMA lengths for titles
emaLengths = array.from(10, 20, 50, 100, 200, 500)

// Inputs for EMA lengths
fast_conviction_ema = input(13, 'Fast Conviction EMA Length')
slow_conviction_ema = input(48, 'Slow Conviction EMA Length')

// Initialize table with 3 rows and 5 columns for the timeframes
var maTable = table.new(position.top_right, TABLE_WIDTH, 3, border_width = 2) // Adjusted number of rows from 4 to 3

// Function to calculate market condition for a given timeframe
marketCondition(string timeframe) =>
    price = request.security(syminfo.tickerid, timeframe, close, lookahead=barmerge.lookahead_on)
    fastEma = ta.ema(price, fast_conviction_ema)
    slowEma = ta.ema(price, slow_conviction_ema)
    fastEma > slowEma ? "Bullish" : "Bearish"

if barstate.islast
    headerColor = color.new(color.blue, TRANSP)
    table.cell(maTable, 0, 0, text = "OneFuture Conviction Table", bgcolor = headerColor)
    table.merge_cells(maTable, 0, 0, 5, 0)

if barstate.islast
    for i = 0 to array.size(emaLengths) - 1
        cellTitle = str.format("EMA {0}", array.get(emaLengths, i))
        cellValue = array.get(emaValues, i)
        // Comparison logic might need adjustment as mentioned earlier
        cellColor = color.new(cellValue >= nz(array.get(emaValues, math.max(i-1, 0)), cellValue) ? color.green : color.red, TRANSP)
        table.cell(maTable, i, 1, bgcolor = cellColor, text = cellTitle, text_color = color.gray, tooltip = CELL_TOOLTIP) // Adjusted row index from 2 to 1
        table.cell(maTable, i, 2, bgcolor = cellColor, text = str.tostring(cellValue, format.mintick), tooltip = CELL_TOOLTIP) // Adjusted row index from 3 to 2
