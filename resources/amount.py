from models.amount import AmountModel, StandardAmountRate


class UserAmount:
    @staticmethod
    def calculate_user_amount(month, month_amount):
        # 最終的に出力したいのがこのリスト
        # monthでの抽出用に[0]に0代入
        user_month_amount_list = [0]
        # 各月の使用量を出すには、年間使用量が必要
        month_year_rate = StandardAmountRate()
        user_year_amount = month_amount / month_year_rate.month_year_rate_list[month]
        # 各月の使用量を計算
        for month_count in range(1, 13):
            user_month_amount = AmountModel.calculate_by_year_amount(month_count,
                                                                     month_year_rate.month_year_rate_list[month],
                                                                     user_year_amount)
            user_month_amount_list.append(user_month_amount.month_amount)
        return user_month_amount_list
