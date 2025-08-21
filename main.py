from flask import Flask, render_template, request
import os
import psycopg2

app = Flask(__name__)

# Get DB URL from Render Environment Variable
DATABASE_URL = os.environ.get("DATABASE_URL")

# Connect to DB
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    route TEXT,
    travel_date DATE,
    prediction TEXT
);
""")
conn.commit()

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

        # Save result in DB
        cursor.execute(
            "INSERT INTO predictions (route, travel_date, prediction) VALUES (%s, %s, %s)",
            (route, travel_date, prediction)
        )
        conn.commit()

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
