import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load the medical examination dataset
df = pd.read_csv('medical_examination.csv')

# Calculate overweight column
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalize cholesterol and gluc values
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Function to draw the categorical plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Create the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    fig.savefig('catplot.png')
    return fig

# Function to draw the heatmap
def draw_heat_map():
    # Filter the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Draw the heatmap
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, square=True, cbar_kws={'shrink': 0.5}, ax=ax)

    # Save the figure
    fig.savefig('heatmap.png')
    return fig

# Scatter plot with regression lines
def draw_plot():
    # Load the sea level data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best Fit Line 1')

    # Create second line of best fit using data from year 2000
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, intercept2 + slope2 * years_extended, 'green', label='Best Fit Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing
    plt.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gca()
