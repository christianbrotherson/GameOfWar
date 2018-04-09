from time import sleep

from player_deck_creation import PlayerDeckCreation
from gameplay import Gameplay

def main():
  name = input("Please enter your name: ")
  new_deck = PlayerDeckCreation()
  deck = new_deck.deck_creation()
  player, computer = new_deck.deal_deck(deck)
  game = Gameplay(player, computer)
  while 0 < len(player) < 52:
    player, computer, play = game.flip_cards()
    if play == 'y':
      game.update_decks(player, computer)
    elif play == 'n':
      break
    print(f'\n{name}: {len(player)}\nComputer: {len(computer)}')
    print("\n---------------------------------")
  if len(player) == 52:
    print(f"{name} wins!")
  elif len(computer) == 52:
    print("Computer wins!")

main()