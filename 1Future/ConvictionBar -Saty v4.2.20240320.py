// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Oneome

//@version=5
indicator("1Future: ConvictionBar -Saty", overlay=true)

// User inputs
themeInput = input.string(defval = "Dark", title = "Theme:", options = ["Dark", "Light"], inline = "Global")
sizeInput = input.string(defval = "Auto", title = "Widget Size:", options = ["Auto", "Tiny", "Small", "Normal", "Large"], inline = "Global")
tablePositionInput = input.string("Top-Right", title="Position:", options=["Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right", "Middle-Left", "Middle-Right"], inline = "Table")
orientationInput = input.string(defval = 'Horizontal', title = 'Orientation:', options = ['Horizontal', 'Vertical'], inline = "Table")

tf15sInput = input.bool(true, title="15s", group = "Timeframes", inline = "TFL")
tf30sInput = input.bool(true, title="30s", group = "Timeframes", inline = "TFL")
tf1mInput = input.bool(true, title="1m", group = "Timeframes", inline = "TFL")
tf2mInput = input.bool(true, title="2m", group = "Timeframes", inline = "TFL")
tf3mInput = input.bool(true, title="3m", group = "Timeframes", inline = "TFL")
tf4mInput = input.bool(true, title="4m", group = "Timeframes", inline = "TFL")
tf5mInput = input.bool(true, title="5m", group = "Timeframes", inline = "TFL")
tf6mInput = input.bool(true, title="6m", group = "Timeframes", inline = "TFM")
tf7mInput = input.bool(true, title="7m", group = "Timeframes", inline = "TFM")
tf8mInput = input.bool(true, title="8m", group = "Timeframes", inline = "TFM")
tf9mInput = input.bool(true, title="9m", group = "Timeframes", inline = "TFM")
tf10mInput = input.bool(true, title="10m", group = "Timeframes", inline = "TFM")
tf11mInput = input.bool(true, title="11m", group = "Timeframes", inline = "TFM")
tf13mInput = input.bool(true, title="13m", group = "Timeframes", inline = "TFH")
tf15mInput = input.bool(true, title="15m", group = "Timeframes", inline = "TFH")
tf20mInput = input.bool(true, title="20m", group = "Timeframes", inline = "TFH")
tf30mInput = input.bool(true, title="30m", group = "Timeframes", inline = "TFH")
tf1hInput = input.bool(true, title="1h", group = "Timeframes", inline = "TFH")
tf4hInput = input.bool(false, title="4h", group = "Timeframes", inline = "TFH")
tf1dInput = input.bool(false, title="1D", group = "Timeframes", inline = "TFH")

bullishTextInput = input.string(defval = "▲", title = "Bullish Sign:", group = "Design", inline = "Text")
bearishTextInput = input.string(defval = "▼", title = "Bearish Sign:", group = "Design", inline = "Text")
bullishColorInput = input.color(color.green, title="Bull Conviction Color:", group = "Design", inline = "Colour")
bearishColorInput = input.color(color.red, title="Bear Conviction Color:", group = "Design", inline = "Colour")

// Setting widget size
textSize = size.auto
if sizeInput == "Auto"
    textSize := size.auto
else if sizeInput == "Tiny"
    textSize := size.tiny
else if sizeInput == "Small"
    textSize := size.small
else if sizeInput == "Normal"
    textSize := size.normal
else if sizeInput == "Large"
    textSize := size.large

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
//

// Initialize an array for timeframes
var string[] timeframes = array.new_string()
if (array.size(timeframes) == 0)
    if (tf15sInput)
        array.push(timeframes, "15s")
    if (tf30sInput)
        array.push(timeframes, "30s")
    if (tf1mInput)
        array.push(timeframes, "1m")
    if (tf2mInput)
        array.push(timeframes, "2m")
    if (tf3mInput)
        array.push(timeframes, "3m")
    if (tf4mInput)
        array.push(timeframes, "4m")
    if (tf5mInput)
        array.push(timeframes, "5m")
    if (tf6mInput)
        array.push(timeframes, "6m")
    if (tf7mInput)
        array.push(timeframes, "7m")
    if (tf8mInput)
        array.push(timeframes, "8m")
    if (tf9mInput)
        array.push(timeframes, "9m")
    if (tf10mInput)
        array.push(timeframes, "11m")
    if (tf11mInput)
        array.push(timeframes, "10m")
    if (tf13mInput)
        array.push(timeframes, "13m")
    if (tf15mInput)
        array.push(timeframes, "15m")
    if (tf20mInput)
        array.push(timeframes, "20m")
    if (tf30mInput)
        array.push(timeframes, "30m")
    if (tf1hInput)
        array.push(timeframes, "60m")
    if (tf4hInput)
        array.push(timeframes, "240m")
    if (tf1dInput)
        array.push(timeframes, "1D")
//
// Initialize an array for timeframes
var string[] convictions = array.new_string(1, "Saty")

// Function to calculate Conviction based on fast and slow EMA
getConviction(src, tf, convictionType) =>
    // Determine EMA periods based on the convictionType : Here ConvictionType will be defined as only Saty
    fastEmaPeriod = convictionType == "Saty(13-48)" ? 13 : convictionType == "Ripster(05-12)" ? 5 : 34
    slowEmaPeriod = convictionType == "Saty(13-48)" ? 48 : convictionType == "Ripster(05-12)" ? 12 : 50
    // Calculate EMAs
    fastEma = request.security(syminfo.tickerid, tf, ta.ema(src, fastEmaPeriod))
    slowEma = request.security(syminfo.tickerid, tf, ta.ema(src, slowEmaPeriod))
    // Determine conviction text and condition
    convictionText = fastEma > slowEma ? bullishTextInput : fastEma < slowEma ? bearishTextInput : "■"
    convictionCondition = fastEma > slowEma ? "Bullish" : fastEma < slowEma ? "Bearish" : "Neutral"
    // Determine colors based on the conviction condition
    convictionBgColor = convictionCondition == "Bullish" ? bullishColorInput : convictionCondition == "Bearish" ? bearishColorInput : color.white
    convictionTextColor = convictionCondition == "Neutral" ? color.gray : color.white
    // Return all calculated values
    [convictionText, convictionCondition, convictionBgColor, convictionTextColor]
//

// Set Theme Text and Background Color
var themeText = color.red
var themeBg = color.blue
themeText := themeInput == "Dark" ? color.white : color.black
themeBg := themeInput == "Dark" ? color.black : color.white

// Function to calculate and return column and row indices based on orientation
calculateIndices(orientation, currentColumn, currentRow, maxColumn, maxRow) =>
    int newColumn = currentColumn
    int newRow = currentRow

    if orientation == 'Horizontal'
        newColumn := newColumn < maxColumn ? newColumn + 1 : maxColumn
        newRow := 0
    else
        newColumn := 0
        newRow := newRow > 0  ? newRow - 1 : 1
    [newColumn, newRow]
//

// Initialize the InfoTable With Total Column and Rows
var table infoTable = na
if orientationInput == 'Horizontal'
    infoTable := table.new(tablePosition, array.size(timeframes) + 2, array.size(convictions) + 1, bgcolor = themeBg, border_width = 1)
    // Place "Timeframe" and "Conviction" headers in their respective positions
    table.cell(infoTable, 0, 0, "Timeframe", text_color = themeText, text_size = textSize)
    table.cell(infoTable, 0, 1, "Conviction", text_color = themeText, text_size = textSize)
else
    // For vertical orientation, assume you want two columns (one for Timeframe and one for Conviction), but many rows
    infoTable := table.new(tablePosition, array.size(convictions) + 1, array.size(timeframes) + 2, bgcolor = themeBg, border_width = 1)
    // Place "Timeframe" and "Conviction" headers in their respective positions
    table.cell(infoTable, 0, 0, "TF", text_color = themeText, text_size = textSize) // Header for timeframes
    table.cell(infoTable, 1, 0, "CV", text_color = themeText, text_size = textSize) // Header for convictions
//

// Declare variables once
var int currentColumn = 0
var int currentRow = 0
var int maxColumn = na
var int maxRow = na
var string convictionType = "Saty(13-48)"

// Initialize maxColumn and maxRow based on orientation
maxColumn := orientationInput == 'Horizontal' ? array.size(timeframes) : array.size(convictions)
maxRow := orientationInput == 'Horizontal' ? array.size(convictions) : array.size(timeframes)
// Direct calls to add data to the table, corresponding to each timeframe
currentColumn := orientationInput == 'Horizontal' ? 0 : 0 // Start at left-top corner for Horizontal, left-bottom corner for Vertical
currentRow := orientationInput == 'Horizontal' ? 0 : maxRow +1 // Start at left-top corner for Horizontal, left-bottom corner for Vertical


// 15 Second
if (tf15sInput)
    [column_15s, row_15s] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_15s
    currentRow := row_15s
    [convictionText_15s, convictionCondition_15s, convictionBgColor_15s, convictionTextColor_15s] = getConviction(close, "15S", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "15s", text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow, convictionText_15s, bgcolor=convictionBgColor_15s, text_color=convictionTextColor_15s, text_size = textSize)
// 30 Second
if (tf30sInput)
    [column_30s, row_30s] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_30s
    currentRow := row_30s
    [convictionText_30s, convictionCondition_30s, convictionBgColor_30s, convictionTextColor_30s] = getConviction(close, "30S", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "30s",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1, orientationInput == 'Horizontal' ? currentRow + 1: currentRow, convictionText_30s,bgcolor=convictionBgColor_30s, text_color=convictionTextColor_30s, text_size = textSize)
// 1 Minute
if (tf1mInput)
    [column_1m, row_1m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_1m
    currentRow := row_1m
    [convictionText_1m, convictionCondition_1m, convictionBgColor_1m, convictionTextColor_1m] = getConviction(close, "1", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "1m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_1m,bgcolor=convictionBgColor_1m,text_color=convictionTextColor_1m, text_size = textSize)
// 2 Minute
if (tf2mInput)
    [column_2m, row_2m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_2m
    currentRow := row_2m
    [convictionText_2m, convictionCondition_2m, convictionBgColor_2m, convictionTextColor_2m] = getConviction(close, "2", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "2m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m, text_size = textSize)
// 3 Minute
if (tf3mInput)
    [column_3m, row_3m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_3m
    currentRow := row_3m
    [convictionText_3m, convictionCondition_3m, convictionBgColor_3m, convictionTextColor_3m] = getConviction(close, "3", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "3m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_3m,bgcolor=convictionBgColor_3m, text_color=convictionTextColor_3m, text_size = textSize)
// 4 Minute
if (tf4mInput)
    [column_4m, row_4m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_4m
    currentRow := row_4m
    [convictionText_4m, convictionCondition_4m, convictionBgColor_4m, convictionTextColor_4m] = getConviction(close, "4", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "4m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_4m,bgcolor=convictionBgColor_4m, text_color=convictionTextColor_4m, text_size = textSize)
// 5 Minute
if (tf5mInput)
    [column_5m, row_5m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_5m
    currentRow := row_5m
    [convictionText_5m, convictionCondition_5m, convictionBgColor_5m, convictionTextColor_5m] = getConviction(close, "5", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "5m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_5m,bgcolor=convictionBgColor_5m, text_color=convictionTextColor_5m, text_size = textSize)
// 6 Minute
if (tf6mInput)
    [column_6m, row_6m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_6m
    currentRow := row_6m
    [convictionText_6m, convictionCondition_6m, convictionBgColor_6m, convictionTextColor_6m] = getConviction(close, "6", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "6m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_6m, bgcolor=convictionBgColor_6m, text_color=convictionTextColor_6m, text_size = textSize)
// 7 Minute
if (tf7mInput)
    [column_7m, row_7m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_7m
    currentRow := row_7m
    [convictionText_7m, convictionCondition_7m, convictionBgColor_7m, convictionTextColor_7m] = getConviction(close, "7", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "7m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_7m,bgcolor=convictionBgColor_7m, text_color=convictionTextColor_7m, text_size = textSize)
// 8 Minute
if (tf8mInput)
    [column_8m, row_8m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_8m
    currentRow := row_8m
    [convictionText_8m, convictionCondition_8m, convictionBgColor_8m, convictionTextColor_8m] = getConviction(close, "8", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "8m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_8m,bgcolor=convictionBgColor_8m, text_color=convictionTextColor_8m, text_size = textSize)
// 9 Minute
if (tf9mInput)
    [column_9m, row_9m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_9m
    currentRow := row_9m
    [convictionText_9m, convictionCondition_9m, convictionBgColor_9m, convictionTextColor_9m] = getConviction(close, "9", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "9m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_9m, bgcolor=convictionBgColor_9m, text_color=convictionTextColor_9m, text_size = textSize)
// 10 Minute
if (tf10mInput)
    [column_10m, row_10m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_10m
    currentRow := row_10m
    [convictionText_10m, convictionCondition_10m, convictionBgColor_10m, convictionTextColor_10m] = getConviction(close, "10", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "10m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_10m,bgcolor=convictionBgColor_10m, text_color=convictionTextColor_10m, text_size = textSize)
// 11 Minute
if (tf11mInput)
    [column_11m, row_11m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_11m
    currentRow := row_11m
    [convictionText_11m, convictionCondition_11m, convictionBgColor_11m, convictionTextColor_11m] = getConviction(close, "11", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "11m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_11m, bgcolor=convictionBgColor_11m, text_color=convictionTextColor_11m, text_size = textSize)
// 13 Minute
if (tf13mInput)
    [column_13m, row_13m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_13m
    currentRow := row_13m
    [convictionText_13m, convictionCondition_13m, convictionBgColor_13m, convictionTextColor_13m] = getConviction(close, "13", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "13m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow, convictionText_13m, bgcolor=convictionBgColor_13m, text_color=convictionTextColor_13m, text_size = textSize)
// 15 Minute
if (tf15mInput)
    [column_15m, row_15m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_15m
    currentRow := row_15m
    [convictionText_15m, convictionCondition_15m, convictionBgColor_15m, convictionTextColor_15m] = getConviction(close, "15", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "15m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_15m,bgcolor=convictionBgColor_15m, text_color=convictionTextColor_15m, text_size = textSize)
// 20 Minute
if (tf20mInput)
    [column_20m, row_20m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_20m
    currentRow := row_20m
    [convictionText_20m, convictionCondition_20m, convictionBgColor_20m, convictionTextColor_20m] = getConviction(close, "20", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "20m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_20m,bgcolor=convictionBgColor_20m, text_color=convictionTextColor_20m, text_size = textSize)
// 30 Minute
if (tf30mInput)
    [column_30m, row_30m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_30m
    currentRow := row_30m
    [convictionText_30m, convictionCondition_30m, convictionBgColor_30m, convictionTextColor_30m] = getConviction(close, "30", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "30m",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_30m,bgcolor=convictionBgColor_30m, text_color=convictionTextColor_30m, text_size = textSize)
// 1 Hour
if (tf1hInput)
    [column_1h, row_1h] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_1h
    currentRow := row_1h
    [convictionText_1h, convictionCondition_1h, convictionBgColor_1h, convictionTextColor_1h] = getConviction(close, "60", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "1hr",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow,convictionText_1h,bgcolor=convictionBgColor_1h, text_color=convictionTextColor_1h, text_size = textSize)
// 4 Hour
if (tf4hInput)
    [column_4h, row_4h] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_4h
    currentRow := row_4h
    [convictionText_4h, convictionCondition_4h, convictionBgColor_4h, convictionTextColor_4h] = getConviction(close, "240", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "4hr",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow, convictionText_4h,bgcolor=convictionBgColor_4h, text_color=convictionTextColor_4h, text_size = textSize)
// 1 Day
if (tf1dInput)
    [column_1D, row_1D] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
    currentColumn := column_1D
    currentRow := row_1D
    [convictionText_1D, convictionCondition_1D, convictionBgColor_1D, convictionTextColor_1D] = getConviction(close, "1D", convictionType)
    table.cell(infoTable, currentColumn, currentRow, "1D",text_color=themeText, text_size = textSize)
    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : currentColumn + 1,orientationInput == 'Horizontal' ? currentRow + 1: currentRow, convictionText_1D, bgcolor=convictionBgColor_1D, text_color=convictionTextColor_1D, text_size = textSize)
