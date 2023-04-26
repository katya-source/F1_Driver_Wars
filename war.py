import csv
import random
import sys

def main():
    print_welcome()
    player_name = get_player_name()

    deck_of_cards,list_of_choices = get_deck_from_file("F1.csv")
    random.shuffle(deck_of_cards)
    player_deck = Deck(player_name,deck_of_cards[26:])
    computer_deck = Deck("Computer",deck_of_cards[:26])

    while True:
        player_card = player_deck.withdraw()
        display_card(list_of_choices, player_card)
        choice_of_attribute = get_choice(list_of_choices)
        computer_card = computer_deck.withdraw()
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

        if display_result(result,player_deck.deck_size,computer_deck.deck_size) == False:
            break

    say_goodbye()


def print_welcome():
    print("Welcome to War Of Cards!")
    print("Here are the rules:")
    print("-" * 60)
    print("* You play against the computer. Each of you gets half of a stack of cards, well-shuffled. ")
    print("* With each turn, you both compare your top cards according to the attribute which you choose.")
    print("* Whichever cards is better by this attribute wins, and the owner gets both cards and puts them on the bottom of his stack.")
    print("* In case of a draw, both players put their cards to the bottom of their stacks.")
    print("* Whoever runs out of cards, loses the game.")
    print("-" * 60)
    print("Good luck!\n")
    

def say_goodbye():
    print("Thank you for playing! I hope you enjoyed it.\nSee you next time!")
    sys.exit(0)
    

def get_player_name():
    player_name = input("Enter your name (or q to quit): ")
    if player_name.lower() == "q":
        say_goodbye()
    return player_name
    

def get_deck_from_file(file_name):
    try:
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            headers = csv_reader.fieldnames
            csv_data = []
            for row in csv_reader:
                csv_data.append(list(row.values))
    except FileNotFoundError:
        print(f"I could not find the file with the deck of cards. Sorry")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while trying to read the deck of cards: {e}. Sorry!")
        sys.exit(1)
    return csv_data, headers


def display_card(list_of_choices, card):
    print("Your card:")
    print("-" * 20)
    print(f"Formula One Pilot {card[0]}")
    for idx in range(1,len(list_of_choices)):
        print(f"{idx}. {list_of_choices[idx]}:\t{card[idx]}")


def get_choice(list_of_choices):
    print("Please choose the attribute:")
    while True:
        player_input = input(f"Choose a number from 1 to {len(list_of_choices)} or 'q' to quit the game: ")
        if player_input.lower() == "q":
            say_goodbye()
        try:
            player_choice = int(player_input)
            if 1 < player_choice < len(list_of_choices)+1:
                continue
            return player_choice
        except ValueError:
            continue

        
def compare_cards(attr,player_card,computer_card):
    if player_card[attr] > computer_card[attr]:
        return 1
    if player_card[attr] < computer_card[attr]:
        return -1
    return 0
    

def display_result(result,):
    ...


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

    def withdraw(self):
        card = self._deck[0]
        self._deck.pop(0)
        return card
    
    def deck_size(self):
        return len(self._deck)
        
    def add_card(self, card):
        self._deck.append(card)


if __name__ == "__main__":
    main()