from bankAccount import BankAccount

#Instantiate 3 objects
samsAcc = BankAccount(100, "Sam", "saving")
leilasAcc = BankAccount(500, "Leila", "saving")
adamsAcc = BankAccount(100, "Adam", "checking")


# adding interest to all three accounts
adamsAcc.addInterest()
leilasAcc.addInterest()
samsAcc.addInterest()

# using getBalance to print
print(f"Leila's balance after interest is $%.2f"%(leilasAcc.getBalance()))
print(f"Sam's balance after interest is $%.2f"%(samsAcc.getBalance()))
print(f"Adam's balance after interest is $%.2f"%(adamsAcc.getBalance()))

# testing exception with transfer more than balance amount
print("")
samsAcc.transfer(200, adamsAcc)
leilasAcc.transfer(50, adamsAcc)

# testing transfer and getName/getBalance
print("")
print(f'{adamsAcc.getName()}\'s account balance after transfer is ${adamsAcc.getBalance():.2f}')
print(f'{leilasAcc.getName()}\'s account balance after transfer is ${leilasAcc.getBalance():.2f}')

# testing deposit method
leilasAcc.deposit(100)
samsAcc.deposit(100)
adamsAcc.deposit(100)
print(f'{leilasAcc.getName()}\'s balance after deposit is ${leilasAcc.getBalance():.2f}')
print(f'{samsAcc.getName()}\'s balance after deposit is ${samsAcc.getBalance():.2f}')
print(f'{adamsAcc.getName()}\'s balance after deposit is ${adamsAcc.getBalance():.2f}')

# testing withdraw method
adamsAcc.withdraw(300)
samsAcc.withdraw(200)
leilasAcc.withdraw(200)

print("")
print(f'{leilasAcc.getName()}\'s balance after withdrawal is ${leilasAcc.getBalance():.2f}')
print(f'{samsAcc.getName()}\'s balance after withdrawal is ${samsAcc.getBalance():.2f}')

# Testing getAccNum and getAccountyType Methods
print("")
print(f'{adamsAcc.getName()} account num: {adamsAcc.getAccNum()}')
print(f'{adamsAcc.getName()} account type: {adamsAcc.getAccountType()}')
print("")

samsAcc.displayAccountInfo()
leilasAcc.displayAccountInfo()
adamsAcc.displayAccountInfo()
