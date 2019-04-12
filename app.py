
from form.titanic_form import TitanicForm
from flask import Flask, render_template, request
from modules.prediction.predictor import Predictor
from builder.passenger_data_builder import PassengerDataBuilder

app = Flask(__name__)

# Home page
@app.route("/", methods=["GET", "POST"])
def home():
    form = TitanicForm(request.form)
    prediction = None
    status = None

    if request.method == "POST" and form.validate():
        passengerData = PassengerDataBuilder.build_from_form_data(request.form)
        prediction = int(Predictor.predict(passengerData) * 100)

        if prediction > 70:
            status = "green"
        elif prediction > 40:
            status = "yellow"
        else:
            status = "red"

    return render_template(
        "index.html",
        form = form,
        prediction = prediction,
        status = status
    )

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8888, debug = True)
