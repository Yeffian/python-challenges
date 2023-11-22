from enum import Enum
import random

NAMES = {
    "Donald Trump": 100,
    "Micheal": 700,
    "Dennis Ritche": 900,
    "Linus Torvalds": 750,
    "Terry Davis": 1000,
    "Bill Gates": 300,
    "Guido Van Rossum": 800,
    "Ada Lovelace": 500,
    "Donald Knuth": 170,
    "Bjarne Stroustrup": 200,
    "Alan Turing": 950
}

class Card:
    def __init__(self, name, value) -> None:
        self.value = value
        self.name = name

    def __repr__(self) -> str:
        return f'{self.name} = {self.value}'

def create_random_card():
    name, value = random.choice(list(NAMES.items()))
    card = Card(name, value)
    return card
    
class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.score = 0
        self.cards = []
    
    def draw_cards(self, no):
        for n in range(no):
            card = create_random_card()
            #im aware this can still result in duplicates but im too lazy 
            if card in self.cards:
                card = create_random_card()
            
            self.cards.append(card.name)

    def remove_card(self, name):
        self.cards.remove(name)

    def give_point(self):
        self.score += 1

class Game:
    def __init__(self) -> None:
        self.player_no = 2
        self.player_one = Player("Player 1")
        self.player_one.draw_cards(5)
        self.player_two = Player("Player 2")
        self.player_two.draw_cards(5)
        
    
    def play(self):
        # for i in range(self.player_no):
        #     player = Player(i, self.deck)
        #     player.draw_card()
        #     self.players.append(player)
        #     print(f'Player {i} has Card(Suit = {player.card.suit}, Value = {player.card.value})')
        
        # print('Scoring now..')
        # highest_player_id = 0
        # for player in self.players:
        #     if player.card.value > self.get_player_by_id(highest_player_id).card.value:
        #         highest_player_id = player.id
        
        # print(f'Player {highest_player_id} won the War!')

        for i in range(1, 6):
            print("Player 1's deck: ")
            for card in self.player_one.cards:
                print('- ' + card)

            p_one_card = input('Who do you want to play? ')

            print("Player 2's deck: ")
            for card in self.player_two.cards:
                print('- ' + card)

            p_two_card = input('Who do you want to play? ')

            self.player_one.remove_card(p_one_card)
            self.player_two.remove_card(p_two_card)

            if NAMES[p_one_card] > NAMES[p_two_card]:
                print('Player 1 gets the point!')
                self.player_one.give_point()
            elif NAMES[p_two_card] > NAMES[p_one_card]:
                print('Player 2 gets the point!')
                self.player_two.give_point()
            elif NAMES[p_one_card] == NAMES[p_two_card]:
                print('No one gets the point!')
            
        print(self.player_one.score)
        print(self.player_two.score)
            
            


g = Game()
g.play()