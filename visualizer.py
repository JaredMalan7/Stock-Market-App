import os
import matplotlib.pyplot as plt
import pandas as pd

def plot_closing_prices(df: pd.DataFrame, ticker: str, folder: str = "results"):
    """
    Plots the daily closing prices along with a 7-day moving average for the given stock ticker.
    Saves the plot as a PNG file in the specified folder.

    Parameters:
    - df (pd.DataFrame): DataFrame containing stock data.
    - ticker (str): Stock ticker symbol.
    - folder (str): Directory to save the generated plot (default is "results").
    """
    # Calculate 7-day moving average and add it as a new column
    df["7-day MA"] = df["Close"].rolling(window=7).mean()

    # Creates a line plot of closing price and moving average
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], label="Closing Price", color='blue')
    plt.plot(df.index, df["7-day MA"], label="7-Day MA", color='orange', linestyle="--")
    plt.title(f"{ticker} Daily Closing Prices with 7-Day MA")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Ensure the results folder exists
    os.makedirs(folder, exist_ok=True)

    # Save the figure to the folder
    plt.savefig(os.path.join(folder, f"{ticker}_daily_closing_prices_with_ma.png"))
    plt.close()


def plot_monthly_avg_close(df: pd.DataFrame, ticker: str, folder: str = "results"):
    """
    Plots the average closing price for each month using a bar chart.
    Saves the chart as a PNG file in the specified folder.

    Parameters:
    - df (pd.DataFrame): DataFrame containing stock data.
    - ticker (str): Stock ticker symbol.
    - folder (str): Directory to save the generated plot (default is "results").
    """
    # Resample to monthly frequency and compute mean closing price
    monthly_avg = df["Close"].resample("ME").mean()

    # Create a bar plot of monthly average close prices
    plt.figure(figsize=(10, 5))
    monthly_avg.plot(kind="bar", color='green')
    plt.title(f"{ticker} Monthly Average Closing Prices")
    plt.xlabel("Month")
    plt.ylabel("Average Close Price ($)")
    plt.tight_layout()

    # Ensure the results folder exists
    os.makedirs(folder, exist_ok=True)

    # Save the plot to the folder
    plt.savefig(os.path.join(folder, f"{ticker}_monthly_avg_close.png"))
    plt.close()