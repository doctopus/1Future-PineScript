//@version=5
indicator("1F - ConvictionBar", overlay=true)

// User inputs
rsiLengthInput = input.int(14, minval=1, title="RSI Length")
maLengthInput = input.int(14, title="MA Length")
showTableInput = input.bool(true, title="Show RSI & MA Table")
tablePositionInput = input.string("Bottom left", title="Table Position", options=["Top left", "Top right", "Bottom left", "Bottom right", "Middle left", "Middle right"])
maTypeInput = input.string("SMA", title="MA Type", options=["SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="MA Settings")
rsiSourceInput = input.source(close, "Source", group="RSI Settings")

// Function for MA calculation based on type
ma(source, length, type) =>
    switch type
        "SMA" => ta.sma(source, length)
        "Bollinger Bands" => ta.sma(source, length) // Simplified representation for the example
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

// Function to calculate Conviction based on fast and slow EMA
getConviction(src, tf) =>
    fastEma = request.security(syminfo.tickerid, tf, ta.ema(src, 13))
    slowEma = request.security(syminfo.tickerid, tf, ta.ema(src, 48))
    conviction = fastEma > slowEma ? "↑😎" : fastEma < slowEma ? "↓😡" : "→😑"
    conviction

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

// Initialize the InfoTable with an additional column for Conviction
var table infoTable = table.new(tablePosition, 6, 9, bgcolor = color.rgb(0, 0, 0), border_width = 1)
table.cell(infoTable, 0, 0, "TF", text_color = color.white)
table.cell(infoTable, 1, 0, "RSI", text_color = color.white)
table.cell(infoTable, 2, 0, "MA", text_color = color.white)
table.cell(infoTable, 3, 0, "Trend", text_color = color.white)
table.cell(infoTable, 4, 0, "Sentiment", text_color = color.white)
table.cell(infoTable, 5, 0, "Conviction", text_color = color.white) // Adding Conviction Column Header

// Dummy function for trend and sentiment color (implement your own logic)
getColorForTrendAndSentiment(trend, sentiment) =>
    trend == "Rising" and sentiment == "Bullish" ? color.green : trend == "Falling" and sentiment == "Bearish" ? color.red : color.gray

// Function to Add a Row to the Table
addTableRow(row, timeframe, rsi, ma, trend, sentiment, conviction) =>
    trendColor = getColorForTrendAndSentiment(trend, sentiment)

    var color rsiColor = color.new(color.white, 0) // Default color for RSI
    if rsi <= 30
        rsiColor := color.new(color.red, 0)
    else if rsi >= 70
        rsiColor := color.new(color.green, 0)

    table.cell(infoTable, 0, row, timeframe, bgcolor=rsiColor, text_color=color.white)
    table.cell(infoTable, 1, row, str.format("{0,number,#.#}", rsi), text_color=color.white)
    table.cell(infoTable, 2, row, str.format("{0,number,#.#}", ma), text_color=color.white)
    table.cell(infoTable, 3, row, trend, bgcolor=trendColor, text_color = color.white)
    table.cell(infoTable, 4, row, sentiment, bgcolor=trendColor, text_color = color.white)
    table.cell(infoTable, 5, row, conviction, text_color=color.white) // New Conviction cell


// Adding Data to the Table
if showTableInput
    // Example for "1m" timeframe. Repeat for other timeframes...
    rsi_1m = ta.rsi(rsiSourceInput, rsiLengthInput)
    ma_1m = ma(rsiSourceInput, maLengthInput, maTypeInput)
    conviction_1m = getConviction(rsiSourceInput, "1")
    // Assume trend and sentiment calculation logic is implemented
    trend_1m = "Rising" // Placeholder
    sentiment_1m = "Bullish" // Placeholder
    addTableRow(1, "1m", rsi_1m, ma_1m, trend_1m, sentiment_1m, conviction_1m)

  // Example for "1m" timeframe. Repeat for other timeframes...
    rsi_2m = ta.rsi(rsiSourceInput, rsiLengthInput)
    ma_2m = ma(rsiSourceInput, maLengthInput, maTypeInput)
    conviction_2m = getConviction(rsiSourceInput, "2")
    // Assume trend and sentiment calculation logic is implemented
    trend_2m = "Rising" // Placeholder
    sentiment_2m = "Bullish" // Placeholder
    addTableRow(2, "2m", rsi_2m, ma_2m, trend_2m, sentiment_2m, conviction_2m)

  // Example for "1m" timeframe. Repeat for other timeframes...
    rsi_3m = ta.rsi(rsiSourceInput, rsiLengthInput)
    ma_3m = ma(rsiSourceInput, maLengthInput, maTypeInput)
    conviction_3m = getConviction(rsiSourceInput, "3")
    // Assume trend and sentiment calculation logic is implemented
    trend_3m = "Rising" // Placeholder
    sentiment_3m = "Bullish" // Placeholder
    addTableRow(3, "3m", rsi_3m, ma_3m, trend_3m, sentiment_3m, conviction_3m)

  // Example for "1m" timeframe. Repeat for other timeframes...
    rsi_5m = ta.rsi(rsiSourceInput, rsiLengthInput)
    ma_5m = ma(rsiSourceInput, maLengthInput, maTypeInput)
    conviction_5m = getConviction(rsiSourceInput, "5")
    // Assume trend and sentiment calculation logic is implemented
    trend_5m = "Rising" // Placeholder
    sentiment_5m = "Bullish" // Placeholder
    addTableRow(4, "5m", rsi_5m, ma_5m, trend_5m, sentiment_5m, conviction_5m)

  // Example for "1m" timeframe. Repeat for other timeframes...
    rsi_15m = ta.rsi(rsiSourceInput, rsiLengthInput)
    ma_15m = ma(rsiSourceInput, maLengthInput, maTypeInput)
    conviction_15m = getConviction(rsiSourceInput, "15")
    // Assume trend and sentiment calculation logic is implemented
    trend_15m = "Rising" // Placeholder
    sentiment_15m = "Bullish" // Placeholder
    addTableRow(5, "15m", rsi_15m, ma_15m, trend_15m, sentiment_15m, conviction_15m)

  // Example for "1m" timeframe. Repeat for other timeframes...
    rsi_1h = ta.rsi(rsiSourceInput, rsiLengthInput)
    ma_1h = ma(rsiSourceInput, maLengthInput, maTypeInput)
    conviction_1h = getConviction(rsiSourceInput, "60")
    // Assume trend and sentiment calculation logic is implemented
    trend_1h = "Rising" // Placeholder
    sentiment_1h = "Bullish" // Placeholder
    addTableRow(6, "1h", rsi_1h, ma_1h, trend_1h, sentiment_1h, conviction_1h)
    // Ensure to calculate RSI, MA, trend, sentiment, and conviction for each and pass to addTableRow
// }