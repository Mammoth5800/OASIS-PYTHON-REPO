from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    bmi = None
    category = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 24.9:
                category = "Normal Weight"
            elif bmi < 29.9:
                category = "Overweight"
            elif bmi < 34.9:
                category = "Obese"
            else:
                category = "Extremely Obese"

            bmi = round(bmi, 2)

        except:
            bmi = "Invalid input"

    return render_template("index.html", bmi=bmi, category=category)


if __name__ == "__main__":
    app.run()
