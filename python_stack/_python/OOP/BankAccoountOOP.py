class BankAccount:
    def __init__(self, username, int_rate, balance):
        #adding default values for parameters
        self.name = username 
        self.rate = (int_rate * .01)
        self.balance = 0

    def deposit(self, amount):# increases the account balance by the given amount
        self.balance += amount 
        return self

    def withdraw(self, amount):# decreases the account balance by the given amount if there are sufficient funds
        amount_after_withdraw = self.balance - amount
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if amount_after_withdraw < 0:
            print(f"User: {self.name}-Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
        # ANOTHER WAY(BETTER)
        # if self.balance >= amount:
        #     self.balance -= amount 
        # else:
        #     self.balance -= 5 
        #     print(f"User: {self.name}-Insufficient Funds: Charging a $5 fee")
        # return self

    def display_account_info(self):# print to the console: eg."Balance:$100"
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def yield_interest(self):# increases the account balance by the current balance * the interest rate(as long as the balance is positive)
        
        if self.balance > 0:
            interest_yield = self.balance * self.rate
            self.balance += interest_yield
        return self

#creation of Instances(OBJECTS)  or accounts      
emily = BankAccount("Emily", 1, 100)
tanya = BankAccount("Tanya",1.2, 10)

#To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
emily.deposit(1000).deposit(200).deposit(50).withdraw(500).yield_interest().display_account_info()

#To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
tanya.deposit(220).deposit(50).withdraw(100).withdraw(100).withdraw(60).withdraw(50).yield_interest().display_account_info()

#OUTPUT----
# User: Emily, Balance: $757.5
# User: Tanya-Insufficient funds: Charging a $5 fee
# User: Tanya, Balance: $5.06