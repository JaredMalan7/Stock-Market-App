import pandas as pd

def analyze_stock_data(df: pd.DataFrame):
    """
    Perform basic analysis on stock data.
    Returns a dictionary with:
    - Average closing price
    - Highest closing price
    - Volatility (standard deviation)
    - Longest streak of positive daily performance
    """

    if df.empty:
        return "No data available to analyze."

    # Average closing price
    average_close = df['Close'].mean()
    # Highest closing price in the date range
    highest_close = df['Close'].max()
    # Volatility (how much the stock moves up/down on average)
    volatility = df['Close'].std()
    # Calculate longest streak of days where the stock closed higher
    longest_streak = find_longest_positive_streak(df)

    # New insight: Day with highest trading volume
    highest_volume_day = df['Volume'].idxmax()
    highest_volume_value = df['Volume'].max()

    return {
        "average_close": round(average_close, 2),
        "highest_close": round(highest_close, 2),
        "volatility": round(volatility, 2),
        "longest_positive_streak": longest_streak,
        "highest_volume_day": highest_volume_day.strftime("%Y-%m-%d"),
        "highest_volume_value": int(highest_volume_value)
    }

def find_longest_positive_streak(df: pd.DataFrame) -> int:
    """
    Finds the longest consecutive streak of days
    where the stock closed higher than it opened.
    """
    streak = 0
    max_streak = 0

    for _, row in df.iterrows():
        if row["Close"] > row["Open"]:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0



    return max_streak