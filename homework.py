import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self,record_class):
        self.records.append([record_class.amount, record_class.comment, record_class.date])



class CaloriesCalculator(Calculator):
    pass

class CashCalculator(Calculator):
    123


class Record(Calculator):
    def __init__(self, amount, comment, date = None):
        self.date_format = "%d.%m.%Y"
        self.amount = amount
        self.comment = comment
        self.date = date
        # Checking the data type of date.
        if date is None:        # Requesting current time and then transform it into a string with given date_format
            self.date = dt.datetime.strftime(dt.datetime.now(), self.date_format)
        else:                   # if we get a string of time, reformat it into the given format (strptime formats the string into datetime-object, so we reformat it again in a proper string)
            self.date = dt.datetime.strftime(dt.datetime.strptime(date, self.date_format), self.date_format)





cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))


print(cash_calculator.records)
