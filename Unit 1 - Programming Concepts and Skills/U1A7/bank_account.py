class BankAccount:
    def __init__(self, name: str, ssn: int, address: str, balance: float) -> None:
        self.name = name
        self.ssn = ssn
        self.address = address
        self.balance = balance

    def show_profile(self) -> None:
        print(self.name)
        print(self.ssn)
        print(self.address)
        print(self.balance)

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} has been withdrawn. Remaining Balance: ${self.balance}")
        else:
            print(f"Insufficient balance. You only have ${self.balance}")

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Deposit success. New balance ${self.balance}")
