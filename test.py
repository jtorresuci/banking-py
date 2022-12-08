from bankAccount import BankAccount


adamsAcc = BankAccount(100, "Adam", "checking")
samsAcc = BankAccount(100, "Sam", "saving")
leilasAcc = BankAccount(500, "Leila", "checking")

adamsAcc.addInterest()
leilasAcc.addInterest()
samsAcc.addInterest()

print("Leila's balance after interest is $%0.2f" % (leilasAcc.getBalance()))