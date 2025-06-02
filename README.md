# News Sentiment and Stock Price Correlation Analysis

## 🧠 Project Overview

This project is **A Challenge**, designed to analyze how financial news sentiment impacts stock price movements. The goal is to combine natural language processing (NLP) techniques with financial market data to extract insights that can guide predictive analytics in finance.

I use:

- A **sentiment-scored news dataset** (headlines, sentiment scores, and publication dates).
- **Historical stock prices** for several major companies (AAPL, AMZN, TSLA, etc.).

The core objectives:

- Perform sentiment analysis on news headlines using TextBlob.
- Generate technical indicators (SMA, RSI, MACD).
- Align news and stock data by date to compute correlations.
- Use Pearson, Spearman, and Kendall correlation coefficients to analyze relationships.
- Visualize insights through well-structured and reusable plots.

---

## 📁 Project Structure

.
├── data/ # All raw and processed data files
│ ├── yfinance_data/ # Historical stock CSV files
│ │ ├── AAPL_historical_data.csv
│ │ └── ...
│ └── sentiment_analysis.csv
│
├── notebooks/ # Jupyter notebooks for all tasks
│ ├── eda_news_sentiment.ipynb
│ ├── sentiment_return_correlation.ipynb
│ └── correlation_analysis.ipynb
│
├── scripts/ # Python modules for reusability
│ ├── data_visualization.py
│ └── correlation_utils.py
│
├── requirements.txt # Required Python packages
├── .gitignore
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   """
   git clone https://github.com/BetselotYitagesu/news_sentiment_stock.git
   cd news_sentiment_stock
   """
   Set up virtual environment:

# Windows

python -m venv .venv
.venv\Scripts\activate

# macOS/Linux

python3 -m venv .venv
source .venv/bin/activate

    Install required packages:

pip install -r requirements.txt

🧪 How to Run the Project

    Launch Jupyter Notebook or VS Code.

    Navigate to the notebooks/ directory.

    Run the notebooks in this order:


    Ensure your stock and sentiment data are in the appropriate data/ subfolders.

    Customize reusable functions in the scripts/ directory as needed.

📊 Features and Techniques Used

    📈 EDA on Stock Data: Price trends, daily returns, moving averages, and volume spikes.

    💬 Sentiment Analysis: NLP with TextBlob to quantify tone of financial news headlines.

    🧮 Technical Indicators: TA-Lib-based indicators like RSI, MACD, and SMA.

    📉 Correlation Analysis: Pearson, Spearman, and Kendall methods to measure alignment between news sentiment and market returns.

    📦 Modular Code: Custom plotting and correlation tools in scripts/ folder for easy reuse and clarity.

    🔧 Flake8/Black Compliance: Clean, well-documented, and PEP8-compliant Python code.

📌 Key Deliverables

    ✔️ sentiment_analysis.csv: Final sentiment-scored dataset.

    ✔️ sentiment_analysis.ipynb: Sentiment scoring + EDA on headlines and publishers.

    ✔️ stock_eda.ipynb: Trends and indicators for individual stocks.

    ✔️ correlation_analysis.ipynb: Date-aligned data merging and correlation computation.

    ✔️ Modular scripts: data_visualization.py, correlation_utils.py

📚 Requirements

    Python 3.10+

    pandas, numpy

    matplotlib, seaborn

    textblob

    scipy

    yfinance

    TA-Lib (optional, for indicators)

Install all dependencies using:

pip install -r requirements.txt

📬 License

This project is part of the 10 Academy Artificial Intelligence Mastery Program and is intended for educational purposes only.

---

Let me know if you’d like a version with badges (like build status, Python version) or deployment instructions for Streamlit.
