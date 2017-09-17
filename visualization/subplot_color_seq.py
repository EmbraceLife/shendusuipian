import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


################################################################
# prepare color sequence data for coloring a curve

## color data
color_data = y_pred

## line data
target_closes = closes/closes[0]
line_data = target_closes.reshape((-1,1))-1

## create color
def uniqueish_color(color_data):
    """There're better ways to generate unique colors, but this isn't awful."""
    # return plt.cm.gist_ncar(color_data)
    # return plt.cm.binary(color_data)
    return plt.cm.bwr(color_data)

## line_data X, and line_data y
X = np.arange(len(line_data)).reshape((-1,1))
y = line_data
xy = np.concatenate((X,y), axis=1)


# set up plotting
plt.figure()

# on figure, 14 rows and 3 columns in total
# set up for subplot 1, span 3 columns, span 4 rows
ax1 = plt.subplot2grid((14, 3), (0, 0), colspan=3, rowspan=4)

# plot predictions(pct) as color into prices
for start, stop, col in zip(xy[:-1], xy[1:], color_data):
    x, y = zip(start, stop)
    ax1.plot(x, y, color=uniqueish_color(col))

################################################################ belong above


# plot another curve
ax1.plot(accum_profit, c='gray', alpha=0.5, label='accum_profit')
ax1.legend(loc='best')
ax1.set_title('RB from %s to %s return: %04f' % (date[0], date[-1], accum_profit[-1]))

# setup for subplot2
ax2 = plt.subplot2grid((14, 3), (4, 0), colspan=3, rowspan=2)

# plot histogram: color, alpha, label, bins
ax2.hist(y_pred_hist, color='red', alpha = 0.5, label='pred')
ax2.hist(y_target_hist, color='blue', alpha = 0.2, label='target')

# subplot: legend, title
ax2.legend(loc='best')
ax2.set_title("y_pred_target frequencies")


# plot bars in subplot
ax4 = plt.subplot2grid((14, 3), (8, 0), colspan=3, rowspan=2)
X = np.arange(len(close_trades_positions))
ax4.bar(X, open_trades_positions, facecolor='gray', edgecolor='gray')
ax4.bar(X, close_trades_positions, facecolor='pink', edgecolor='pink')

ax4.set_title('open position (gray), close position(pink), %d winning trades, %d trades in total' % (winning_trades_sum, num_full_trades)) # change model name


plt.tight_layout()
plt.show()



# plt.savefig("/Users/Natsume/Downloads/data_for_all/stocks/model_performance/ETF300_model4_addcost.png")
