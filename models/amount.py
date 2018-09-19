class AmountModel:
    def __init__(self, month, month_amount):
        self.month = month
        self.month_amount = month_amount

    def json(self):
        return {"month": self.month, "month_amount": self.month_amount}

    @classmethod
    def calculate_by_year_amount(cls, month, month_year_rate, year_amount):
        month_amount = year_amount * month_year_rate
        return cls(month, month_amount)


class StandardAmountRate:
    def __init__(self):
        # DBから月順で引っ張ってくること
        standard_month_amount_list = []
        # クラスとして返すリスト
        # month指定用に[0]に0入れておく
        month_year_rate_list = [0]
        for month_amount in standard_month_amount_list:
            month_year_rate_list.append(month_amount / sum(standard_month_amount_list))
        self.month_year_rate_list = month_year_rate_list
