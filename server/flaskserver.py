from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

from charts.vol_surface import vol_surface

@app.route("/")
def hello_world():
    

    fig = vol_surface("AAPL")
    fig = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return render_template("index.html", plot=fig)


if __name__ == "__main__":
    app.run(debug=True, port=8100)
