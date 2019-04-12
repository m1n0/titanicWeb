from wtforms import Form, TextField, validators, SubmitField, DecimalField, IntegerField, SelectField

class TitanicForm(Form):
    sex = SelectField(
        "Sex:",
        choices = [
            ("1", "Male"),
            ("0", "Female")
        ],
        validators = [
            validators.InputRequired()
        ]
    )

    title = SelectField(
        "Title:",
        choices = [
            ("Mr", "Mr"),
            ("Miss", "Miss"),
            ("Mrs", "Mrs"),
            ("Master", "Master")
        ],
        validators = [
            validators.InputRequired()
        ]
    )

    age = DecimalField(
        "Age:",
        default = 30,
        places = 0,
        validators = [
            validators.InputRequired(),
            validators.NumberRange(
                min = 0.5,
                max = 80,
                message = "Age must be between 0.5 and 80"
            )
        ]
    )

    Pclass = SelectField(
        "Ticket class:",
        choices = [
            ("1", "First Class"),
            ("2", "Second Class"),
            ("3", "Third Class")
        ],
        validators = [
            validators.InputRequired()
        ]
    )

    cabin = SelectField(
        "Has private cabin or not:",
        choices = [
            ("1", "Yes"),
            ("0", "No")
        ],
        validators = [
            validators.InputRequired()
        ]
    )

    SibSp = IntegerField(
        "Number of siblings and/or spouses aboard:",
        default = 0,
        validators = [
            validators.InputRequired(),
            validators.NumberRange(
                min = 0,
                max = 9,
                message="Number must be between 0 and 9"
            )
        ]
    )

    ParCh = IntegerField(
        "Number of parents and/or children aboard:",
        default = 0,
        validators = [
            validators.InputRequired(),
            validators.NumberRange(
                min = 0,
                max = 9,
                message = "Number must be between 0 and 9"
            )
        ]
    )

    fare = DecimalField(
        "Passenger Fare ($):",
        default = 33,
        places = 1,
        validators = [
            validators.InputRequired(),
            validators.NumberRange(
                min = 0,
                max = 512,
                message = "Fare must be between 0 and 512"
            )
        ]
    )

    embarked = SelectField(
        "Port of Embarkation:",
        choices = [
            ("S", "Southampton, England"),
            ("C", "Cherbourg, France"),
            ("Q", "Queenstown, Ireland")
        ],
        validators = [
            validators.InputRequired()
        ]
    )

    submit = SubmitField("Predict")
