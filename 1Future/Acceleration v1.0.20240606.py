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
tf6mInput = input.bool(true, title="6m", group = "Timeframes", inline = "TFL")
tf7mInput = input.bool(true, title="7m", group = "Timeframes", inline = "TFL")
tf8mInput = input.bool(false, title="8m", group = "Timeframes", inline = "TFH")
tf9mInput = input.bool(false, title="9m", group = "Timeframes", inline = "TFH")
tf10mInput = input.bool(false, title="10m", group = "Timeframes", inline = "TFH")

bullishTextInput = input.string(defval = "▲", title = "Bullish Sign:", group = "Design", inline = "Text")
bearishTextInput = input.string(defval = "▼", title = "Bearish Sign:", group = "Design", inline = "Text")
bullishColorInput = input.color(color.green, title="Bull Conviction Color:", group = "Design", inline = "Colour")
bearishColorInput = input.color(color.red, title="Bear Conviction Color:", group = "Design", inline = "Colour")
