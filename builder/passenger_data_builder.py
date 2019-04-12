from model.passenger_data import PassengerData

class PassengerDataBuilder(object):
    @staticmethod
    def build_from_form_data(form_data: list) -> PassengerData:
        return PassengerData(
            int(form_data["sex"]),
            form_data["title"],
            float(form_data["age"]),
            int(form_data["Pclass"]),
            int(form_data["Pclass"]),
            int(form_data["SibSp"]),
            int(form_data["ParCh"]),
            float(form_data["fare"]),
            form_data["embarked"]
        )
