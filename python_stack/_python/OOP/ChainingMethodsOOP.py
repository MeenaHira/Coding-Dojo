class User:		# declaring class named User
    def __init__(self, username, email):# intiating and parameters set
        self.name = username # adding attributes
        self.email = email
        self.account_balance = 0
    # adding the deposit, withdrawl and balance display and BONUS-transfer money from other user methods
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount # the specific user's account decreases by the amount of the value withdrawn
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}") # display of user name  and balance
        return self

    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount # other user transferring money 
        self.account_balance -= amount 
        return self

# Instances/Objects creation(outside Class)
emily = User("Emily", "emily6@email.com")
tanya = User("Tanya", "tan2@lol.com")
dennis = User("Dennis", "Den123@email.com")

#METHOD CALLS---
#Have the first user make 3 deposits and 1 withdrawal and then display their balance
emily.make_deposit(1000).make_deposit(200).make_deposit(50).make_withdrawal(500).display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
tanya.make_deposit(25).make_deposit(2000).make_withdrawal(600).make_withdrawal(200).display_user_balance()


#Have the third user make 1 deposit and 3 withdrawals and then display their balance
dennis.make_deposit(5000).make_withdrawal(250).make_withdrawal(150).make_withdrawal(1000).display_user_balance()


# BONUS-have the first user transfer money to the third user and then print both users' balances
emily.transfer_money(dennis,500).display_user_balance()
dennis.display_user_balance()

#OUTPUT---
# User: Emily, Balance: $750
# User: Tanya, Balance: $1225
# User: Dennis, Balance: $3600
# User: Emily, Balance: $250
# User: Dennis, Balance: $4100