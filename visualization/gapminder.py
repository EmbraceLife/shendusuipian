# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")
import pandas as pd
my_dpi=720

# Get the data (csv file is hosted on the web)
url = 'https://python-graph-gallery.com/wp-content/uploads/gapminderData.csv'
data = pd.read_csv(url)
data.to_csv("gapminder.csv")

# And I need to transform my categorical column (continent) in a numerical value group1->1, group2->2...
data['continent']=pd.Categorical(data['continent'])

# For each year:
for i in data.year.unique():

# initialize a figure
    fig = plt.figure(figsize=(8,6), dpi=720)

    # Change color with c and alpha. I map the color to the X axis value.
    tmp=data[ data.year == i ] # get data for each year

    plt.scatter(tmp['lifeExp'], tmp['gdpPercap'] , s=tmp['pop']/200000 , c=tmp['continent'].cat.codes, cmap="Accent", alpha=0.6, edgecolors="white", linewidth=2)

    # Add titles (main and on axis)
    plt.yscale('log')
    plt.xlabel("Life Expectancy")
    plt.ylabel("GDP per Capita")
    plt.title("Year: "+str(i) )
    plt.ylim(0,100000)
    plt.xlim(30, 90)

    # Save it
    filename='Gapminder_step'+str(i)+'.png'
    plt.savefig(filename, dpi=720)
    plt.gca()

# convert -delay 80 Gapminder*.png animated_gapminder.gif
