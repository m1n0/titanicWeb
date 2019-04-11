import pickle
import numpy as np

class Predictor(object):
    def predict(self, sex, title, age, Pclass, cabin, SibSp, ParCh, fare, embarked):
        with open("model/model.pkl", "rb") as f:
            model = pickle.load(f)

        probability = model.predict_proba(
            self.__preprocess(sex, title, age, Pclass, cabin, SibSp, ParCh, fare, embarked)
        )[0, 1]

        return probability

    @staticmethod
    def __preprocess(sex, title, age, Pclass, cabin, SibSp, ParCh, fare, embarked) -> list:
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
            "FamilySize": SibSp + ParCh + 1,
            "Title_Mr": int(title == "Mr"),
            "Title_Mrs": int(title == "Mrs"),
            "Title_Miss": int(title == "Miss"),
            "Title_Master": int(title == "Master")
        }

        return np.array(list(x.values())).reshape(1, -1)
