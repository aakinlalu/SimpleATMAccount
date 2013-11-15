from simpleAcount import Account

def main():
    ''' (int, float, float, float, float,) -> float
    
    Return the balance of the account
    
    '''
    
    print '_________________________________________________'
    print '| Assuming the person has $20,000 in the account|'
    print '|_______________________________________________|'
    print '|Assumming the Annual interest rate is 4.5%     |'
    print '|_______________________________________________|'
    
    balance = 20000
    annualInterestRate = 4.5
    
    print '\t'
    
    id = str(input('Enter your four digit Acount number: '))
    
    
   # deposit money into the account 
    
    indicate = raw_input('Want to deposit? Please Enter yes/ no: ')
    
    if indicate == 'yes':
        
        deposit = float(input('Enter the amount in number only: '))
        
        A = Account(id, balance, annualInterestRate, deposit)
        
        indicate = raw_input('Do you want to see your new balance? Please \
        Enter yes/no: ')
        
        if indicate == 'yes':
            
            balance_result = A.updateBalance()
            
            monthlyInterest = A.updateMonthInterest()
            
            print 'Account Number:', A.getAccountId()
            
            print 'New balance: $', balance_result
            
            print 'Monthly interest based on the new balance is $', monthlyInterest
            
        else:
            
            balance_result = A.getBalance()
            
            print 'Thank you for banking with us!'
  
  # Withdraw money from the account     
        
    else:
        
        indicate2 = raw_input('want to Withdraw? Enter yes/ no: ')
        
        if indicate2 == 'yes':
            withdraw = float(input('Enter the amount in number only: '))
            
            A = Account(id, balance, annualInterestRate, 0, withdraw)
            
            indicate2 = raw_input('Do you want to see your new balance? Please \
            Enter yes/no: ')
            
            if indicate2 == 'yes':
                
                balance_result = A.updateBalance()
                
                monthlyInterest = A.updateMonthInterest()
                
                print 'Account Number:', A.getAccountId()
                
                print 'New balance: $', balance_result
                
                print 'Monthly interest based on the new balance is $', monthlyInterest
                
            else:
                
                print 'Thank you for banking with us!'    
    
# Check your balance


        else:
            A = Account(id, balance, annualInterestRate)
            
            balance_result = A.getBalance()
            
            print 'Account Number:', A.getAccountId()
            
            print 'Your balance is $', float(balance_result)
            
            print 'Your monthly interest is $', A.getMonthInterest()
            
            
   