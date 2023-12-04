class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = list()

    def __str__(self):
        formatted = self.category_name.center(30, "*")
        for item in self.ledger:
            formatted += "\n" + f'{item["description"][0:23]:23}' + f'{item["amount"]:>7.2f}'
        formatted += "\nTotal:" + str(self.get_balance()).rjust(7)
        return formatted

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.category_name}"):
            category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def get_withdraw(self):
        total_amount = 0
        for ledger_item in self.ledger:
            if ledger_item['amount'] < 0:
                total_amount += ledger_item['amount']
        return total_amount

    def total_deposit(self):
        total_amount = 0
        for ledger_item in self.ledger:
            if ledger_item['amount'] > 0:
                total_amount += ledger_item['amount']
        return total_amount


def truncate(number, multiplier=10):
    return int((number * multiplier) / multiplier)


def calculate_total(categories):
    total = []
    tmp_list = []
    rounded = []
    for category in categories:
        tmp_list.append(category.get_withdraw())
        total.append(category.total_deposit())
    tmp_list_length = len(tmp_list)
    for i in range(tmp_list_length):
        rounded.append((-tmp_list[i] / total[i]) * 100)

    return rounded


def create_spend_chart(categories):
    output_text = 'Percentage spent by category\n'
    percent = 100
    totals = calculate_total(categories)
    while percent >= 0:
        line = ' '
        for total in totals:
            if total >= percent:
                line += 'o  '
            else:
                line += '   '
        output_text += str(percent).rjust(3) + '|' + line + '\n'
        percent -= 10

    underline = '-' + '---' * len(categories)

    tmp_category_length = 0
    for x in categories:
        if len(str(x.category_name)) > tmp_category_length:
            tmp_category_length = len(str(x.category_name))

    tmp_categories = []
    for x in categories:

        number_of_spaces = tmp_category_length - len(str(x.category_name))
        tmp_end = ' ' * number_of_spaces
        tmp_category_name = str(x.category_name) + tmp_end
        tmp_categories.append(tmp_category_name)

    output_text += underline.rjust(len(underline) + 4) + '\n     '
    letter = 0
    while letter < tmp_category_length:
        for x in tmp_categories:
            output_text += x[letter] + '  '
        output_text += '\n     '
        letter += 1
    return output_text
