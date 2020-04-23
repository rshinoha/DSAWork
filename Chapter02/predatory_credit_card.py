# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Creativity exercise C-2.27
# Ryoh Shinohara
# =======================================================================================
# **C-2.28** The `PredatoryCreditCard` class of Section 2.4.1 provides a `process_month`
# method that models the completion of a monthly cycle. Modify the class so that once a
# customer has made ten calls to charge in the current month, each additional call to
# that function results in an additional $1 surcharge.
#
# **C-2.29** Modify the `PredatoryCreditCard` class from Section 2.4.1 so that a customer
# is assigned a minimum monthly payment, as a percentage of the balance, and so that a
# late fee is assessed if the customer does not subsequently pay that minimum amount
# before the next monthly cycle.
#
# **C-2.30** At the close of Section 2.4.1, we suggest a model in which the `CreditCard`
# class supports a nonpublic method, `set_balance(b)`, that could be used by subclasses
# to affect a change to the balance, without directly accessing the `_balance` data
# member. Implement such a model, revising both the `CreditCard` and
# `PredatoryCreditCard` classes accordingly.

from credit_card import CreditCard

MAX_CALL = 10
SURCHARGE = 1
MIN_PAYMENT_PER = 0.2

class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr, call=0, payment=0, late_fee=False):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    call      number of calls in a month (default 0)
    payment   minimum payment required (default 0)
    late_fee  whether customer has a late fee or not (default False)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr
    self._call = call
    self._payment = payment
    self._late_fee = late_fee

  def get_apr(self):
    return self._apr

  def get_call(self):
    return self._call

  def get_payment(self):
    return self._payment

  def get_late_fee(self):
    return self._late_fee

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    self._call += 1
    success = super().charge(price)          # call inherited method
    if not success:
      self._balance += 5                     # assess penalty
    if self._call > MAX_CALL:                # additional surcharge if toomany calls
      self._balance += SURCHARGE
    return success                           # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      self._balance *= monthly_factor

  def minimum_payment(self):
    """Returns the minimum payment required at the end of monthly cycle"""
    self._payment =  self._balance * MIN_PAYMENT_PER

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
    self._payment = max(0, self._payment - amount)
    self._balance -= amount

  def need_late_fee(self):
    """
    Returns whether customer has accrued a late fee
    
    Based on whether they have paid the minimum amount
    """
    self._late_fee = self._payment > 0


if __name__ == "__main__":
  card = PredatoryCreditCard("bob", "TCF", "1122233", 200, 0.0825)
  for i in range(15):
    card.charge(10)
  card.process_month()
  print(card.get_balance())     # print 156.05733147172415
  card.minimum_payment()
  print(card.get_payment())     # print 31.205466970935408
  card.make_payment(30)
  card.need_late_fee()
  print(card.get_late_fee())    # print True
  card.make_payment(1.3)
  card.need_late_fee()
  print(card.get_late_fee())    # print False
  print(card.get_balance())     # print 124.72733485467704
  card.set_balance(500)
  print(card.get_balance())     # print 500