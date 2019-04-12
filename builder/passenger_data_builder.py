from model.passenger_data import PassengerData

class PassengerDataBuilder(object):
    @staticmethod
    def build_from_form_data(form_data: list) -> PassengerData:
        return PassengerData(
            sex = int(form_data["sex"]),
            title = form_data["title"],
            age = float(form_data["age"]),
            Pclass = int(form_data["Pclass"]),
            ticket_strategy = int(form_data["ticket_strategy"]),
            SibSp = int(form_data["SibSp"]),
            ParCh = int(form_data["ParCh"]),
            embarked = form_data["embarked"]
        )
