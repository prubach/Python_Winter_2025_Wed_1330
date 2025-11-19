class Customer:
    last_id = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Cust[{self.id}, {self.first_name}, {self.last_name}]'

class Account:
    last_id = 1000
    def __init__(self, customer):
        self.customer = customer
        self._balance = 0
        Account.last_id += 1
        self.id = Account.last_id

    def __repr__(self):
        return f'Acc[{self.id}, {self.customer.last_name}, {self._balance}]'

class Bank:
    def __init__(self, name):
        self.name = name
        self.account_list = []
        self.customer_list = []

    def create_customer(self, first_name, last_name):
        customer = Customer(first_name, last_name)
        self.customer_list.append(customer)
        return customer

    def create_account(self, customer):
        account = Account(customer)
        self.account_list.append(account)
        return account

    def __repr__(self):
        return f'Bank[{self.name}\n{self.account_list}\n{self.customer_list}\n]'

bank = Bank('SGH Bank')
c1 = bank.create_customer('John', 'Brown')
a1 = bank.create_account(c1)
a2 = bank.create_account(c1)
c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)
print(bank)

