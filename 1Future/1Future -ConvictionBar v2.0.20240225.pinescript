//Vertical Only

//@version=5
indicator("1F- ConvictionBar -Vertical", overlay=true)

// Assuming other initializations and function definitions remain as previously defined...
// User inputs
rsiLengthInput = input.int(14, minval=1, title="RSI Length")
maLengthInput = input.int(14, title="MA Length")
showTableInput = input.bool(true, title="Show RSI & MA Table")
tablePositionInput = input.string("Bottom left", title="Table Position", options=["Top left", "Top right", "Bottom left", "Bottom right", "Middle left", "Middle right"])
maTypeInput = input.string("SMA", title="MA Type", options=["SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="MA Settings")
rsiSourceInput = input.source(close, "Source", group="RSI Settings")

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
var table infoTable = table.new(tablePosition, 2, 10, bgcolor = color.rgb(0, 0, 0), border_width = 1)
// Header for timeframes
table.cell(infoTable, 0, 0, "TF", text_color = color.white)
// Header for convictions
table.cell(infoTable, 1, 0, "Conviction", text_color = color.white)

// Simplified function to determine colors for conviction
getColorForConviction(convictionCondition) =>
    convictionBgColor = color.white // Default background color
    convictionTextColor = color.gray // Default text color
    if convictionCondition == "Bullish"
        convictionBgColor := color.red
        convictionTextColor := color.yellow
    else if convictionCondition == "Bearish"
        convictionBgColor := color.green
        convictionTextColor := color.blue
    else if convictionCondition == "Neutral"
        convictionBgColor := color.white
        convictionTextColor := color.gray
    [convictionBgColor, convictionTextColor]

// Simplified addTableRow function for Time Frame and Conviction
addData(columnIndex, timeframe, convictionText, convictionCondition) =>
    [convictionBgColor, convictionTextColor] = getColorForConviction(convictionCondition)

    // Apply the conviction colors to the table cells
    table.cell(infoTable, 0, columnIndex, timeframe, text_color=color.white)
    table.cell(infoTable, 1, columnIndex, convictionText, bgcolor=convictionBgColor, text_color=convictionTextColor)

// Example usage within your script to add rows for different timeframes
// if (showTableInput)
//     // Assuming getConviction function returns just the conviction string for simplicity
//     [convictionText_1m, convictionCondition_1m] = getConviction(close, "1")
//     [convictionText_5m, convictionCondition_5m] = getConviction(close, "5")
//     addTableRow(1, "1m", convictionText_1m, convictionCondition_1m)
//     addTableRow(2, "5m", convictionText_5m, convictionCondition_5m)


// if (showTableInput)
//     // Directly assign convictions for each timeframe; consider restructuring to avoid repetitive calls
//     // Example placeholder for the first timeframe; repeat for others as needed
//     [convictionText_1m, convictionCondition_1m] = getConviction(close, "1m")
//     addTableRow(1, "1m", convictionText_1m, convictionCondition_1m)
//     // Note: You would repeat the above two lines for each timeframe, adjusting the index accordingly.
if (showTableInput)
    // 1 Minute
    [convictionText_1m, convictionCondition_1m] = getConviction(close, "1")
    addData(1, "1m", convictionText_1m, convictionCondition_1m)
    // columnIndex := columnIndex + 1

    // 2 Minutes
    [convictionText_2m, convictionCondition_2m] = getConviction(close, "2")
    addData(2, "2m", convictionText_2m, convictionCondition_2m)
    // columnIndex := columnIndex + 1

    // 3 Minutes
    [convictionText_3m, convictionCondition_3m] = getConviction(close, "3")
    addData(3, "3m", convictionText_3m, convictionCondition_3m)
    // columnIndex := columnIndex + 1

    // // 5 Minutes
    [convictionText_5m, convictionCondition_5m] = getConviction(close, "5")
    addData(4, "5m", convictionText_5m, convictionCondition_5m)
    // columnIndex := columnIndex + 1

    // // 10 Minutes
    [convictionText_10m, convictionCondition_10m] = getConviction(close, "10")
    addData(5, "10m", convictionText_10m, convictionCondition_10m)
    // columnIndex := columnIndex + 1

    // // 15 Minutes
    [convictionText_15m, convictionCondition_15m] = getConviction(close, "15")
    addData(6, "15m", convictionText_15m, convictionCondition_15m)
    // columnIndex := columnIndex + 1

    // // 30 Minutes
    [convictionText_30m, convictionCondition_30m] = getConviction(close, "30")
    addData(7, "30m", convictionText_30m, convictionCondition_30m)
    // columnIndex := columnIndex + 1

    // // 60 Minutes
    [convictionText_60m, convictionCondition_60m] = getConviction(close, "60")
    addData(8, "60m", convictionText_60m, convictionCondition_60m)
