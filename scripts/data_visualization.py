"""
A data visualization module.
"""

import matplotlib.pyplot as plt


class Visualizer:
    """
    A class for data visualization purposes.
    """

    def __init__(self, df):
        self.df = df

    def _check_columns(self, *cols):
        """
        Check if all required columns exist in the dataframe.

        Raises:
            ValueError: If any required column is missing.
        """
        missing = [col for col in cols if col not in self.df.columns]
        if missing:
            raise ValueError(f"Columns not found: {', '.join(missing)}")

    def _prepare_plot(self, figsize=(10, 5), ax=None):
        """
        Create a new plot or use the given axis.

        Returns:
            tuple: (fig, ax) objects for the plot.
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
        else:
            fig = ax.figure
        ax.grid(True)
        return fig, ax

    def plot_close_with_sma(
        self,
        price_col="Close",
        sma_col="SMA_20",
        title="Close Price & 20-Day SMA",
        figsize=(12, 5),
        ax=None,
        price_color="blue",
        sma_color="orange",
    ):
        """
        Plot the closing price along with a simple moving average (SMA).
        """
        self._check_columns(price_col, sma_col)
        fig, ax = self._prepare_plot(figsize, ax)
        ax.plot(self.df[price_col], label="Close Price", color=price_color)
        ax.plot(self.df[sma_col], label="20-Day SMA", color=sma_color)
        ax.set_title(title)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.legend()
        fig.tight_layout()
        fig.autofmt_xdate()
        if ax is None:
            plt.show()

    def plot_rsi(
        self,
        rsi_col="RSI",
        title="Relative Strength Index (RSI)",
        figsize=(10, 3),
        ax=None,
        line_color="purple",
        overbought_level=70,
        oversold_level=30,
    ):
        """
        Plot the Relative Strength Index (RSI).
        """
        self._check_columns(rsi_col)
        fig, ax = self._prepare_plot(figsize, ax)
        ax.plot(self.df[rsi_col], label="RSI", color=line_color)
        ax.axhline(overbought_level, linestyle="--", label="OverB")
        ax.axhline(oversold_level, linestyle="--", label="OverS")
        ax.set_title(title)
        ax.set_xlabel("Date")
        ax.set_ylabel("RSI")
        ax.legend()
        fig.tight_layout()
        fig.autofmt_xdate()
        if ax is None:
            plt.show()

    def plot_macd(
        self,
        macd_col="MACD",
        signal_col="MACD_signal",
        title="MACD Indicator",
        figsize=(10, 3),
        ax=None,
        macd_color="blue",
        signal_color="orange",
    ):
        """
        Plot the MACD line and the signal line.
        """
        self._check_columns(macd_col, signal_col)
        fig, ax = self._prepare_plot(figsize, ax)
        ax.plot(self.df[macd_col], label="MACD", color=macd_color)
        ax.plot(self.df[signal_col], label="Signal Line", color=signal_color)
        ax.axhline(0, linestyle="--", color="grey")
        ax.set_title(title)
        ax.set_xlabel("Date")
        ax.set_ylabel("MACD")
        ax.legend()
        fig.tight_layout()
        fig.autofmt_xdate()
        if ax is None:
            plt.show()
