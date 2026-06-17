"""Lightweight plotting helpers."""


def save_bar_chart(df, x, y, path, title=None, xlabel=None, ylabel=None):
    """Save a simple matplotlib bar chart from a dataframe."""
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df[x], df[y])
    if title:
        ax.set_title(title)
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path
