
class BankAccount:
    lastAccNum = 1000

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
    
    def getName(self):
        return self._accName
    
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
            print(f'{self._accName} has insufficient funds')
            
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
            print(self.getName() + " has insufficient funds")        
    
    # display users account 
    # @return accNum , accName , Balance, accType
    #
    def displayAccountInfo(self):
        print(f'The account name: {self._accName}')
        print(f'The account num: {self._accNum}')
        print(f'The account type: {self._accountType}')
        print(f'The account balance: ${self._balance:.2f}')
        print("")
        
    ## Adds interest to this account.
    #  @param self
    #   @returns interest amount 
    def addInterest(self):
        if self._accountType == "saving":
            amount = self.Financial.percentOf(self._interest_rate, self._balance)
            self._balance += amount
        else:
            self._balance = self._balance

    class Financial:    
        def percentOf(interestRate, balance):
            balance *= interestRate
            return balance

    
    

