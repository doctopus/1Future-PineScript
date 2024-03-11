
//@version=5
indicator("1Future: ConvictionBar", overlay=true)

// User inputs
themeInput = input.string(defval = "Light", title = "Theme:", options = ["Dark", "Light"], inline = "Global")
sizeInput = input.string(defval = "Auto", title = "Widget Size:", options = ["Auto", "Tiny", "Small", "Normal", "Large"], inline = "Global")
tablePositionInput = input.string("Top-Right", title="Position:", options=["Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right", "Middle-Left", "Middle-Right"], inline = "Table")
orientationInput = input.string(defval = 'Horizontal', title = 'Orientation:', options = ['Horizontal', 'Vertical'], inline = "Table")

show13_48Input = input.bool(defval = true, title = "Saty(13-48)", inline = "Convictions")
show05_12Input = input.bool(defval = false, title = "Ripster(05-12)", inline = "Convictions")
show34_50Input = input.bool(defval = false, title = "Ripster(34-50)", inline = "Convictions")

tf30sInput = input.bool(true, title="30s", group = "Timeframes", inline = "TFL")
tf1mInput = input.bool(true, title="1m", group = "Timeframes", inline = "TFL")
tf2mInput = input.bool(true, title="2m", group = "Timeframes", inline = "TFL")
tf3mInput = input.bool(true, title="3m", group = "Timeframes", inline = "TFL")
tf4mInput = input.bool(true, title="4m", group = "Timeframes", inline = "TFL")
tf5mInput = input.bool(true, title="5m", group = "Timeframes", inline = "TFL")
tf7mInput = input.bool(true, title="7m", group = "Timeframes", inline = "TFL")
tf10mInput = input.bool(true, title="10m", group = "Timeframes", inline = "TFH")
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
//}
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
    if (tf7mInput)
        array.push(timeframes, "7m")
    if (tf10mInput)
        array.push(timeframes, "10m")
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
//}
// Initialize an array for timeframes
var string[] convictions = array.new_string()
if (array.size(convictions) == 0)
    if (show13_48Input)
        array.push(convictions, "Saty(13-48)")
    if (show05_12Input)
        array.push(convictions, "Ripster(05-12)")
    if (show34_50Input)
        array.push(convictions, "Ripster(34-50)")
//}
// Function to calculate Conviction based on fast and slow EMA
getConviction(src, tf, convictionType) =>
    // Determine EMA periods based on the convictionType
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
    // [convictionText, convictionCondition]
    // Return all calculated values
    [convictionText, convictionCondition, convictionBgColor, convictionTextColor]

//}

// Function to determine colors for conviction
//getColorForConviction(convictionCondition) =>
//    convictionBgColor = color.white // Default background color
//    convictionTextColor = color.gray // Default text color
//    if convictionCondition == "Bullish"
//        convictionBgColor := bullishColorInput
//        convictionTextColor := color.white
//    else if convictionCondition == "Bearish"
//        convictionBgColor := bearishColorInput
//        convictionTextColor := color.white
//    else if convictionCondition == "Neutral"
//        convictionBgColor := color.white
//        convictionTextColor := color.gray
//    [convictionBgColor, convictionTextColor]
//}
// Set Theme Text and Background Color
var themeText = color.red
var themeBg = color.blue
themeText := themeInput == "Dark" ? color.white : color.black
themeBg := themeInput == "Dark" ? color.black : color.white

//if themeInput == "Dark"
//    themeText := color.white
//    themeBg := color.black
//else
//    themeText := color.black
//    themeBg := color.white
//}
// Initialize the simplified InfoTable based on orientation
var table infoTable = na
if orientationInput == 'Horizontal'
    infoTable := table.new(tablePosition, array.size(timeframes) + 2, array.size(convictions) + 3, bgcolor = themeBg, border_width = 1)
    // Place "Timeframe" and "Conviction" headers in their respective positions
    table.cell(infoTable, 0, 0, "Timeframe", text_color = themeText, text_size = textSize)
    for i = 0 to array.size(convictions) - 1
        table.cell(infoTable, 0, i + 1, array.get(convictions, i), text_color = themeText, text_size = textSize)
else
    // For vertical orientation, assume you want two columns (one for Timeframe and one for Conviction), but many rows
    infoTable := table.new(tablePosition, array.size(convictions) + 3, array.size(timeframes) + 2, bgcolor = themeBg, border_width = 1)
    // Place "Timeframe" and "Conviction" headers in their respective positions
    table.cell(infoTable, 0, 0, "TF", text_color = themeText, text_size = textSize) // Header for timeframes
    for i = 0 to array.size(convictions) -1
        table.cell(infoTable, i + 1, 0, array.get(convictions, i), text_color = themeText, text_size = textSize) // Header for convictions
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

// Direct calls to add data to the table, corresponding to each timeframe
currentColumn := orientationInput == 'Horizontal' ? 1 : 0 // Start at row 1 for Horizontal (for labels), row 0 for Vertical (for data)
currentRow := orientationInput == 'Horizontal' ? 0 : 1 // Start at row 0 for Horizontal (for labels), row 1 for Vertical (for data)
// Initialize maxColumn and maxRow based on orientation
maxColumn := orientationInput == 'Horizontal' ? array.size(timeframes) + 1 : 2
maxRow := orientationInput == 'Vertical' ? array.size(timeframes) + 1 : 2

if (show13_48Input)
    //Conditionally Define Conviction Type
    convictionType = show13_48Input ? "Saty(13-48)" : show05_12Input ? "Ripster(05-12)" : "Ripster(34-50)"
    // 30 Second
    if (tf30sInput)
        [column_30s, row_30s] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_30s
        currentRow := row_30s
        [convictionText_30s, convictionCondition_30s, convictionBgColor_30s, convictionTextColor_30s] = getConviction(close, "30S", convictionType)
        //[convictionBgColor_30s, convictionTextColor_30s] = getColorForConviction(convictionCondition_30s)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "30s",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_30s,bgcolor=convictionBgColor_30s, text_color=convictionTextColor_30s, text_size = textSize)
    // 1 Minute
    if (tf1mInput)
        [column_1m, row_1m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_1m
        currentRow := row_1m
        [convictionText_1m, convictionCondition_1m, convictionBgColor_1m, convictionTextColor_1m] = getConviction(close, "1", convictionType)
        //[convictionBgColor_1m, convictionTextColor_1m] = getColorForConviction(convictionCondition_1m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "1m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_1m,bgcolor=convictionBgColor_1m,text_color=convictionTextColor_1m, text_size = textSize)
    // 2 Minute
    if (tf2mInput)
        [column_2m, row_2m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_2m
        currentRow := row_2m
        [convictionText_2m, convictionCondition_2m, convictionBgColor_2m, convictionTextColor_2m] = getConviction(close, "2", convictionType)
        //[convictionBgColor_2m, convictionTextColor_2m] = getColorForConviction(convictionCondition_2m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "2m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m, text_size = textSize)
    // 3 Minute
    if (tf3mInput)
        [column_3m, row_3m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_3m
        currentRow := row_3m
        [convictionText_3m, convictionCondition_3m, convictionBgColor_3m, convictionTextColor_3m] = getConviction(close, "3", convictionType)
        //[convictionBgColor_3m, convictionTextColor_3m] = getColorForConviction(convictionCondition_3m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "3m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_3m,bgcolor=convictionBgColor_3m, text_color=convictionTextColor_3m, text_size = textSize)
    // 4 Minute
    if (tf4mInput)
        [column_4m, row_4m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_4m
        currentRow := row_4m
        [convictionText_4m, convictionCondition_4m, convictionBgColor_4m, convictionTextColor_4m] = getConviction(close, "4", convictionType)
        //[convictionBgColor_4m, convictionTextColor_4m] = getColorForConviction(convictionCondition_4m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "4m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_4m,bgcolor=convictionBgColor_4m, text_color=convictionTextColor_4m, text_size = textSize)
    // 5 Minute
    if (tf5mInput)
        [column_5m, row_5m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_5m
        currentRow := row_5m
        [convictionText_5m, convictionCondition_5m, convictionBgColor_5m, convictionTextColor_5m] = getConviction(close, "5", convictionType)
        //[convictionBgColor_5m, convictionTextColor_5m] = getColorForConviction(convictionCondition_5m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "5m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_5m,bgcolor=convictionBgColor_5m, text_color=convictionTextColor_5m, text_size = textSize)
    // 7 Minute
    if (tf7mInput)
        [column_7m, row_7m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_7m
        currentRow := row_7m
        [convictionText_7m, convictionCondition_7m, convictionBgColor_7m, convictionTextColor_7m] = getConviction(close, "7", convictionType)
        //[convictionBgColor_7m, convictionTextColor_7m] = getColorForConviction(convictionCondition_7m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "7m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_7m,bgcolor=convictionBgColor_7m, text_color=convictionTextColor_7m, text_size = textSize)
    // 10 Minute
    if (tf10mInput)
        [column_10m, row_10m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_10m
        currentRow := row_10m
        [convictionText_10m, convictionCondition_10m, convictionBgColor_10m, convictionTextColor_10m] = getConviction(close, "10", convictionType)
        //[convictionBgColor_10m, convictionTextColor_10m] = getColorForConviction(convictionCondition_10m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "10m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_10m,bgcolor=convictionBgColor_10m, text_color=convictionTextColor_10m, text_size = textSize)
    // 15 Minute
    if (tf15mInput)
        [column_15m, row_15m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_15m
        currentRow := row_15m
        [convictionText_15m, convictionCondition_15m, convictionBgColor_15m, convictionTextColor_15m] = getConviction(close, "15", convictionType)
        //[convictionBgColor_15m, convictionTextColor_15m] = getColorForConviction(convictionCondition_15m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "15m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_15m,bgcolor=convictionBgColor_15m, text_color=convictionTextColor_15m, text_size = textSize)
    // 20 Minute
    if (tf20mInput)
        [column_20m, row_20m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_20m
        currentRow := row_20m
        [convictionText_20m, convictionCondition_20m, convictionBgColor_20m, convictionTextColor_20m] = getConviction(close, "20", convictionType)
        //[convictionBgColor_20m, convictionTextColor_20m] = getColorForConviction(convictionCondition_20m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "20m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_20m,bgcolor=convictionBgColor_20m, text_color=convictionTextColor_20m, text_size = textSize)
    // 30 Minute
    if (tf30mInput)
        [column_30m, row_30m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_30m
        currentRow := row_30m
        [convictionText_30m, convictionCondition_30m, convictionBgColor_30m, convictionTextColor_30m] = getConviction(close, "30", convictionType)
        //[convictionBgColor_30m, convictionTextColor_30m] = getColorForConviction(convictionCondition_30m)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "30m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_30m,bgcolor=convictionBgColor_30m, text_color=convictionTextColor_30m, text_size = textSize)
    // 1 Hour
    if (tf1hInput)
        [column_1h, row_1h] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_1h
        currentRow := row_1h
        [convictionText_1h, convictionCondition_1h, convictionBgColor_1h, convictionTextColor_1h] = getConviction(close, "60", convictionType)
        //[convictionBgColor_1h, convictionTextColor_1h] = getColorForConviction(convictionCondition_1h)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "1hr",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_1h,bgcolor=convictionBgColor_1h, text_color=convictionTextColor_1h, text_size = textSize)


// Ripster 5-12
// Declare variables once
currentColumn := 0
currentRow := 0
maxColumn := na
maxRow := na

// Direct calls to add data to the table, corresponding to each timeframe
currentColumn := orientationInput == 'Horizontal' ? 1 : 2 // Start at row 1 for Horizontal (for labels), row 0 for Vertical (for data)
currentRow := orientationInput == 'Horizontal' ? 2 : 1 // Start at row 0 for Horizontal (for labels), row 1 for Vertical (for data)
// Initialize maxColumn and maxRow based on orientation
maxColumn := orientationInput == 'Horizontal' ? array.size(timeframes) + 1 : 4
maxRow := orientationInput == 'Vertical' ? array.size(timeframes) + 1 : 4

if (show05_12Input)
    //Conditionally Define Conviction Type
    convictionType = show13_48Input ? "Saty(13-48)" : show05_12Input ? "Ripster(05-12)" : "Ripster(34-50)"
    // 30 Second
    if (tf30sInput)
        [column_30s, row_30s] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_30s
        currentRow := row_30s
        [convictionText_30s, convictionCondition_30s, convictionBgColor_30s, convictionTextColor_30s] = getConviction(close, "30S", convictionType)
        //[convictionBgColor_30s, convictionTextColor_30s] = getColorForConviction(convictionCondition_30s)
        //table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "30s",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 2: currentRow,convictionText_30s,bgcolor=convictionBgColor_30s, text_color=convictionTextColor_30s, text_size = textSize)
    // 1 Minute
    if (tf1mInput)
        [column_1m, row_1m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_1m
        currentRow := row_1m
        [convictionText_1m, convictionCondition_1m, convictionBgColor_1m, convictionTextColor_1m] = getConviction(close, "1", convictionType)
        //[convictionBgColor_1m, convictionTextColor_1m] = getColorForConviction(convictionCondition_1m)
        //table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "1m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 2: currentRow,convictionText_1m,bgcolor=convictionBgColor_1m,text_color=convictionTextColor_1m, text_size = textSize)
    // 2 Minute
    if (tf2mInput)
        [column_2m, row_2m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_2m
        currentRow := row_2m
        [convictionText_2m, convictionCondition_2m, convictionBgColor_2m, convictionTextColor_2m] = getConviction(close, "2", convictionType)
        //[convictionBgColor_2m, convictionTextColor_2m] = getColorForConviction(convictionCondition_2m)
        //table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "2m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 2: currentRow,convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m, text_size = textSize)
    // 3 Minute


// Ripster 34-50
// Declare variables once
currentColumn := 0
currentRow := 0
maxColumn := na
maxRow := na

// Direct calls to add data to the table, corresponding to each timeframe
currentColumn := orientationInput == 'Horizontal' ? 1 : 2 // Start at row 1 for Horizontal (for labels), row 0 for Vertical (for data)
currentRow := orientationInput == 'Horizontal' ? 3 : 1 // Start at row 0 for Horizontal (for labels), row 1 for Vertical (for data)
// Initialize maxColumn and maxRow based on orientation
maxColumn := orientationInput == 'Horizontal' ? array.size(timeframes) + 1 : 4
maxRow := orientationInput == 'Vertical' ? array.size(timeframes) + 1 : 4

if (show34_50Input)
    //Conditionally Define Conviction Type
    convictionType = show13_48Input ? "Saty(13-48)" : show05_12Input ? "Ripster(05-12)" : "Ripster(34-50)"
    // 30 Second
    if (tf30sInput)
        [column_30s, row_30s] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_30s
        currentRow := row_30s
        [convictionText_30s, convictionCondition_30s, convictionBgColor_30s, convictionTextColor_30s] = getConviction(close, "30S", convictionType)
        //[convictionBgColor_30s, convictionTextColor_30s] = getColorForConviction(convictionCondition_30s)
        //table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "30s",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 3: currentRow,convictionText_30s,bgcolor=convictionBgColor_30s, text_color=convictionTextColor_30s, text_size = textSize)
    // 1 Minute
    if (tf1mInput)
        [column_1m, row_1m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_1m
        currentRow := row_1m
        [convictionText_1m, convictionCondition_1m, convictionBgColor_1m, convictionTextColor_1m] = getConviction(close, "1", convictionType)
        //[convictionBgColor_1m, convictionTextColor_1m] = getColorForConviction(convictionCondition_1m)
        //table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "1m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 3: currentRow,convictionText_1m,bgcolor=convictionBgColor_1m,text_color=convictionTextColor_1m, text_size = textSize)
    // 2 Minute
    if (tf2mInput)
        [column_2m, row_2m] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
        currentColumn := column_2m
        currentRow := row_2m
        [convictionText_2m, convictionCondition_2m, convictionBgColor_2m, convictionTextColor_2m] = getConviction(close, "2", convictionType)
        //[convictionBgColor_2m, convictionTextColor_2m] = getColorForConviction(convictionCondition_2m)
        //table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "2m",text_color=themeText, text_size = textSize)
        table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 3: currentRow,convictionText_2m, bgcolor=convictionBgColor_2m, text_color=convictionTextColor_2m, text_size = textSize)
    // 3 Minute
