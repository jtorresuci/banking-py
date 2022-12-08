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
        
    ## Gets the current balance of this account.
    #  @return the current balance
    #
    def getBalance(self):
        return self._balance
    
    ## Gets the account type of this account.
    #  @return the accountType 
    #
    def getAccountType(self):
        return self._accountType
    
    ## Gets the account number 
    #  @return the accNum
    #
    def getAccNum(self):
        return self._accNum
    
    ## Makes a withdrawal from this account, if account does not have enought raise ValueError
    #  sufficient funds are not available.
    #  @param amount the amount of the withdrawal
    #
    def withdraw(self, amt):
        try:
            if amt <= self._balance:
                self._balance -= amt
            else:
                raise ValueError
        except ValueError:
            print("Insufficient funds")
            
    ## Deposits money into this account.
    #  @param amount to deposit
    #
    def deposit(self, amt):
        self._balance += amt
        
    # transfers money from one account to another
    # @param amount to transfer, bankAccount obj
    #
    def transfer(self, amt, bank_account2):
        try:
            if amt <= self._balance:
                self._balance -= amt
                bank_account2.deposit(amt)
            else:
                raise ValueError
        except ValueError:
            print("Insufficient funds")        
    
    # display users account 
    # @return accNum , accName , Balance, accType
    #
    def displayAccountInfo(self):
        print(self._balance)
        print(self._accNum)
        print(self._accName)
        print(self._accountType)
        
    ## Adds interest to this account.
    #  @param self
    #   @returns interest amount 
    def addInterest(self):
        if self._accoutType == "saving":
            amount = self.Financial.percentOf(self._interest, self._balance)
            self._balance += amount
        else:
            self._balance = self._balance

    class Financial:    
        def percentOf(interestRate, balance):
            balance *= interestRate
            return balance

    
    

