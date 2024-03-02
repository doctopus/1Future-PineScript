// Horizontal Only: More Modular

//@version=5
indicator("1F- ConvictionBar", overlay=true)

// User inputs
showTableInput = input.bool(true, title="Show Conviction Bar")
tablePositionInput = input.string("Top right", title="Table Position", options=["Top left", "Top right", "Bottom left", "Bottom right", "Middle left", "Middle right"])
orientationInput = input.string(defval = 'Horizontal', title = 'Table Orientation', options = ['Horizontal', 'Vertical'])
bullishTextInput = input.string(defval = "↑😎", title = "Bullish Conviction Text")
bearishTextInput = input.string(defval = "↓👽", title = "Bearish Conviction Text")
neutralTextInput = input.string(defval = "→🤢", title = "Neutral Conviction Text")
// Function to calculate Conviction based on fast and slow EMA
getConviction(src, tf) =>
    fastEma = request.security(syminfo.tickerid, tf, ta.ema(src, 13))
    slowEma = request.security(syminfo.tickerid, tf, ta.ema(src, 48))
    convictionText = fastEma > slowEma ? bullishTextInput : fastEma < slowEma ? bearishTextInput : neutralTextInput
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
//}
// Initialize an array for timeframes
var string[] timeframes = array.new_string()
array.push(timeframes, "1m")
array.push(timeframes, "2m")
array.push(timeframes, "3m")
array.push(timeframes, "5m")
array.push(timeframes, "10m")
array.push(timeframes, "15m")
array.push(timeframes, "30m")
array.push(timeframes, "60m")

// Function to determine colors for conviction
getColorForConviction(convictionCondition) =>
    convictionBgColor = color.white // Default background color
    convictionTextColor = color.gray // Default text color
    if convictionCondition == "Bullish"
        convictionBgColor := color.green
        convictionTextColor := color.white
    else if convictionCondition == "Bearish"
        convictionBgColor := color.red
        convictionTextColor := color.white
    else if convictionCondition == "Neutral"
        convictionBgColor := color.white
        convictionTextColor := color.gray
    [convictionBgColor, convictionTextColor]


// Initialize the simplified InfoTable
var table infoTable = table.new(tablePosition, 10, 2, bgcolor = color.rgb(0, 0, 0), border_width = 1)
// Header for timeframes
table.cell(infoTable, 0, 0, "Timeframe", text_color = color.white)
// Header for convictions
table.cell(infoTable, 0, 1, "Conviction", text_color = color.white)


// Define a function or direct calls to add data to the table, corresponding to each timeframe
if (showTableInput)

    [convictionText_30s, convictionCondition_30s] = getConviction(close, "30S")
    table.cell(infoTable, 1, 0, "30s", text_color=color.white)
    [convictionBgColor_30s, convictionTextColor_30s] = getColorForConviction(convictionCondition_30s)
    table.cell(infoTable, 1, 1, convictionText_30s, bgcolor=convictionBgColor_30s, text_color=convictionTextColor_30s)

    [convictionText_1m, convictionCondition_1m] = getConviction(close, "1")
    table.cell(infoTable, 2, 0, "1m", text_color=color.white)
    [convictionBgColor_1m, convictionTextColor_1m] = getColorForConviction(convictionCondition_1m)
    table.cell(infoTable, 2, 1, convictionText_1m, bgcolor=convictionBgColor_1m, text_color=convictionTextColor_1m)

    [convictionText_2m, convictionCondition_2m] = getConviction(close, "2")
    table.cell(infoTable, 3, 0, "2m", text_color=color.white)
    [convictionBgColor_2m, convictionTextColor_2m] = getColorForConviction(convictionCondition_2m)
    table.cell(infoTable, 3, 1, convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m)

    [convictionText_3m, convictionCondition_3m] = getConviction(close, "3")
    table.cell(infoTable, 4, 0, "3m", text_color=color.white)
    [convictionBgColor_3m, convictionTextColor_3m] = getColorForConviction(convictionCondition_3m)
    table.cell(infoTable, 4, 1, convictionText_3m, bgcolor=convictionBgColor_3m, text_color=convictionTextColor_3m)

    [convictionText_5m, convictionCondition_5m] = getConviction(close, "5")
    table.cell(infoTable, 5, 0, "5m", text_color=color.white)
    [convictionBgColor_5m, convictionTextColor_5m] = getColorForConviction(convictionCondition_5m)
    table.cell(infoTable, 5, 1, convictionText_5m, bgcolor=convictionBgColor_5m, text_color=convictionTextColor_5m)

    [convictionText_10m, convictionCondition_10m] = getConviction(close, "10")
    table.cell(infoTable, 6, 0, "10m", text_color=color.white)
    [convictionBgColor_10m, convictionTextColor_10m] = getColorForConviction(convictionCondition_10m)
    table.cell(infoTable, 6, 1, convictionText_10m, bgcolor=convictionBgColor_10m, text_color=convictionTextColor_10m)

    [convictionText_15m, convictionCondition_15m] = getConviction(close, "15")
    table.cell(infoTable, 7, 0, "15m", text_color=color.white)
    [convictionBgColor_15m, convictionTextColor_15m] = getColorForConviction(convictionCondition_15m)
    table.cell(infoTable, 7, 1, convictionText_15m, bgcolor=convictionBgColor_15m, text_color=convictionTextColor_15m)

    [convictionText_30m, convictionCondition_30m] = getConviction(close, "30")
    table.cell(infoTable, 8, 0, "30m", text_color=color.white)
    [convictionBgColor_30m, convictionTextColor_30m] = getColorForConviction(convictionCondition_30m)
    table.cell(infoTable, 8, 1, convictionText_30m, bgcolor=convictionBgColor_30m, text_color=convictionTextColor_30m)

    [convictionText_1h, convictionCondition_1h] = getConviction(close, "60")
    table.cell(infoTable, 9, 0, "1h", text_color=color.white)
    [convictionBgColor_1h, convictionTextColor_1h] = getColorForConviction(convictionCondition_1h)
    table.cell(infoTable, 9, 1, convictionText_1h, bgcolor=convictionBgColor_1h, text_color=convictionTextColor_1h)
