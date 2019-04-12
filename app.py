
from form.titanic_form import TitanicForm
# from gen_html import fit_model
from flask import Flask, render_template, request
from modules.prediction.predictor import Predictor
# from modules import predictor

app = Flask(__name__)

# Home page
@app.route("/", methods=["GET", "POST"])
def home():
    form = TitanicForm(request.form)

    if request.method == "POST" and form.validate():
        sex = int(request.form["sex"])
        title = request.form["title"]
        age = float(request.form["age"])
        Pclass = int(request.form["Pclass"])
        cabin = int(request.form["Pclass"])
        SibSp = int(request.form["SibSp"])
        ParCh = int(request.form["ParCh"])
        fare = float(request.form["fare"])
        embarked = request.form["embarked"]

        predictor = Predictor()
        prediction = predictor.predict(
            sex = sex,
            title = title,
            age = age,
            Pclass = Pclass,
            cabin = cabin,
            SibSp = SibSp,
            ParCh = ParCh,
            fare = fare,
            embarked = embarked
        )

        return render_template(
            "index.html",
            prediction = prediction,
            form = form
        )

    return render_template(
        "index.html",
        form=form
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
