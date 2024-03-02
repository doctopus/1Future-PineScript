// Both Horizontal and Vertical
//@version=5
indicator("1F- ConvictionBar", overlay=true)

// User inputs
showTableInput = input.bool(true, title="Show Conviction Bar")
tablePositionInput = input.string("Top-Right", title="Table Position", options=["Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right", "Middle-Left", "Middle-Right"])
orientationInput = input.string(defval = 'Horizontal', title = 'Table Orientation', options = ['Horizontal', 'Vertical'])
bullishTextInput = input.string(defval = "↑😎", title = "Bullish Text", group = "Design", inline = "Text")
bearishTextInput = input.string(defval = "↓👽", title = "Bearish Text", group = "Design", inline = "Text")
bullishColorInput = input.color(color.green, title="Bullish Colour", group = "Design", inline = "Bullish Colour")
bearishColorInput = input.color(color.red, title="Bearish Colour", group = "Design", inline = "Bullish Colour")
tf30sInput = input.bool(true, title="30s", group = "Timeframes", inline = "TFL")
tf1mInput = input.bool(true, title="1m", group = "Timeframes", inline = "TFL")
tf2mInput = input.bool(true, title="2m", group = "Timeframes", inline = "TFL")
tf3mInput = input.bool(true, title="3m", group = "Timeframes", inline = "TFL")
tf5mInput = input.bool(true, title="5m", group = "Timeframes", inline = "TFL")
tf10mInput = input.bool(true, title="10m", group = "Timeframes", inline = "TFH")
tf15mInput = input.bool(true, title="15m", group = "Timeframes", inline = "TFH")
tf30mInput = input.bool(true, title="30m", group = "Timeframes", inline = "TFH")
tf1hInput = input.bool(true, title="1h", group = "Timeframes", inline = "TFH")

// Setting table position
tablePosition = position.top_right
if tablePositionInput == "Top-Left"
    tablePosition := position.top_left
else if tablePositionInput == "Top-Right"
    tablePosition := position.top_right
else if tablePositionInput == "Bottom-Left"
    tablePosition := position.bottom_left
else if tablePositionInput == "Bottom-Right"
    tablePosition := position.bottom_right
else if tablePositionInput == "Middle-Left"
    tablePosition := position.middle_left
else if tablePositionInput == "Middle-Right"
    tablePosition := position.middle_right
//}
// Initialize an array for timeframes
var string[] timeframes = array.new_string()
if (array.size(timeframes) == 0)
    array.push(timeframes, "30s")
    array.push(timeframes, "1m")
    array.push(timeframes, "2m")
    array.push(timeframes, "3m")
    array.push(timeframes, "5m")
    array.push(timeframes, "10m")
    array.push(timeframes, "15m")
    array.push(timeframes, "30m")
    array.push(timeframes, "60m")
// }
// Function to calculate Conviction based on fast and slow EMA
getConviction(src, tf) =>
    fastEma = request.security(syminfo.tickerid, tf, ta.ema(src, 13))
    slowEma = request.security(syminfo.tickerid, tf, ta.ema(src, 48))
    convictionText = fastEma > slowEma ? bullishTextInput : fastEma < slowEma ? bearishTextInput : "→🤢"
    convictionCondition = fastEma > slowEma ? "Bullish" : fastEma < slowEma ? "Bearish" : "Neutral"
    [convictionText, convictionCondition]
// }
// Function to determine colors for conviction
getColorForConviction(convictionCondition) =>
    convictionBgColor = color.white // Default background color
    convictionTextColor = color.gray // Default text color
    if convictionCondition == "Bullish"
        convictionBgColor := bullishColorInput
        convictionTextColor := color.white
    else if convictionCondition == "Bearish"
        convictionBgColor := bearishColorInput
        convictionTextColor := color.white
    else if convictionCondition == "Neutral"
        convictionBgColor := color.white
        convictionTextColor := color.gray
    [convictionBgColor, convictionTextColor]
// }

// Initialize the simplified InfoTable based on orientation
var table infoTable = na
if orientationInput == 'Horizontal'
    infoTable := table.new(tablePosition, array.size(timeframes) + 2, 2, bgcolor = color.rgb(0, 0, 0), border_width = 1)
    // Place "Timeframe" and "Conviction" headers in their respective positions
    table.cell(infoTable, 0, 0, "Timeframe", text_color = color.white)
    table.cell(infoTable, 0, 1, "Conviction", text_color = color.white)
else
    // For vertical orientation, assume you want two columns (one for Timeframe and one for Conviction), but many rows
    infoTable := table.new(tablePosition, 2, array.size(timeframes) + 2, bgcolor = color.rgb(0, 0, 0), border_width = 1)
    // Place "Timeframe" and "Conviction" headers in their respective positions
    table.cell(infoTable, 0, 0, "TF", text_color = color.white) // Header for timeframes
    table.cell(infoTable, 1, 0, "CV", text_color = color.white) // Header for convictions
// }
// Function to calculate and return column and row indices based on orientation
calculateIndices(orientation, currentColumn, currentRow, maxColumn, maxRow) =>
    int newColumn = currentColumn
    int newRow = currentRow
    if orientation == 'Horizontal'
        // Increment column, wrap and move to next row if at max
        newColumn := newColumn + 1
        if newColumn > maxColumn
            newColumn := 1
            newRow := math.min(newRow + 1, maxRow) // Ensure newRow does not exceed maxRow
    else
        // Increment row, wrap and move to next column if at max
        newRow := newRow + 1
        if newRow > maxRow
            newRow := 1
            newColumn := math.min(newColumn + 1, maxColumn) // Ensure newColumn does not exceed maxColumn
    [newColumn, newRow]
// }
// Declare variables once
var int currentColumn = 0
var int currentRow = 0
var int maxColumn = na
var int maxRow = na
// Define a function or direct calls to add data to the table, corresponding to each timeframe
if (showTableInput)
    currentColumn := orientationInput == 'Horizontal' ? 1 : 0 // Start at row 1 for Horizontal (for labels), row 0 for Vertical (for data)
    currentRow := orientationInput == 'Horizontal' ? 0 : 1 // Start at row 0 for Horizontal (for labels), row 1 for Vertical (for data)
    // Initialize maxColumn and maxRow based on orientation
    maxColumn := orientationInput == 'Horizontal' ? array.size(timeframes) + 1 : 2
    maxRow := orientationInput == 'Vertical' ? array.size(timeframes) + 1 : 2
// 30 Second
    [column_30s, row_30s] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    [convictionText_30s, convictionCondition_30s] = getConviction(close, "30S")
    [convictionBgColor_30s, convictionTextColor_30s] = getColorForConviction(convictionCondition_30s)
    // table.cell(infoTable, 1, 0, "30s", text_color=color.white)
    // table.cell(infoTable, 1, 1, convictionText_30s, bgcolor=convictionBgColor_30s, text_color=convictionTextColor_30s)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_30s : 0, orientationInput == 'Horizontal' ? 0: row_30s, "30s", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_30s : 1, orientationInput == 'Horizontal' ? 1: row_30s, convictionText_30s, bgcolor=convictionBgColor_30s, text_color=convictionTextColor_30s)
// 1 Minute
    [column_1m, row_1m] = calculateIndices(orientationInput, column_30s, row_30s, maxColumn, maxRow)
    [convictionText_1m, convictionCondition_1m] = getConviction(close, "1")
    [convictionBgColor_1m, convictionTextColor_1m] = getColorForConviction(convictionCondition_1m)
    // table.cell(infoTable, 2, 0, "1m", text_color=color.white)
    // table.cell(infoTable, 2, 1, convictionText_1m, bgcolor=convictionBgColor_1m, text_color=convictionTextColor_1m)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_1m : 0, orientationInput == 'Horizontal' ? 0: row_1m, "1m", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_1m : 1, orientationInput == 'Horizontal' ? 1: row_1m, convictionText_1m, bgcolor=convictionBgColor_1m, text_color=convictionTextColor_1m)
// 2 Minute
    [column_2m, row_2m] = calculateIndices(orientationInput, column_1m, row_1m, maxColumn, maxRow)
    [convictionText_2m, convictionCondition_2m] = getConviction(close, "2")
    [convictionBgColor_2m, convictionTextColor_2m] = getColorForConviction(convictionCondition_2m)
    // table.cell(infoTable, 3, 0, "2m", text_color=color.white)
    // table.cell(infoTable, 3, 1, convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_2m : 0, orientationInput == 'Horizontal' ? 0: row_2m, "2m", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_2m : 1, orientationInput == 'Horizontal' ? 1: row_2m, convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m)
// 3 Minute
    [column_3m, row_3m] = calculateIndices(orientationInput, column_2m, row_2m, maxColumn, maxRow)
    [convictionText_3m, convictionCondition_3m] = getConviction(close, "3")
    [convictionBgColor_3m, convictionTextColor_3m] = getColorForConviction(convictionCondition_3m)
    // table.cell(infoTable, 4, 0, "3m", text_color=color.white)
    // table.cell(infoTable, 4, 1, convictionText_3m, bgcolor=convictionBgColor_3m, text_color=convictionTextColor_3m)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_3m : 0, orientationInput == 'Horizontal' ? 0: row_3m, "3m", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_3m : 1, orientationInput == 'Horizontal' ? 1: row_3m, convictionText_3m, bgcolor=convictionBgColor_3m, text_color=convictionTextColor_3m)
// 5 Minute
    [column_5m, row_5m] = calculateIndices(orientationInput, column_3m, row_3m, maxColumn, maxRow)
    [convictionText_5m, convictionCondition_5m] = getConviction(close, "5")
    [convictionBgColor_5m, convictionTextColor_5m] = getColorForConviction(convictionCondition_5m)
    // table.cell(infoTable, 5, 0, "5m", text_color=color.white)
    // table.cell(infoTable, 5, 1, convictionText_5m, bgcolor=convictionBgColor_5m, text_color=convictionTextColor_5m)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_5m : 0, orientationInput == 'Horizontal' ? 0: row_5m, "5m", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_5m : 1, orientationInput == 'Horizontal' ? 1: row_5m, convictionText_5m, bgcolor=convictionBgColor_5m, text_color=convictionTextColor_5m)
// 10 Minute
    [column_10m, row_10m] = calculateIndices(orientationInput, column_5m, row_5m, maxColumn, maxRow)
    [convictionText_10m, convictionCondition_10m] = getConviction(close, "10")
    [convictionBgColor_10m, convictionTextColor_10m] = getColorForConviction(convictionCondition_10m)
    // table.cell(infoTable, 6, 0, "10m", text_color=color.white)
    // table.cell(infoTable, 6, 1, convictionText_10m, bgcolor=convictionBgColor_10m, text_color=convictionTextColor_10m)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_10m : 0, orientationInput == 'Horizontal' ? 0: row_10m, "10m", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_10m : 1, orientationInput == 'Horizontal' ? 1: row_10m, convictionText_10m, bgcolor=convictionBgColor_10m, text_color=convictionTextColor_10m)
// 15 Minute
    [column_15m, row_15m] = calculateIndices(orientationInput, column_10m, row_10m, maxColumn, maxRow)
    [convictionText_15m, convictionCondition_15m] = getConviction(close, "15")
    [convictionBgColor_15m, convictionTextColor_15m] = getColorForConviction(convictionCondition_15m)
    // table.cell(infoTable, 7, 0, "15m", text_color=color.white)
    // table.cell(infoTable, 7, 1, convictionText_15m, bgcolor=convictionBgColor_15m, text_color=convictionTextColor_15m)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_15m : 0, orientationInput == 'Horizontal' ? 0: row_15m, "15m", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_15m : 1, orientationInput == 'Horizontal' ? 1: row_15m, convictionText_15m, bgcolor=convictionBgColor_15m, text_color=convictionTextColor_15m)
// 30 Minute
    [column_30m, row_30m] = calculateIndices(orientationInput, column_15m, row_15m, maxColumn, maxRow)
    [convictionText_30m, convictionCondition_30m] = getConviction(close, "30")
    [convictionBgColor_30m, convictionTextColor_30m] = getColorForConviction(convictionCondition_30m)
    // table.cell(infoTable, 8, 0, "30m", text_color=color.white)
    // table.cell(infoTable, 8, 1, convictionText_30m, bgcolor=convictionBgColor_30m, text_color=convictionTextColor_30m)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_30m : 0, orientationInput == 'Horizontal' ? 0: row_30m, "30m", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_30m : 1, orientationInput == 'Horizontal' ? 1: row_30m, convictionText_30m, bgcolor=convictionBgColor_30m, text_color=convictionTextColor_30m)
// 1 Hour
    [column_1h, row_1h] = calculateIndices(orientationInput, column_30m, row_30m, maxColumn, maxRow)
    [convictionText_1h, convictionCondition_1h] = getConviction(close, "60")
    [convictionBgColor_1h, convictionTextColor_1h] = getColorForConviction(convictionCondition_1h)
    // table.cell(infoTable, 9, 0, "1h", text_color=color.white)
    // table.cell(infoTable, 9, 1, convictionText_1h, bgcolor=convictionBgColor_1h, text_color=convictionTextColor_1h)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_1h : 0, orientationInput == 'Horizontal' ? 0: row_1h, "1h", text_color=color.white)
    table.cell(infoTable, orientationInput == 'Horizontal' ? column_1h : 1, orientationInput == 'Horizontal' ? 1: row_1h, convictionText_1h, bgcolor=convictionBgColor_1h, text_color=convictionTextColor_1h)
