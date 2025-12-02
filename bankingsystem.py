


class User:
    
    def __init__(self, name: str, balance: int, checking_account: bool):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            raise ValueError("Nicht genug Deckung")
        return f"{self.name} has {self.balance}."
    
    def add_cash(self, amount):
        self.balance += amount
        return f"{self.name} has {self.balance}"
    
    def check(self, issuer, amount):
        if issuer.checking_account == True:
            if amount < issuer.balance:
                issuer.balance -= amount
                self.balance += amount
                #print(f"{self.name} has {self.balance} and {issuer.name} has {issuer.balance}.")
            else:
                raise ValueError("Nicht genug Deckung.")
            return f"{self.name} has {self.balance} and {issuer.name} has {issuer.balance}."
        else:
            raise ValueError("Kein Scheck-Account.")
               


if __name__ == "__main__":
    Jeff = User('Jeff', 70, True)
    Joe = User('Joe', 70, True)
    try:
        print(Jeff.withdraw(2))
    except ValueError as e:
        print(e)

    try:
        print(Joe.check(Jeff,50))
    except ValueError as e:
        print(e)
    try:
        print(Jeff.check(Joe, 80))
    except ValueError as e:
        print(e)