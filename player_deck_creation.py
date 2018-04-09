from random import choice, shuffle

class PlayerDeckCreation():

  def __init__(self):
    self.deck = []


  def deck_creation(self):
    deck_list = []
    x = 0
    while x < 4:
      for i in range(2,15):
        deck_list.append(i)
      x += 1
      
    self.deck = deck_list

    return self.deck


  def deal_deck(self, full_deck):
    half_deck = []
    x = 0
    while x < 26:
      num = choice(full_deck)
      half_deck.append(num)
      full_deck.remove(num)
      x += 1
    return full_deck, half_deck
