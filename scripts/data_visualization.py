
import matplotlib.pyplot as plt


class Visualizer:
    '''Here is a class for data visualization purpose '''

    def __init__(self, df):
        self.df = df

    def plot_close_with_sma(
        self, price_col="Close", sma_col="SMA_20",
        title="Close Price & 20-Day SMA"
    ):
        """
        Plots the stock closing price along with a simple moving average (SMA).
        """
        plt.figure(figsize=(12, 5))
        plt.plot(self.df[price_col], label="Close Price")
        plt.plot(self.df[sma_col], label="20-Day SMA", color="orange")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_rsi(self, rsi_col="RSI"):
        """
        Plots the Relative Strength Index (RSI).
        """
        plt.figure(figsize=(10, 3))
        plt.plot(self.df[rsi_col], label="RSI", color="purple")
        plt.axhline(70, linestyle="--", color="red", label="Overbought")
        plt.axhline(30, linestyle="--", color="green", label="Oversold")
        plt.title("Relative Strength Index (RSI)")
        plt.xlabel("Date")
        plt.ylabel("RSI")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_macd(self, macd_col="MACD", signal_col="MACD_signal"):
        """
        Plots the MACD line and the signal line.
        """
        plt.figure(figsize=(10, 3))
        plt.plot(self.df[macd_col], label="MACD", color="blue")
        plt.plot(self.df[signal_col], label="Signal Line", color="orange")
        plt.axhline(0, linestyle="--", color="grey")
        plt.title("MACD Indicator")
        plt.xlabel("Date")
        plt.ylabel("MACD")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()



    