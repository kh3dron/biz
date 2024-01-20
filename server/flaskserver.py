from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

free_tier_tickers = ["AAPL", "AMZN", "DIA", "EEM", "META", "MSFT", "QQQ", "SPY", "TSLA", "VXX"]
free_tier_options = ["AAPL", "META", "TSLA"]

from charts.vol_surface import vol_surface
from charts.vol_surface_volume import vol_surface_volume

@app.route("/vol_surface/<ticker>")
def page_vol_surface(ticker):
    
    print(ticker)
    if ticker not in free_tier_options:
        return jsonify({"error": "Ticker not in free tier"}), 403

    fig = vol_surface(ticker)
    fig = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return render_template("index.html", plot=fig)

@app.route("/vol_surface_volume/<ticker>")
def page_vol_surface_volume(ticker):
    
    print(ticker)
    if ticker not in free_tier_options:
        return jsonify({"error": "Ticker not in free tier"}), 403

    fig = vol_surface_volume(ticker)
    fig = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return render_template("index.html", plot=fig)


if __name__ == "__main__":
    app.run(debug=True, port=8100)
