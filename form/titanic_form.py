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
        default = "2",
        validators = [
            validators.InputRequired()
        ]
    )

    ticket_strategy = SelectField(
        "How would you buy tickets?",
        choices = [
            ("0", "As cheap as possible"),
            ("1", "Something decent, average within ticket class"),
            ("2", "Best possible cabin and deck")
        ],
        default = "1",
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
