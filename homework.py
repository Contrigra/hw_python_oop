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
        date_week_ago = date_now - dt.timedelta(weeks=1)  # time a week ago
        for record in self.records:
            if record.date > date_week_ago.date():
                week_amount += record.amount
        return week_amount


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_eaten = self.get_today_stats()  # Requesting stats for today
        limit_left = self.limit - calories_eaten
        if limit_left > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с" \
                   f" общей калорийностью не более {limit_left} кКал"
        else:
            return f"Хватит есть!"


class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 60.0
    RUB_RATE = 1
    currency_data = {
        "eur": (EURO_RATE, "Euro"),
        "usd": (USD_RATE, "USD"),
        "rub": (RUB_RATE, "руб")
    }

    def get_today_cash_remained(self, currency=None):
        if currency not in self.currency_data:
            if currency is None:
                currency = "rub"
            else:
                return f"Курс не поддерживается"
        currency_rate = self.currency_data.get(currency)[0]
        currency_name = self.currency_data.get(currency)[1]
        spent_money = self.get_today_stats()
        cash_remainder = (self.limit - spent_money) / currency_rate
        cash_remainder = round(float(cash_remainder), 2)  # reformat to x.xx
        if cash_remainder > 0:
            return f"На сегодня осталось " \
                    f"{cash_remainder} {currency_name}"
        if cash_remainder == 0:
            return f"Денег нет, держись"
        if cash_remainder < 0:
            return f"Денег нет, держись: твой долг - " \
                    f"{abs(cash_remainder)} {currency_name}"


class Record(Calculator):
    def __init__(self, amount, comment, date=None):
        date_format = "%d.%m.%Y"
        self.amount = amount
        self.comment = comment
        self.date = date
        if date is None:    # create the default time
            self.date = (dt.datetime.now()).date()
        else:               # Reformat string of time to the desired format
            self.date = (dt.datetime.strptime(date, date_format)).date()
