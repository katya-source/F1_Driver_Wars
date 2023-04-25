import random

def main():
    print_welcome()
    player_name = get_player_name()
    deck_of_cards,list_of_choices = get_deck_from_file("F1.csv")
    random.shuffle(deck_of_cards)
    player_deck = Deck(player_name,deck_of_cards[26:])
    computer_deck = Deck("Computer",deck_of_cards[:26])
    while True:
        player_card = player_deck.get_player_top_card()
        display_card(player_card)
        choice_of_attribute = get_choice(list_of_choices)
        computer_card = computer_deck.get_player_top_card()
        display_card(computer_card)
        result = compare_cards(choice_of_attribute,player_card,computer_card)
        if result == 1: # player wins
            player_deck.add_card(player_card)
            player_deck.add_card(computer_card)
        elif result == -1:
            computer_deck.add_card(player_card)
            computer_deck.add_card(computer_card)
        else:
            player_deck.add_card(player_card)
            computer_deck.add_card(computer_card)
        player_deck.remove_top_card()
        computer_deck.remove_top_card()
        if display_result(result,player_deck.deck_size,computer_deck.deck_size) == False:
            break

    say_goodbye()


def print_welcome():
    ...
    
def say_goodbye():
    ...
    
def get_player_name():
    ...
    
def get_deck_from_file(file_name):
    return list_of_cards, headers

def get_choice(list_of_choices):  # 0-5 index
    return index
        
def compare_cards(choice_of_attribute,player_card,computer_card):
    return # 1, -1 , 0
    
def display_result(result,)
    
class Deck:
    def __init__(self,name,deck):
        self.name = name
        self.deck = deck

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def deck(self):
        return self._deck
    
    @deck.setter
    def deck(self,deck):
        self._deck = deck

    def get_player_top_card():
        return self._deck[0]
    
    def deck_size(self):
        return len(self._desk)
        
    def remove_top_card(self):
        ...

    def add_card(self):
        ...