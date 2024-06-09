// © Oneome

//@version=5
indicator("1Future: Acceleration", overlay=true)

// User inputs
themeInput = input.string(defval = "Dark", title = "Theme:", options = ["Dark", "Light"], inline = "Global")
sizeInput = input.string(defval = "Auto", title = "Widget Size:", options = ["Auto", "Tiny", "Small", "Normal", "Large"], inline = "Global")
tablePositionInput = input.string("Top-Right", title="Position:", options=["Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right", "Middle-Left", "Middle-Right"], inline = "Table")
orientationInput = input.string(defval = 'Horizontal', title = 'Orientation:', options = ['Horizontal', 'Vertical'], inline = "Table")

show05_12Input = input.bool(defval = true, title = "Ripster(05-12)", inline = "Convictions")
show13_48Input = input.bool(defval = true, title = "Saty(13-48)", inline = "Convictions")
show34_50Input = input.bool(defval = true, title = "Ripster(34-50)", inline = "Convictions")

tf15sInput = input.bool(true, title="15s", group = "Timeframes", inline = "TFL")
tf30sInput = input.bool(true, title="30s", group = "Timeframes", inline = "TFL")
tf1mInput = input.bool(true, title="1m", group = "Timeframes", inline = "TFL")
tf2mInput = input.bool(true, title="2m", group = "Timeframes", inline = "TFL")
tf3mInput = input.bool(true, title="3m", group = "Timeframes", inline = "TFL")
tf4mInput = input.bool(true, title="4m", group = "Timeframes", inline = "TFL")
tf5mInput = input.bool(true, title="5m", group = "Timeframes", inline = "TFL")

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
//}
// Initialize an array for timeframes
var string[] convictions = array.new_string()
if (array.size(convictions) == 0)
    if (show05_12Input)
        array.push(convictions, "Ripster(05-12)")
    if (show13_48Input)
        array.push(convictions, "Saty(13-48)")
    if (show34_50Input)
        array.push(convictions, "Ripster(34-50)")
//}

// Initialize an array for timeframes for short names
var string[] convictions_short = array.new_string()
if (array.size(convictions_short) == 0)
    if (show05_12Input)
        array.push(convictions_short, "05")
    if (show13_48Input)
        array.push(convictions_short, "13")
    if (show34_50Input)
        array.push(convictions_short, "34")
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
    // Return all calculated values
    [convictionText, convictionCondition, convictionBgColor, convictionTextColor]
//


// Set Theme Text and Background Color
var themeText = color.red
var themeBg = color.blue
themeText := themeInput == "Dark" ? color.white : color.black
themeBg := themeInput == "Dark" ? color.new(color.black, 30) : color.new(color.white, 30)

// 15 Second
//if (tf15sInput)

//    [column_15s, row_15s] = calculateIndices(orientationInput, currentColumn, currentRow, maxColumn, maxRow)
//    currentColumn := column_15s
//    currentRow := row_15s
//    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 0,orientationInput == 'Horizontal' ? 0: currentRow, "15s",text_color=themeText, text_size = textSize)
//
//    convictionType := "Ripster(05-12)"
//    [convictionText_15s, convictionCondition_15s, convictionBgColor_15s, convictionTextColor_15s] = getConviction(close, "15S", convictionType)
//    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 1,orientationInput == 'Horizontal' ? 1: currentRow,convictionText_15s,bgcolor=convictionBgColor_15s, text_color=convictionTextColor_15s, text_size = textSize)
//    convictionType := "Saty(13-48)"
//    [convictionText_15s2, convictionCondition_15s2, convictionBgColor_15s2, convictionTextColor_15s2] = getConviction(close, "15S", convictionType)
//    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 2,orientationInput == 'Horizontal' ? 2: currentRow, convictionText_15s2,bgcolor=convictionBgColor_15s2, text_color=convictionTextColor_15s2, text_size = textSize)
//    convictionType := "Ripster(34-50)"
//    [convictionText_15s3, convictionCondition_15s3, convictionBgColor_15s3, convictionTextColor_15s3] = getConviction(close, "15S", convictionType)
//    table.cell(infoTable,orientationInput == 'Horizontal' ? currentColumn : 3,orientationInput == 'Horizontal' ? 3: currentRow,convictionText_15s3,bgcolor=convictionBgColor_15s3, text_color=convictionTextColor_15s3, text_size = textSize)

l = line.new(bar_index, high, bar_index[10], high, width = 2)
line.delete(l[1])
