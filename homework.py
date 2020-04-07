import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record_class):
        self.records.append(record_class)

    def get_today_stats(self):
        self.today_stats = 0                                              #Creating a variable
        for self.record in self.records:
            if self.record.date == dt.datetime.now().date():              #Checking if the date is today.
                self.today_stats += self.record.amount
        return self.today_stats                                           #Returning stats of spent money for today.

    def get_week_stats(self):
        self.week_amount = 0
        self.date_now = dt.datetime.now()
        self.date_week_ago = self.date_now - dt.timedelta(days = 7)       #узнаём, время неделю назад
        for self.record in self.records:
            if self.record.date > self.date_week_ago.date():
                self.week_amount += self.record.amount
        return self.week_amount


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        self.limit_left = 0
        self.calories_eaten = 0
        self.date_now = dt.datetime.now().date()
        for self.record in self.records:
            if self.record.date == self.date_now:
                self.calories_eaten += self.record.amount
        self.limit_left = self.limit - self.calories_eaten
        if self.limit_left > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit_left} кКал"
        else:
            return f"Хватит есть!"


class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 60.0
    def get_today_cash_remained(self, currency = None):
        self.spent_money = self.get_today_stats()
        self.cash_remainder = self.limit - self.spent_money #Calculating the remainder
        self.cash_remainder = float(self.cash_remainder)    #Transforming remainder into float type, if we get a non-float
        #branching, for different currencies
        if currency == "rub":
            if self.cash_remainder > 0:
                return f"На сегодня осталось {round(self.cash_remainder, 2)} руб"
            elif self.cash_remainder == 0:
                return f"Денег нет, держись"
            elif self.cash_remainder < 0:
                return f"Денег нет, держись: твой долг - {abs(round(self.cash_remainder, 2))} руб"
        elif currency == "eur":
            self.cash_remainder = self.cash_remainder / self.EURO_RATE
            if self.cash_remainder > 0:
                return f"На сегодня осталось {round(self.cash_remainder, 2)} Euro"
            elif self.cash_remainder == 0:
                return f"Денег нет, держись"
            elif self.cash_remainder < 0:
                return f"Денег нет, держись: твой долг - {abs(round(self.cash_remainder, 2))} Euro"
        elif currency == "usd":
            self.cash_remainder = self.cash_remainder / self.USD_RATE
            if self.cash_remainder > 0:
                return f"На сегодня осталось {round(self.cash_remainder, 2)} USD"
            elif self.cash_remainder == 0:
                return f"Денег нет, держись"
            elif self.cash_remainder < 0:
                return f"Денег нет, держись: твой долг - {abs(round(self.cash_remainder, 2))} USD"


class Record(Calculator):
    def __init__(self, amount, comment, date = None):
        self.date_format = "%d.%m.%Y"
        self.amount = amount
        self.comment = comment
        self.date = date
        # Checking the data type of date.
        if date is None:        #Request current time and transform it via .date method to the suitable format
            self.date = (dt.datetime.now()).date()
        else:                   # if we get a string of time, reformat it into the required format using strptime.
                                #.date transform it into suitable format of datetime-type
            self.date = (dt.datetime.strptime(self.date, self.date_format)).date()



