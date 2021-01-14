class Account:
  def __init__(self,owner,balance = 0):
    self.owner = owner
    self.balance = balance

  def __str__(self):
    return f'Account owner:   ${self.owner}\nAccount balance: ${self.balance}'

  def deposit(self,dep_amt):
    self.balance += dep_amt
    print('Deposit Accepted')

  def withdraw(self,wd_amt):
    if self.balance >= wd_amt:
      self.balance -= wd_amt
      print('Withdrawal Accepted')
    else:
      print('Funds Unavailable!')

# 1. Instantiate the class
acct1 = Account('Jose',100)

# 3. Show the account owner attribute

# 3. Show the account owner attribute
print(acct1)
acct1.deposit(50)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

