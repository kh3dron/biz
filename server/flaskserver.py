from flask import Flask, request, render_template, jsonify

app = Flask(__name__)



@app.route("/")
def hello_world():
    import plotly.express as px

    # Assuming df is your DataFrame
    import warnings

    warnings.simplefilter(action="ignore", category=FutureWarning)

    import pandas as pd


    def load_data(ticker):
        filename = "../frd_complete_plus_options_sample/option_chain_" + ticker + ".csv"
        df = pd.read_csv(filename)
        df["ticker"] = ticker

        return df


    ticker = "META"
    df = load_data(ticker)

    # DTE column

    df["Trade Date"] = pd.to_datetime(df["Trade Date"], errors="coerce")
    df["Expiry Date"] = pd.to_datetime(df["Expiry Date"], errors="coerce")
    df["DTE"] = (df["Expiry Date"] - df["Trade Date"]).dt.days

    df["Spread Volatility"] = (
        df["Bid Implied Volatility"] + df["Ask Implied Volatility"] / 2
    )


    fig = px.scatter_3d(
        df,
        x="STrike",
        y="DTE",
        z="Bid Implied Volatility",
        color="Call/Put",
        color_continuous_scale="viridis",
        labels={
            "STrike": "Strike",
            "DTE": "Days to Expiry",
            "Bid Implied Volatility": "Implied Volatility",
        },
        title="Volatility Surface for " + ticker + " Option Chain - Bid Implied Volatility",
        height=1200,
        width=1200,
    )
    fig.update_layout(coloraxis_colorbar=dict(title="Implied Volatility"))
    fig = fig.to_html(full_html=False, include_plotlyjs='cdn')


    # Add colorbar

    return render_template("index.html", plot=fig)


if __name__ == "__main__":
    app.run(debug=True, port=8100)
