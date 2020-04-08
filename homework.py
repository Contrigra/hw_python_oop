import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record_instance):
        self.records.append(record_instance)

    def get_today_stats(self):
        today_stats = 0
        date_now = dt.datetime.now().date()
        for record in self.records:
            if record.date == date_now:
                today_stats += record.amount
        return today_stats

    def get_week_stats(self):
        week_amount = 0
        date_now = dt.datetime.now()
        date_week_ago = date_now - dt.timedelta(weeks=1)  # Learning time a week ago
        for record in self.records:
            if record.date > date_week_ago.date():
                week_amount += record.amount
        return week_amount


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_eaten = self.get_today_stats()  # Requesting stats for today
        limit_left = self.limit - calories_eaten
        if limit_left > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {limit_left} кКал"
        else:
            return f"Хватит есть!"


class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 60.0
    def get_today_cash_remained(self, currency):
        spent_money = self.get_today_stats()
        cash_remainder = self.limit - spent_money  #Calculating the remainder
        cash_remainder = float(cash_remainder)  #Transforming remainder into float
        #branching, for different currencies
        if currency == "rub":    # TODO rewrite using dictionary
            if cash_remainder > 0:
                return f"На сегодня осталось {round(cash_remainder, 2)} руб"
            elif cash_remainder == 0:
                return f"Денег нет, держись"
            elif cash_remainder < 0:
                return f"Денег нет, держись: твой долг - {abs(round(cash_remainder, 2))} руб"
        elif currency == "eur":
            cash_remainder = cash_remainder / self.EURO_RATE
            if cash_remainder > 0:
                return f"На сегодня осталось {round(cash_remainder, 2)} Euro"
            elif cash_remainder == 0:
                return f"Денег нет, держись"
            elif cash_remainder < 0:
                return f"Денег нет, держись: твой долг - {abs(round(cash_remainder, 2))} Euro"
        elif currency == "usd":
            cash_remainder = cash_remainder / self.USD_RATE
            if cash_remainder > 0:
                return f"На сегодня осталось {round(cash_remainder, 2)} USD"
            elif cash_remainder == 0:
                return f"Денег нет, держись"
            elif cash_remainder < 0:
                return f"Денег нет, держись: твой долг - {abs(round(cash_remainder, 2))} USD"


class Record(Calculator):
    def __init__(self, amount, comment, date = None):
        self.date_format = "%d.%m.%Y"
        self.amount = amount
        self.comment = comment
        self.date = date
        # Checking the data type of date.
        if date is None:        # Request current time and transform it via .date method to the suitable format
            self.date = (dt.datetime.now()).date()
        else:                   # Reformat string of time to the desired format
            self.date = (dt.datetime.strptime(self.date, self.date_format)).date()
