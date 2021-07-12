#Update existing User class to have an association with the BankAccount class.'BankAccount Class' has to be defined first as it needs to accessed by 'User class'

class BankAccount:# declaring class named BankAccount and parameters 
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate 
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):# decreases the account balance by the given amount if there are sufficient funds
        if self.balance >= amount:
            self.balance -= amount 
        else:
            self.balance -= 5 
            print(f"User: {self.name}-Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):# print to the console: eg."Balance:$100"
        print(f"Balance: ${self.balance}")
        return self

    
class User:		# declaring class named User and parameters  
    def __init__(self, username, email, account_number, int_rate=0, balance=0):
    #adding attributes and reference to "BankAccount" attributes
        self.name = username  
        self.email = email
        self.accountname = account_number
        self.account = BankAccount(int_rate, balance) 

    # Argument that is the amount of the deposit, Withdraw
    def make_deposit(self, amount): 
        self.account.deposit(amount)	# Note-the User class doesn't have an 'account_balance' attribute anymore. We can call the BankAccount instance's methods through User, or access its attributes
        print(f"User:{self.name}, Account number:{self.accountname}, Balance:${self.account.balance},  Interest Rate: {self.account.int_rate}%")
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"User:{self.name}, Account number:{self.accountname}, Balance:${self.account.balance},  Interest Rate: {self.account.int_rate}%")
        return self

    def yield_interest(self):# increases the account balance by the current balance * the interest rate(as long as the balance is positive)
        # if self.balance > 0:
        #     interest_yield = self.balance * self.rate
        #     self.balance += interest_yield
        # return self

        if self.account.balance > 0:
            self.account.balance += self.account.balance * self.account.int_rate
        return self
        

    def display_user_balance(self):
        print(f"User: {self.name}, Email: {self.email}, Account number: {self.accountname}")
        self.account.display_account_info()
        return self

# Instances/Objects creation
emily1 = User("Emily", "emily6@email.com", 1234, 1)
emily2 = User("Emily", "emily6@email.com", 5678, .1)
tanya = User("Tanya", "tan2@lol.com", 111, 1.2, 2000 )

emily1.make_deposit(100).make_deposit(300).make_withdrawal(300).display_user_balance()
emily2.make_deposit(300).make_withdrawal(100).display_user_balance()

tanya.make_withdrawal(100).make_withdrawal(200).yield_interest().display_user_balance()



