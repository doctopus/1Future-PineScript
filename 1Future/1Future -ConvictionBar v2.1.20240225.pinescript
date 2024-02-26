// Horizontal Only

//@version=5
indicator("1F- ConvictionBar -Horizontal", overlay=true)

// Assuming other initializations and function definitions remain as previously defined...
// User inputs
rsiLengthInput = input.int(14, minval=1, title="RSI Length")
maLengthInput = input.int(14, title="MA Length")
showTableInput = input.bool(true, title="Show RSI & MA Table")
tablePositionInput = input.string("Bottom left", title="Table Position", options=["Top left", "Top right", "Bottom left", "Bottom right", "Middle left", "Middle right"])
maTypeInput = input.string("SMA", title="MA Type", options=["SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="MA Settings")
rsiSourceInput = input.source(close, "Source", group="RSI Settings")
var orientation = input.string(defval = 'vertical', title = 'Orientation', options = ['horizontal', 'vertical'])

// Function to calculate Conviction based on fast and slow EMA
getConviction(src, tf) =>
    fastEma = request.security(syminfo.tickerid, tf, ta.ema(src, 13))
    slowEma = request.security(syminfo.tickerid, tf, ta.ema(src, 48))
    convictionText = fastEma > slowEma ? "↑😎" : fastEma < slowEma ? "↓😡" : "→😑"
    convictionCondition = fastEma > slowEma ? "Bullish" : fastEma < slowEma ? "Bearish" : "Neutral"
    [convictionText, convictionCondition]

// Setting table position
tablePosition = position.top_right
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

//
// Initialize an array for timeframes
var string[] timeframes = array.new_string()
// Populate the array with timeframes
array.push(timeframes, "1m")
array.push(timeframes, "2m")
array.push(timeframes, "3m")
array.push(timeframes, "5m")
array.push(timeframes, "10m")
array.push(timeframes, "15m")
array.push(timeframes, "30m")
array.push(timeframes, "60m")

// Initialize the simplified InfoTable with just two columns
var table infoTable = table.new(tablePosition, 10, 2, bgcolor = color.rgb(0, 0, 0), border_width = 1)
// Header for timeframes
table.cell(infoTable, 0, 0, "TF", text_color = color.white)
// Header for convictions
table.cell(infoTable, 0, 1, "Conviction", text_color = color.white)

// Simplified function to determine colors for conviction
getColorForConviction(convictionCondition) =>
    convictionBgColor = color.white // Default background color
    convictionTextColor = color.gray // Default text color
    if convictionCondition == "Bullish"
        convictionBgColor := color.green
        convictionTextColor := color.yellow
    else if convictionCondition == "Bearish"
        convictionBgColor := color.red
        convictionTextColor := color.blue
    else if convictionCondition == "Neutral"
        convictionBgColor := color.white
        convictionTextColor := color.gray
    [convictionBgColor, convictionTextColor]

// Simplified addTableRow function for Time Frame and Conviction
addData(columnIndex, timeframe, convictionText, convictionCondition) =>
    [convictionBgColor, convictionTextColor] = getColorForConviction(convictionCondition)

    // Apply the conviction colors to the table cells
    table.cell(infoTable, 0, 0, timeframe, text_color=color.white)
    table.cell(infoTable, 0, 1, columnIndex, convictionText, bgcolor=convictionBgColor, text_color=convictionTextColor)
    table.cell(infoTable, 1, 0, "1m", text_color=color.white)
    table.cell(infoTable, 2, 0, "2m", text_color=color.white)
    table.cell(infoTable, 3, 0, "3m", text_color=color.white)
    table.cell(infoTable, 4, 0, "5m", text_color=color.white)
    table.cell(infoTable, 5, 0, "15m", text_color=color.white)

// Define a function or direct calls to add data to the table, corresponding to each timeframe
if (showTableInput)
    // Manually call getConviction for each timeframe
    [convictionText_1m, convictionCondition_1m] = getConviction(close, "1")
    [convictionText_2m, convictionCondition_2m] = getConviction(close, "2")
    [convictionText_3m, convictionCondition_3m] = getConviction(close, "3")
    [convictionText_5m, convictionCondition_5m] = getConviction(close, "5")
    [convictionText_15m, convictionCondition_15m] = getConviction(close, "15")
    // Continue for other timeframes...

    // Manually update the table for each timeframe
    table.cell(infoTable, 1, 0, "1m", text_color=color.white)
    [convictionBgColor_1m, convictionTextColor_1m] = getColorForConviction(convictionCondition_1m)
    table.cell(infoTable, 1, 1, convictionText_1m, bgcolor=convictionBgColor_1m, text_color=convictionTextColor_1m)

    table.cell(infoTable, 2, 0, "2m", text_color=color.white)
    [convictionBgColor_2m, convictionTextColor_2m] = getColorForConviction(convictionCondition_2m)
    table.cell(infoTable, 2, 1, convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m)

    table.cell(infoTable, 3, 0, "3m", text_color=color.white)
    [convictionBgColor_3m, convictionTextColor_3m] = getColorForConviction(convictionCondition_3m)
    table.cell(infoTable, 3, 1, convictionText_3m, bgcolor=convictionBgColor_3m, text_color=convictionTextColor_3m)

    table.cell(infoTable, 4, 0, "5m", text_color=color.white)
    [convictionBgColor_5m, convictionTextColor_5m] = getColorForConviction(convictionCondition_5m)
    table.cell(infoTable, 4, 1, convictionText_5m, bgcolor=convictionBgColor_5m, text_color=convictionTextColor_5m)

    table.cell(infoTable, 5, 0, "15m", text_color=color.white)
    [convictionBgColor_15m, convictionTextColor_15m] = getColorForConviction(convictionCondition_15m)
    table.cell(infoTable, 5, 1, convictionText_15m, bgcolor=convictionBgColor_15m, text_color=convictionTextColor_15m)
