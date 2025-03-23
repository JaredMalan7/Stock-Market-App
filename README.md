# 📈 Stock-Market-App


## Overview

Stock-Market-App is a data analysis tool built using **Python** and **Pandas**, powered by real-time financial data from **Yahoo Finance** via the `yfinance` API. It enables users to explore the performance of any public stock over a specific date range, view visual trends, and export findings.

Users can:
- Input a stock ticker and custom date range
- View statistics like average/maximum close and volatility
- Track streaks of positive gains and high-volume days
- Generate clean, exportable line and bar charts
- Save analysis results to a `.txt` file

---

## 🎥 YouTube Video Demo

---

## 🛠 Installation and Setup

### Requirements
- Python 3.x
- `yfinance`
- `pandas`
- `matplotlib`

### Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/JaredMalan7/Stock-Market-App.git
cd Stock-Market-App
```

2. **Create and Activate Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the App**
```bash
python main.py
```

---

## 🧠 Features

| Feature                          | Description |
|----------------------------------|-------------|
| ✅ Input-based Analysis          | Enter any stock ticker and date range |
| ✅ Statistical Summary           | Avg close, max close, volatility |
| ✅ Positive Streak Tracking      | Detects longest streak of gain days |
| ✅ High Volume Day               | Identifies day with most trades |
| ✅ Chart Visualizations          | Line + bar charts saved automatically |
| ✅ File Export                   | Saves stats to a `.txt` file in `/results` |

---

## 📊 Chart Visualizations

### 1. Daily Closing Prices with 7-Day Moving Average
- A line chart showing stock price trend
- Includes a smoothed 7-day moving average overlay

### 2. Monthly Average Closing Prices
- A bar chart showing average monthly closing values
- Good for observing long-term patterns

Charts are saved in the `/results/` folder as:
- `{ticker}_daily_closing_prices_with_ma.png`
- `{ticker}_monthly_avg_close.png`

---

## 📝 Result Export

After analysis:
- You’re asked if you want to save your results
- If “y”, a `.txt` file with analysis is saved in `/results`

Example:
```
AAPL_analysis.txt
```

---

## 📁 Code Structure

```bash
/Stock-Market-App
│
├── main.py                  # Main logic, user inputs, orchestrates modules
├── fetcher.py               # Retrieves stock data from Yahoo Finance
├── analyzer.py              # Computes statistics and insights
├── visualizer.py            # Generates line and bar plots
├── exporter.py              # Exports results to a text file
├── config.py                # Holds default ticker and date configs
├── requirements.txt         # All Python package dependencies
├── results/                 # Folder where outputs are saved
└── README.md                # You're reading it 😄
```

---

## 🔍 Sample Output

```
Enter stock ticker (default: AAPL): 
Enter start date YYYY-MM-DD (default: 2024-01-01): 
Enter end date YYYY-MM-DD (default: 2024-12-31): 

 Preview of Data:
                                 Open        High  ...  Dividends  Stock Splits
Date                                               ...                         
2024-01-02 00:00:00-05:00  186.03  187.31  ...        0.0           0.0
...

Analysis Results:
Average close: 206.37
Highest close: 258.74
Volatility: 25.59
Longest positive streak: 13
Highest volume day: 2024-09-20
Highest volume value: 318679900

Would you like to save the results to a file? (y/n): y
Results saved to results/AAPL_analysis.txt
Charts saved to results/
```

---



## 📚 Useful Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Docs](https://matplotlib.org/stable/index.html)
- [yfinance GitHub](https://github.com/ranaroussi/yfinance)
- [Yahoo Finance](https://finance.yahoo.com/)
- [Python Official Docs](https://docs.python.org/3/)


---

## 🧪 Stretch Features Completed

- ✅ Visual chart output using matplotlib
- ✅ User-controlled export
- ✅ Organized output in `/results` folder
- ✅ Modular file structure

---

