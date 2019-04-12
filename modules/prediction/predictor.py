import pickle
import numpy as np
import os
from model.passenger_data import PassengerData

class Predictor(object):
    @staticmethod
    def predict(passenger_data: PassengerData):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, './model.pkl')
        with open(filename, "rb") as f:
            model = pickle.load(f)

        probability = model.predict_proba(Predictor.__preprocess(passenger_data))[0, 1]

        return probability

    @staticmethod
    def __preprocess(passenger_data: PassengerData) -> list:
        age = passenger_data.age
        sex = passenger_data.sex
        embarked = passenger_data.embarked
        Pclass = passenger_data.Pclass
        title = passenger_data.title

        # Set up Fare value based on ticket buying strategy (values are hardcoded here and come from data exploration).
        s = passenger_data.ticket_strategy
        if Pclass == 1:
            if s == 0:
                fare = 30
            elif s == 1:
                fare = 84
            else:
                fare = 428
        if Pclass == 2:
            if s == 0:
                fare = 13
            elif s == 1:
                fare = 20
            else:
                fare = 53
        if Pclass == 3:
            if s == 0:
                fare = 8
            elif s == 1:
                fare = 14
            else:
                fare = 55

        x = {
            "Fare": fare,
            "AgeCategory_Infant": int(age <= 5),
            "AgeCategory_Child": int(age > 5 and age <= 12),
            "AgeCategory_Teenager": int(age > 12 and age <= 18),
            "AgeCategory_YoungAdult": int(age > 18 and age <= 35),
            "AgeCategory_Adult": int(age > 35 and age <= 60),
            "AgeCategory_Senior": int(age > 60 and age <= 100),
            "Sex_female": int(sex == 0),
            "Sex_male": int(sex == 1),
            "Embarked_C": int(embarked == "C"),
            "Embarked_Q": int(embarked == "Q"),
            "Embarked_S": int(embarked == "S"),
            "Pclass_1": int(Pclass == 1),
            "Pclass_2": int(Pclass == 2),
            "Pclass_3": int(Pclass == 3),
            "FamilySize": passenger_data.SibSp + passenger_data.ParCh + 1,
            "Title_Mr": int(title == "Mr"),
            "Title_Mrs": int(title == "Mrs"),
            "Title_Miss": int(title == "Miss"),
            "Title_Master": int(title == "Master")
        }

        return np.array(list(x.values())).reshape(1, -1)
