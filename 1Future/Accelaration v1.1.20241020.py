//@version=5
strategy("1Future-Acceleration", overlay=true)

// Input for EMA periods
fastEmaPeriod = input.int(13, title="Fast EMA Period")
slowEmaPeriod = input.int(48, title="Slow EMA Period")

// Function to calculate trend for a given timeframe
getTrend(tf) =>
    fastEma = request.security(syminfo.tickerid, tf, ta.ema(close, fastEmaPeriod))
    slowEma = request.security(syminfo.tickerid, tf, ta.ema(close, slowEmaPeriod))
    fastEma >= slowEma ? 1 : -1

// Calculate trends for each timeframe
trend1m = getTrend("1")
trend2m = getTrend("2")
trend3m = getTrend("3")
trend4m = getTrend("4")
trend5m = getTrend("5")
trend6m = getTrend("6")
trend7m = getTrend("7")
trend8m = getTrend("8")
trend9m = getTrend("9")
trend10m = getTrend("10")

// Function to get trend for a specific index
getTrendByIndex(index) =>
    if index == 0
        trend1m
    else if index == 1
        trend2m
    else if index == 2
        trend3m
    else if index == 3
        trend4m
    else if index == 4
        trend5m
    else if index == 5
        trend6m
    else if index == 6
        trend7m
    else if index == 7
        trend8m
    else if index == 8
        trend9m
    else if index == 9
        trend10m
    else
        0  // Default case, should never happen

// Variables to track acceleration
var float acceleration = 0.0
var int direction = 0
var int lastChangeBar = 0
var int highestAlignedTimeframe = 0
var int consistentTrendDuration = 0

// Function to calculate acceleration and direction
calculateAcceleration(int currentDirection) =>
    currentTrend = getTrendByIndex(0)  // 1-minute trend
    newDirection = currentDirection
    newAcceleration = acceleration
    newLastChangeBar = lastChangeBar
    newHighestAlignedTimeframe = highestAlignedTimeframe
    newConsistentTrendDuration = consistentTrendDuration

    if (currentTrend != currentDirection)
        // Trend has changed, reset acceleration
        newDirection := currentTrend
        newAcceleration := 0.0
        newLastChangeBar := bar_index
        newHighestAlignedTimeframe := 0
        newConsistentTrendDuration := 1
    else
        newConsistentTrendDuration := consistentTrendDuration + 1
        // Check how many higher timeframes align with the current trend
        for i = 1 to 9
            if (getTrendByIndex(i) == currentDirection)
                newHighestAlignedTimeframe := i
            else
                break

        // Calculate acceleration based on how quickly higher timeframes aligned and current trend duration
        timeTaken = bar_index - newLastChangeBar + 1
        alignmentFactor = (newHighestAlignedTimeframe + 1) / 10
        durationFactor = math.log(newConsistentTrendDuration) / math.log(1000)  // Logarithmic scaling
        newAcceleration := alignmentFactor * (1 - durationFactor)

    [newAcceleration, newDirection, newLastChangeBar, newHighestAlignedTimeframe, newConsistentTrendDuration]

// Calculate acceleration and direction
[newAcceleration, newDirection, newLastChangeBar, newHighestAlignedTimeframe, newConsistentTrendDuration] = calculateAcceleration(direction)
acceleration := newAcceleration
direction := newDirection
lastChangeBar := newLastChangeBar
highestAlignedTimeframe := newHighestAlignedTimeframe
consistentTrendDuration := newConsistentTrendDuration

// Colors for visual indicators
bullColor = color.new(color.green, 20)
bearColor = color.new(color.red, 20)

// Plotting acceleration as colored background
bgcolor(direction > 0 ? bullColor : bearColor, title="Acceleration Background")

// Plotting arrows to indicate direction and strength of acceleration
arrowLength = acceleration * 10  // Scale arrow length based on acceleration
plotarrow(direction > 0 ? arrowLength : 0, title="Bullish Arrow", colorup=color.green, maxheight=60, minheight=10)
plotarrow(direction < 0 ? -arrowLength : 0, title="Bearish Arrow", colordown=color.red, maxheight=60, minheight=10)

// Strategy logic
if (direction > 0 and direction[1] <= 0)
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit Long", "Long", stop=strategy.position_avg_price * 0.99, limit=strategy.position_avg_price * 1.02)

if (direction < 0 and direction[1] >= 0)
    strategy.entry("Short", strategy.short)
    strategy.exit("Exit Short", "Short", stop=strategy.position_avg_price * 1.01, limit=strategy.position_avg_price * 0.98)

// Display acceleration value and direction as labels
var label accelerationLabel = na
label.delete(accelerationLabel)
accelerationLabel := label.new(
  x=bar_index,
  y=high,
  text="Acceleration: " + str.tostring(acceleration, "#.##") + "\nDirection: " + (direction > 0 ? "Bullish" : "Bearish") + "\nDuration: " + str.tostring(consistentTrendDuration),
  color=direction > 0 ? color.green : color.red,
  textcolor=color.white,
  style=label.style_label_down,
  yloc=yloc.abovebar)