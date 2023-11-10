from enum import Enum
import random

class Suits(Enum):
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3

class Card:
    def __init__(self, suit, value) -> None:
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self) -> None:
        self.values = range(0, 14)
        self.cards = []
    
    def create_random_card(self):
        suit = random.choice(list(Suits))
        value = random.choice(self.values)
        card = Card(suit, value)
        self.cards.append(card)
        return card
    
class Player:
    def __init__(self, id, deck) -> None:
        self.id = id
        self.deck = deck
        self.card = None
    
    def draw_card(self):
        self.card = self.deck.create_random_card()

class Game:
    def __init__(self, player_no) -> None:
        self.player_no = player_no
        self.players = []
        self.deck = Deck()
    
    def get_player_by_id(self, id):
        for player in self.players:
            if player.id == id:
                return player
    
    def play(self):
        print('The War is starting!')
        for i in range(self.player_no):
            player = Player(i, self.deck)
            player.draw_card()
            self.players.append(player)
            print(f'Player {i} has Card(Suit = {player.card.suit}, Value = {player.card.value})')
        
        print('Scoring now..')
        highest_player_id = 0
        for player in self.players:
            if player.card.value > self.get_player_by_id(highest_player_id).card.value:
                highest_player_id = player.id
        
        print(f'Player {highest_player_id} won the War!')

g = Game(3)
g.play()