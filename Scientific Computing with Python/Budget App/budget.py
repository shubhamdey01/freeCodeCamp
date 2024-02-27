class Category:
    # costructor
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # object as string
    def __str__(self):
        # title
        star = (30 - len(self.name))//2
        s = '*' * star + self.name + '*' * (30 - star - len(self.name)) + '\n'

        # items in ledger
        for item in self.ledger:
            s += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"

        # total
        s += f"Total: {self.get_balance():.2f}"
        return s

    # deposit mthod
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # withdraw method
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # get balance method
    def get_balance(self):
        bal = 0
        for item in self.ledger:
            bal += item['amount']
        return bal

    # transfer method
    def transfer(self, amount, budgetCategory):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budgetCategory.name)
            budgetCategory.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    # check funds method
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


# function to create spend chart
def create_spend_chart(categories):
    # total withdrawals & catagory wise withdrawals
    total = 0
    withdraws = {}
    for category in categories:
        sum = 0
        for item in category.ledger:
            if item['amount'] < 0:
                sum += item['amount']
        withdraws[category.name] = sum
        total += sum

    # bar chart
    bar = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        bar += f"{i:3}| "
        for category in categories:
            if withdraws[category.name] / total * 100 >= i:
                bar += "o  "
            else:
                bar += "   "
        bar += "\n"
    bar += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # category names
    m = max([len(category.name) for category in categories])
    for i in range(m):
        bar += "     "
        for category in categories:
            if i < len(category.name):
                bar += category.name[i] + "  "
            else:
                bar += "   "
        if i != m - 1:
            bar += "\n"
    return bar
