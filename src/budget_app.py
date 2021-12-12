from typing import List

class Category:

    def __init__(self, name) -> None:
        self.name = name
        self.ledger = []

    def __str__(self) -> str:
        total = 0
        s = f"{self.name:*^30}\n"
        
        for item in self.ledger:
            s += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}\n"
            total += item["amount"]           
        return s + f"Total: {total:.2f}"

    def deposit(self, amount, description="") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description="") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    def transfer(self, amount, category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount) -> bool:
        return self.get_balance() >= amount

    def get_amount_withdrawn(self) -> float:
        return sum(list(map(lambda item: item["amount"], filter(lambda item: item["amount"] < 0, self.ledger))))

def get_total_percent(categories) -> List:
    amounts_withdrawn = list(map(lambda category: category.get_amount_withdrawn(), categories))
    return list(map(lambda amount: amount / sum(amounts_withdrawn) * 100, amounts_withdrawn))

def create_spend_chart(categories) -> str:
    chart = ""
    title = "Percentage spent by category\n"
    
    percents = get_total_percent(categories)

    for i in range(100, -10, -10):
        row = f"{i}| ".rjust(5)
        for percent in percents:
            if percent >= i:
                row += "o".ljust(3)
            else:
                row += " " * 3
        chart += row.ljust(len(categories) * 5 - 1) + "\n"

    row = "-" + "---" * len(categories)
    chart += row.rjust(len(row) + 4)
    names = list(map(lambda category: category.name, categories))
    longest_name = max(names, key=len)

    for i in range(len(longest_name)):
        row = "\n" + " " * 5
        for name in names:
            if i < len(name):
                row += name[i].ljust(3)
            else:
                row += " " * 3
        chart += row
        
    return title + chart

def main():
    """
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)
    print(auto)

    print(create_spend_chart([food, clothing, auto]))
    """

    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)

    print(create_spend_chart([business, food, entertainment]))

if __name__ == "__main__":
    main()