import yfinance as yf
import pandas as pd
from fetcher import fetch_stock_data
from analyzer import analyze_stock_data
from visualizer import plot_closing_prices, plot_monthly_avg_close
from config import DEFAULT_TICKER, DEFAULT_START_DATE, DEFAULT_END_DATE
from exporter import export_results_to_file

# Force pandas to show all rows and columns in the terminal output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def main():
    # Prompt the user for stock ticker and date range (use default if left empty)
    ticker = input(f"Enter stock ticker (default: {DEFAULT_TICKER}): ") or DEFAULT_TICKER
    start_date = input(f"Enter start date YYYY-MM-DD (default: {DEFAULT_START_DATE}): ") or DEFAULT_START_DATE
    end_date = input(f"Enter end date YYYY-MM-DD (default: {DEFAULT_END_DATE}): ") or DEFAULT_END_DATE

    try:
        # Fetch historical stock data
        data = fetch_stock_data(ticker, start_date, end_date)
        if data.empty:
            print("No data found for the given inputs.")
            return

        # Display the first few rows of data
        print("\n Preview of Data:")
        print(data)

        # Run analysis on the data
        results = analyze_stock_data(data)
        print("\nAnalysis Results:")
        for key, value in results.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")

        # Generate visualizations (charts)
        plot_closing_prices(data, ticker)
        plot_monthly_avg_close(data, ticker)

        # Ask to export results
        save = input("\nWould you like to save the results to a file? (y/n): ").lower()
        if save == "y":
            export_results_to_file(results, ticker)

    except Exception as e:
        # Handle errors gracefully
        print(f"\n Error: {e}")
        print("Please check your input and try again.")

if __name__ == "__main__":
    main()