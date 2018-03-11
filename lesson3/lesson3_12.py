"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

        # Rename to prevent clash of column names
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df = df.join(df_temp, how='inner') # this how='inner' will join the intersection between tables, thus removing NaN values

    return df

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """ Plot the stock price """
    ax = df.plot(title=title, fontsize=8)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.grid() # display the grid line
    plt.show() # display the plot

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data, with ix slicing for more refined data
    df = get_data(symbols, dates)
    print(df.ix['2010-02-01' : '2010-03-01', ['IBM', 'GLD']])
    plot_data(df)

if __name__ == "__main__":
    test_run()
