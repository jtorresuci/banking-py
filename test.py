from bankAccount import BankAccount

#Instantiate 3 objects
adamsAcc = BankAccount(100, "Adam", "checking")
samsAcc = BankAccount(100, "Sam", "saving")
leilasAcc = BankAccount(500, "Leila", "checking")

# adding interest to all three accounts
adamsAcc.addInterest()
leilasAcc.addInterest()
samsAcc.addInterest()

# using getBalance to print
print(f"Leila's balance after interest is $%.2f"%(leilasAcc.getBalance()))
print(f"Sam's balance after interest is $%.2f"%(samsAcc.getBalance()))
print(f"Adam's balance after interest is $%.2f"%(adamsAcc.getBalance()))

# testing exception with transfer more than balance amount

# testing transfer and getName/getBalance
samsAcc.transfer(200, adamsAcc.getName())
leilasAcc.transfer(50, adamsAcc.getName())
print(adamsAcc.getBalance())
print(leilasAcc.getBalance())

print("Leila's balance after interest is $%0.2f" % (leilasAcc.getBalance()))
