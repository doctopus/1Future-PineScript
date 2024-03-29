// Shows Live Profit/Loss of Futures
// Copyleft OnePro
// V1.0.20240122

//@version=5
indicator("1Future: Net Gain", overlay=true)

// Input parameters

// Future Settings -Individual
//qty_per_set = input.float(5, "Quantity per Set", minval=0, step=0.1, group="Future Settings")
//fee = input.float(5.24, "Fees for a Set", minval=0, step=0.1, group="Future Settings")
//Future Setting -Groups
qty_per_set_ES = 5
fee_ES = 5.24

qty_per_set_NIFTY = 50
fee_NIFTY = 260

qty_per_set_ETH = 0.1
fee_ETH = 0.2

selected_option = input.string("NIFTY", "Trading Future", options=["NIFTY", "ES", "ETH"])

qty_per_set = selected_option == "NIFTY" ? qty_per_set_NIFTY :
              selected_option == "ES" ? qty_per_set_ES :
              qty_per_set_ETH

fee = selected_option == "NIFTY" ? fee_NIFTY :
      selected_option == "ES" ? fee_ES :
      fee_ETH

entry_price = input(defval = 5000.00, title = "Entry Price")
num_sets = input.int(defval =1, title = "Traded Sets", minval =1  , maxval =100  , step =1)
isLong = input.string("Long", title="Position", options=["Long", "Short"])

// Style inputs for BuyPriceLine
labelSizeOption = input.string("Normal", title="Net Gain Label Size", options=["Tiny", "Small", "Normal", "Large", "Huge"], group="Style")
bars_behind_current = input(0, title="Line Length on Left", group="Style")

gainLineColor = input(color.new(color.green, 0), title="Gain Line Color", group="Style")
gainLineWidth = input.int(2, title="Gain Line Width", minval=1, group="Style")
lossLineColor = input(color.new(color.red, 0), title="Loss Line Color", group="Style")
lossLineWidth = input.int(2, title="Loss Line Width", minval=1, group="Style")

// Map Selected Label Size to Predefined Sizes
labelSize = labelSizeOption == "Tiny" ? size.tiny :
             labelSizeOption == "Small" ? size.small :
             labelSizeOption == "Normal" ? size.normal :
             labelSizeOption == "Large" ? size.large :
             labelSizeOption == "Huge" ? size.huge :
             na

calculate_profit_loss(qty_per_set, entry_price, current_price, fee, isLong) =>
    net_profit_loss = isLong == "Long" ? ((current_price - entry_price) * qty_per_set * num_sets) - (num_sets * fee) : ((entry_price - current_price) * qty_per_set * num_sets) - (num_sets * fee)
    net_profit_loss

format_profit_loss(value) =>
    rounded_value = math.round(value, 2)
    sign = rounded_value >= 0 ? "+" : "-"
    abs_value = math.abs(rounded_value)
    formatted_value = str.tostring(abs_value, "#.00")
    sign + formatted_value

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
         width=current_profit_loss > 0 ? gainLineWidth : lossLineWidth,
         color=current_profit_loss > 0 ? gainLineColor : lossLineColor,
         extend=extend.right)

    // Display Net Gain/Loss value as a box on the right edge of the chart near the axis
    label_text = current_profit_loss > 0 ? "😎" + format_profit_loss(current_profit_loss) : "😡" + format_profit_loss(current_profit_loss)
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
