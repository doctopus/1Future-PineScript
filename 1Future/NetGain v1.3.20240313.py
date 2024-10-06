// Shows Live Profit/Loss of Futures
// Copyleft OneFuture
// V1.4.20240628

//@version=5
indicator("1Future: Net Gain", overlay=true)

// Input parameters
selected_option = input.string("NIFTY", "Trading Future:", options=["NIFTY", "ES", "ETH", "Stock"], inline = "Trade")
isLong = input.string("Long", title="Position:", options=["Long", "Short"],inline = "Trade")

entry_price1 = input.float(defval = 0.0, title = "Entry:", inline = "Price")
entry_price2 = input.float(defval = 0.0, title = "", inline = "Price")
entry_price3 = input.float(defval = 0.0, title = "", inline = "Price")
entry_price4 = input.float(defval = 0.0, title = "", inline = "Price")

gainLogo = input.string(defval = "😎 ", title = "Gain Style:", group="Style", inline = "Logo")
gainLineColor = input.color(color.new(color.green, 0), title="", group="Style", inline = "Logo")
lossLogo = input.string(defval = "😡 ", title = "Loss Style:", group="Style", inline = "Logo")
lossLineColor = input.color(color.new(color.red, 0), title="", group="Style", inline = "Logo")

labelSizeOption = input.string("Normal", title="Size", options=["Tiny", "Small", "Normal", "Large", "Huge"], group="Style", inline = "Line")
lineWidth = input.int(defval = 2, title="Thickness", minval=1, group="Style", inline = "Line")
bars_behind_current = input(0, title="Extension", group="Style", inline = "Line")

// Initialize entry_price and num_sets variables
float sum_sets = 0.0
int num_sets = 0

// Calculate num_sets
if entry_price1 != 0
    num_sets := num_sets + 1
    sum_sets := sum_sets + entry_price1
if entry_price2 != 0
    num_sets := num_sets + 1
    sum_sets := sum_sets + entry_price2
if entry_price3 != 0
    num_sets := num_sets + 1
    sum_sets := sum_sets + entry_price3
if entry_price4 != 0
    num_sets := num_sets + 1
    sum_sets := sum_sets + entry_price4

// Calculate average entry_price
float entry_price = na
if (num_sets > 0)
    entry_price := sum_sets / num_sets

// Fixed Settings
curSymbol = selected_option == "NIFTY" ? "₹ " : "$ "
qty_per_set_ES = 5
fee_ES = 5.24

qty_per_set_NIFTY = 25
fee_NIFTY = 120.36

qty_per_set_ETH = 0.1
fee_ETH = 0.2

qty_per_set_Stock = 1.0
fee_Stock = 0.0

qty_per_set = selected_option == "NIFTY" ? qty_per_set_NIFTY :
              selected_option == "ES" ? qty_per_set_ES :
              selected_option == "ETH" ? qty_per_set_ETH :
              qty_per_set_Stock

fee = selected_option == "NIFTY" ? fee_NIFTY :
      selected_option == "ES" ? fee_ES :
      selected_option == "ETH" ? fee_ETH :
      fee_Stock

// Map Selected Label Size to Predefined Sizes
labelSize = labelSizeOption == "Tiny" ? size.tiny :
             labelSizeOption == "Small" ? size.small :
             labelSizeOption == "Normal" ? size.normal :
             labelSizeOption == "Large" ? size.large :
             labelSizeOption == "Huge" ? size.huge :
             na
// Functions to Calculate Profit/Loss
calculate_profit_loss(qty_per_set, entry_price, current_price, fee, isLong) =>
    net_profit_loss = isLong == "Long" ? ((current_price - entry_price) * qty_per_set * num_sets) - (num_sets * fee) : ((entry_price - current_price) * qty_per_set * num_sets) - (num_sets * fee)
    net_profit_loss

format_profit_loss(value) =>
    rounded_value = math.round(value, 2)
    sign = rounded_value >= 0 ? "+" : "-"
    abs_value = math.abs(rounded_value)
    formatted_value = str.tostring(abs_value, "#.00")
    sign + curSymbol + formatted_value

current_profit_loss = calculate_profit_loss(qty_per_set, entry_price, close, fee, isLong)

var line BuyPriceLine = na
var label NetGainLabel = na

// Update or create the horizontal line and label
if barstate.islast
    line.delete(BuyPriceLine)
    label.delete(NetGainLabel)

    // Calculate the x1 position for the horizontal line
    x1_position = bars_behind_current > 0 ? (bar_index - bars_behind_current) : na

    // Draw horizontal line at Buy Price with conditional color
    BuyPriceLine := line.new(
         x1=x1_position,
         y1=entry_price,
         x2=bar_index+1,
         y2=entry_price,
         width=current_profit_loss > 0 ? lineWidth : 0,
         color=current_profit_loss > 0 ? gainLineColor : lossLineColor,
         extend=extend.right)

    // Display Net Gain/Loss value as a box on the right edge of the chart near the axis
    label_text = current_profit_loss > 0 ? gainLogo + format_profit_loss(current_profit_loss) : lossLogo + format_profit_loss(current_profit_loss)
    NetGainLabel := label.new(
         x=bar_index+10,
         y=entry_price,
         text=label_text,
         xloc=xloc.bar_index,
         yloc=yloc.price,
         style=label.style_label_left,
         color=current_profit_loss > 0 ? color.new(#09aa00, 10) : color.new(#ffffff, 5),
         textcolor=current_profit_loss > 0 ? color.new(#ffffff, 0):color.new(#fb1b0b, 0),
         size=labelSize)
