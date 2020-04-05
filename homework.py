import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

class CaloriesCalculator(Calculator):
    pass

class CashCalculator(Calculator):
    pass


class Record(Calculator):

    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date #TODO make current time through datetime
        super().records = records #Как-то надо сделать рекордсы

    def add_record(self):
        self.records.append([self.amount, self.comment, self.date])




calculator1 = Calculator(1500)
r1 = Record(145, "lol", 2019)

r1.add_record()

print(calculator1.records)

