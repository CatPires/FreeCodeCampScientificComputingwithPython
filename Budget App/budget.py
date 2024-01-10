class Category:

    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = []
        self.balance = 0.0

    def check_funds(self, amount):
        if self.balance < amount:
            return False        
        else:
            return True

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.budget_category}"):
            category.deposit(amount, f"Transfer from {self.budget_category}")
            return True
        else:
            return False

    def __str__(self):
        header = '{:*^30}'.format(self.budget_category,'*') + '\n'
        ledger = ""
        for item in self.ledger:
            ledger += '{:23}'.format(item['description'])[:23] + '{:>7.2f}'.format(item['amount'])[:7] + '\n'
        total = "Total: {:.2f}".format(self.balance)
        return header + ledger + total



def create_spend_chart(categories):
    import math

    categories_spent = []
    
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        categories_spent.append(spent)

    total = sum(categories_spent) / 10
    spent_percentage = [math.trunc((cat/total) *10) for cat in categories_spent]

    ## My Bar Chart
    header = "Percentage spent by category\n"

    body = ""
    for value in range(100,-1,-10):
        ab = '%s' %(value)
        body += ab.rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                body += " o "
            else:
                body += "   "
        body += " \n"
    
    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"

    labels = [category.budget_category for category in categories]
    my_max = max([len(label) for label in labels])
    new_labels = [label.ljust(my_max) for label in labels]

    for i in range(my_max):
        line = '     '
        for l in range(len(new_labels)):
            line += new_labels[l][i]+'  '
        if i < (my_max-1):
            line += '\n'
        footer += line

    return header+body+footer