class PassengerData(object):
    def __init__(
        self,
        sex: int,
        title: str,
        age: float,
        Pclass: int,
        ticket_strategy: int,
        SibSp: int,
        ParCh: int,
        embarked: str
    ):
        self.sex = sex
        self.title = title
        self.age = age
        self.Pclass = Pclass
        self.ticket_strategy = ticket_strategy
        self.SibSp = SibSp
        self.ParCh = ParCh
        self.embarked = embarked
