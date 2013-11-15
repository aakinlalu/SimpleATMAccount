#          UML ACCOUNT Class
#   *___________________________________*
#   *           Account                 *
#   *___________________________________*
#   * id: int                           * 
#   * balance: float                    *
#   * annualInterestRate: float         *
#   *___________________________________*
#   * Acount(id: int, balance: float,   *
#   *      annualInterestRate: float)   *
#   *                                   *
#   * getMonthinterest(): float         *
#   * setWithdraw( withdraw: float):    *
#   * setDeposit(deposit: float)        *
#   * getAccountid(): int               *
#   * getBalance(): float               *
#   *___________________________________*


class Account:
    '''
    Using  a constractor to initialize the objects
    '''
    def __init__(self, iD = 0, balance = 100, annualInterestRate = 0,\
                  deposit = 0, withdraw = 0, ):
        self.__iD = iD
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate 
        self.withdraw = withdraw
        self.deposit = deposit
        
        
    def getAccountId(self):
        return self.__iD
    
    def getBalance(self):
        return self.__balance
        
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def getWithdraw(self):
        return self.withdraw
    
    def getDeposit(self):
        return self.deposit
    
    def setAccountId(self, iD):
        self.__iD = iD
        
    def setBalance(self, balance):
        self.__balance = balance
        
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def setWithdraw(self, withdraw):
        self.withdraw = withdraw
                
    def setDeposit(self, deposit):
        self.deposit = deposit    
        
        
    def getMonthInterestRate(self):
        return self.getAnnualInterestRate()/12
    
    
    def getMonthInterest(self):
            return (self.getMonthInterestRate()/100) * self.__balance
      
    
     
    def updateBalance(self):
        return self.getBalance() - self.getWithdraw() + self.getDeposit() 
    
    def updateMonthInterest(self):
            return (self.getMonthInterestRate()/100) * self.updateBalance()
    



    