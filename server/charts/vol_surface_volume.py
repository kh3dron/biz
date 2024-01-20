import plotly.express as px
import pandas as pd


def vol_surface_volume(ticker):
    filename = "../frd_complete_plus_options_sample/option_chain_" + ticker + ".csv"
    df = pd.read_csv(filename)
    df["ticker"] = ticker

    # DTE column
    df["Trade Date"] = pd.to_datetime(df["Trade Date"], errors="coerce")
    df["Expiry Date"] = pd.to_datetime(df["Expiry Date"], errors="coerce")
    df["DTE"] = (df["Expiry Date"] - df["Trade Date"]).dt.days

    fig = px.scatter_3d(
        df,
        x="STrike",
        y="DTE",
        z="Bid Implied Volatility",
        color="Call/Put",
        color_continuous_scale="viridis",
        size="Volume",
        labels={
            "STrike": "Strike",
            "DTE": "Days to Expiry",
            "Bid Implied Volatility": "Implied Volatility",
        },
        title="Volatility Surface for "
        + ticker
        + " Option Chain - Bid Implied Volatility",
        height=1200,
        width=1200,
    )
    fig.update_layout(coloraxis_colorbar=dict(title="Implied Volatility"))

    return fig
