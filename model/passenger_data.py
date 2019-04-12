class PassengerData(object):
    def __init__(
        self,
        sex: int,
        title: str,
        age: float,
        Pclass: int,
        cabin: int,
        SibSp: int,
        ParCh: int,
        fare: float,
        embarked: str
    ):
        self.sex = sex
        self.title = title
        self.age = age
        self.Pclass = Pclass
        self.cabin = cabin
        self.SibSp = SibSp
        self.ParCh = ParCh
        self.fare = fare
        self.embarked = embarked
