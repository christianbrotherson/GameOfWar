class Gameplay():

  def __init__(self, player_deck, computer_deck):
    self.player_deck = player_deck
    self.computer_deck = computer_deck
    self.winners_cards = []


  def flip_cards(self):
    play = 'y'
    # play = input("Enter y to flip your next card or n to exit (y or n): ")
    # if play.lower() == 'y':
    player_deck_card = self.player_deck.pop(0)
    computer_deck_card = self.computer_deck.pop(0)
    self.winners_cards.append(player_deck_card)
    self.winners_cards.append(computer_deck_card)

    if player_deck_card == 11:
      print('\nJack')
    elif player_deck_card == 12:
      print('\nQueen')
    elif player_deck_card == 13:
      print('\nKing')
    elif player_deck_card == 14:
      print('\nAce')
    else:
      print(f'\n{player_deck_card}')

    if computer_deck_card == 11:
      print('Jack')
    elif computer_deck_card == 12:
      print('Queen')
    elif computer_deck_card == 13:
      print('King')
    elif computer_deck_card == 14:
      print('Ace')
    else:
      print(computer_deck_card)

    if player_deck_card == computer_deck_card:
      player_deck_card, computer_deck_card, play = self.war()

      if player_deck_card > computer_deck_card:
        self.player_deck = self.player_deck + self.winners_cards
        self.winners_cards.clear()
      
      elif player_deck_card < computer_deck_card:
        self.computer_deck = self.computer_deck + self.winners_cards
        self.winners_cards.clear()

    elif player_deck_card > computer_deck_card:
      self.player_deck = self.player_deck + self.winners_cards
      self.winners_cards.clear()

    elif player_deck_card < computer_deck_card:
      self.computer_deck = self.computer_deck + self.winners_cards
      self.winners_cards.clear()

    # if play.lower() == 'n':
    #   print("exiting")

    return self.player_deck, self.computer_deck, play 


  def war(self):
    play = input("It's a War!\n\nEnter y to lay down your next three cards or n to exit (y or n): ")
    i = 0
    while i < 3:
      player_card = self.player_deck.pop(0)
      self.winners_cards.append(player_card)
      computer_card = self.computer_deck.pop(0)
      self.winners_cards.append(computer_card)
      i += 1
    
    player_deck_card = self.player_deck.pop(0)
    computer_deck_card = self.computer_deck.pop(0)
    self.winners_cards.append(player_deck_card)
    self.winners_cards.append(computer_deck_card)

    print(f"\n---------------------------------\n{player_deck_card}\n{computer_deck_card}")

    return player_deck_card, computer_deck_card, play


  def update_decks(self, player, computer):
    self.player_deck = player
    self.computer_deck = computer