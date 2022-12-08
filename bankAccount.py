class BankAccount:
    lastAccNum = 0

    # Write function documentation

    ## What does the function do
    # @param self
    # @return: none

    # Test documentation
    # crate 3 bank account objects
    # obj1 ...
    # obj2 ...
    # obj3 ... 
    # calling (short description of what the tests does)

    def __init__(self, init_balance = 0, init_accName ="", init_accountType = ""):
        self._balance = init_balance
        self._accName = init_accName
        self._accountType = init_accountType
        BankAccount.lastAccNum += 1
        self._accNum = BankAccount.lastAccNum 
        self._interest_rate = 0.03

    def getBalance(self):
        return self._balance
    
    def getAccountType(self):
        return self._accountType
    
    def getAccNum(self):
        return self._accNum
    
    def withdraw(self, amt):
        try:
            if amt <= self._balance:
                self._balance -= amt
            else:
                raise ValueError
        except ValueError:
            print("Insufficient funds")

    def deposit(self, amt):
        self._balance += amt

    def transfer(self, amt, bank_account2):
        try:
            if amt <= self._balance:
                self._balance -= amt
                bank_account2.deposit(amt)
            else:
                raise ValueError
        except ValueError:
            print("Insufficient funds")        
    
    def displayAccountInfo(self):
        print(self._balance)
        print(self._accNum)
        print(self._accName)
        print(self._accountType)

    def addInterest(self):
        amt = self.Financial.percentOf(self._interest_rate, self._balance)
        self._balance += amt

    class Financial:    
        def percentOf(interestRate, balance):
            balance *= interestRate
            return balance

    
    

