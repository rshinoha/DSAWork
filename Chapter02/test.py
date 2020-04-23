if __name__ == "__main__":
  from .predatory_credit_card import PredatoryCreditCard


  card = PredatoryCreditCard("bob", "TCF", "1122233", 200, 0.0825)
  for i in range(15):
    card.charge(10)
  card.process_month()
  print(card.get_balance())     # print 156.05733147172415