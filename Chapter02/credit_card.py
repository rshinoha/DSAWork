# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Reinforcement exercises R-2.5 to R-2.8 and Creativity exercise 2.30
# Ryoh Shinohara
# =======================================================================================
# **R-2.5** Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number as a
# parameter.
# 
# **R-2.6** If the parameter to the make payment method of the CreditCard class were a
# negative number, that would have the effect of raising the balance on the account.
# Revise the implementation so that it raises a ValueError if a negative value is sent.
# 
# **R-2.7** The CreditCard class of Section 2.3 initializes the balance of a new account
# to zero. Modify that class so that a new account can be given a nonzero balance using
# an optional fifth parameter to the constructor. The four-parameter constructor syntax
# should continue to produce an account with zero balance.
# 
# **R-2.8** Modify the declaration of the first for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three credit
# cards to go over its credit limit. Which credit card is it?
#
# **C-2.30** At the close of Section 2.4.1, we suggest a model in which the `CreditCard`
# class supports a nonpublic method, `set_balance(b)`, that could be used by subclasses
# to affect a change to the balance, without directly accessing the `_balance` data
# member. Implement such a model, revising both the `CreditCard` and
# `PredatoryCreditCard` classes accordingly.

class CreditCard:
    """
    A consumer credit card
    """
    # R-2.7 solution
    def __init__(self, customer, bank, acnt, limit, balance=0):
        """
        Create a new credit card instance
        
        The initial balance is zero.
        
        * customer: the name of a customer (e.g. 'John Bowman')
        * banks: the name of the bank (e.g. 'California Savings')
        * acnt: the account identifier (e.g. '5391 0375 9387 5309')
        * limit: credit limit (measured in dollar)
        """
        
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        # R-2.7 solution
        self._balance = balance
        
    def get_customer(self):
        """
        Returns name of customer
        """
        return self._customer
    
    def get_bank(self):
        """
        Returns the bank's name
        """
        return self._bank
    
    def get_account(self):
        """
        Returns the card identifying number (typically stored as a string)
        """
        return self._account
    
    def get_limit(self):
        """
        Returns credit limit
        """
        return self._limit
    
    def get_balance(self):
        """
        Returns current balance
        """
        return self._balance

    def set_balance(self, balance):
        """Sets a new balance"""
        self._balance = balance
    
    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """ 
        # R-2.5 solution
        if not isinstance(price, (int, float)):
            raise TypeError('price must be numeric')
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """
        Processes customer payment that reduces balance
        """
        # R-2.5 solution
        if not isinstance(amount, (int, float)):
            raise TypeError('amount must be numeric')
        # R-2.6 solution
        if amount < 0:
            raise ValueError('amount must be positive')
        self._balance -= amount

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500) )
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500) )
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000) )

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    # R-1.28 solution
    # Scratch work to find which val to use for for loop
    # val = 1
    # while wallet[0].charge(val) and wallet[1].charge(2*val) and  wallet[2].charge(3*val):
    #     val += 1
    
    # for val in range(1, 58):
    #     wallet[0].charge(val)
    #     wallet[1].charge(2*val)
    #     wallet[2].charge(3*val)

    # tempVal = 58

    # print('Final val: {}'.format(tempVal))
    # print('Wallet 0: {}'.format(wallet[0].charge(tempVal)))
    # print('Wallet 1: {}'.format(wallet[1].charge(2*tempVal)))
    # print('Wallet 2: {}'.format(wallet[2].charge(3*tempVal)))

    # Output:
    # Final val: 58
    # Wallet 0: True
    # Wallet 1: True
    # Wallet 2: False

    # So, wallet 2 will go over the credit limit first. 

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()