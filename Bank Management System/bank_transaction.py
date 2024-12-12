from main import BankAccount

account1 = BankAccount("1234567890", "Jane Doe", 5000, "Savings")
account2 = BankAccount("0987654321", "John Doe", 3000, "Checking")

account1.deposit()
account1.withdraw()
account1.check_balance()
account1.transfer(account2)