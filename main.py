import datetime


class Client:

    def __init__(self, first, last, cpf):
        self.first = first
        self.last = last
        self.cpf = cpf


class Historic:

    def __init__(self):
        self.open_date = datetime.datetime.today()
        self.transactions = []

    def prints(self):
        print(f"Open date: {self.open_date}")
        print("Transactions: ")
        for t in self.transactions:
            print("-", t)


class Account:

    def __init__(self, number, client, balance, limit=1000.0):
        if not isinstance(client, Client):
            raise TypeError(f"client must be of type Client not {type(client)}")
        self.holder = client
        self.number = str(number)
        self.balance = float(balance)
        self.limit = float(limit)
        self.historic = Historic()

    def deposit(self, amount):
        self.balance += amount
        self.historic.transactions.append(f"Deposit of R$ {amount}")

    def withdraw_money(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            self.historic.transactions.append(f"Cash withdraw of R$ {amount}")

    def bank_statement(self):
        print(f"Account number: {self.number}\n Account amount: {self.balance}")
        self.historic.transactions.append(f"Took extract - Balance of {self.balance}")
        return self.balance

    def transfer_to(self, destiny, amount):
        withdrew = self.withdraw_money(amount)
        if not withdrew:
            return False
        else:
            destiny.deposit(amount)
            self.historic.transactions.append(f"Transfer of R$ {amount} for account {destiny.number}")
            return True
