<a name="___top"></a>
<div align="center">
<link rel="icon" href="http://pinecoders.com/favicon.ico?v=2" />

![logo](images/PineScript.png "PineCoders")
</div>

[](1}}})
<a name="Official_Resources"></a> []({{{1)
# [Official Resources &#9650;](#___top "click to go to top of document")

- [Pine Script v5 User Manual](https://www.tradingview.com/pine-script-docs/en/v5/index.html) - *Official Documentation on Pine Script Version 5.*
- [Pine Script Chat Room](https://www.tradingview.com/chat/#BfmVowG1TZkKO235) - *TradingView public chat dedicated to Pine Script where active developers of the community help each other out.*
- [TV Blog](https://www.tradingview.com/blog/en/category/market-analysis/pine/) - *Information about major releases and modifications to Pine Script (as well as other features.)*
- [TV Public Scripts](https://www.tradingview.com/scripts/) - *TradingView’s Public Library contains all user-published scripts.*
- [Editors Picks](https://www.tradingview.com/scripts/editors-picks/) - *TV's curated list of best indicators*

<div align="left">

[](1}}})
<a name="Pinescript_Resources"></a> []({{{1)
# [PineScript Resources &#9650;](#___top "click to go to top of document")

<font size="+1"><strong>New to <a href="https://www.tradingview.com/u/?solution=43000561836">Pine Script™</a>?</strong></font><br>
Begin your journey with Pinecoders: <a href="http://www.pinecoders.com/learning_pine_roadmap">Learning Pine Script™ Roadmap</a>.<br><br>

<font size="+1"><strong>Stay Up to Date on Pine Script™</strong></font><br>

Reddit: <a href="https://www.reddit.com/r/TradingView/">TradingView's subreddit</a>.<br><br>
</div>

<pre>
//@version=5
//@strategy_alert_message {{strategy.order.action}} {{strategy.position_size}} {{ticker}} @ {{strategy.order.price}}

strategy("1Future -StrategyName", overlay=true)
</pre>


<a name="Pinescript"></a> 
[]({{{1)
## Calculate EMA
```shell
// Calculate EMAs
//fast_conv_ema = ta.ema(close, fast_conv_ema_length)
```

## Show Label Text
```shell
label_text = current_profit_loss > 0 ? "😎" + format_profit_loss(current_profit_loss) : "😡" + format_profit_loss(current_profit_loss)
```

## Plot Arrows
```// Plot arrows
plotshape(bullish_conviction_confirmed,
    style=shape.triangleup,
    color=#3afc3399, 
    location=location.belowbar, 
    size=size.small, text=""
)
```
**Note**: Follow the official Documentation for examples.
[](1}}})

---
[](1}}})
<a name="Other_Resources"></a> []({{{1)
# [Other Resources &#9650;](#___top "click to go to top of document")
[Pine Script™ Reference Manual](https://www.tradingview.com/pine-script-reference/v5/)  
[Pine Script™ User Manual](https://www.tradingview.com/pine-script-docs/en/v5/)

