from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        route = request.form["route"]
        travel_date = request.form["travel_date"]

        # Simple demo prediction logic
        if "DEL" in route.upper():
            prediction = "High"
        elif "BLR" in route.upper():
            prediction = "Medium"
        else:
            prediction = "Low"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
