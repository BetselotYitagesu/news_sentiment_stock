import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def compute_correlation_matrix(
    df: pd.DataFrame, columns: list[str]
) -> dict:
    """
    Compute Pearson, Spearman, and Kendall correlation matrices.

    Args:
        df (pd.DataFrame): The dataframe containing the data.
        columns (list[str]): The list of columns to include in correlation.

    Returns:
        dict: A dictionary with correlation matrices.
    """
    corr_results = {
        "pearson": df[columns].corr(method="pearson"),
        "spearman": df[columns].corr(method="spearman"),
        "kendall": df[columns].corr(method="kendall"),
    }
    return corr_results


def plot_correlation_heatmap(
    corr_matrix: pd.DataFrame,
    title: str = "Correlation Heatmap"
) -> None:
    """
    Plot a heatmap for a given correlation matrix.

    Args:
        corr_matrix (pd.DataFrame): The correlation matrix to visualize.
        title (str): Title for the heatmap.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def run_correlation_analysis(
    df: pd.DataFrame, columns: list[str]
) -> None:
    """
    Run full correlation analysis and plot heatmaps.

    Args:
        df (pd.DataFrame): The dataframe to analyze.
        columns (list[str]): The columns to analyze.
    """
    corrs = compute_correlation_matrix(df, columns)
    for method, matrix in corrs.items():
        title = f"{method.capitalize()} Correlation Heatmap"
        plot_correlation_heatmap(matrix, title=title)
