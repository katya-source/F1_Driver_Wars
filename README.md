# F1_Driver_Wars
Requirements for the program
----------------------------

- The human player plays against the computer
- At the beginning, a welcome message with the rules is printed
- Human player is asked for his name
- The deck consists of 52 "vanity cards" of famous Formula 1 drivers with the following information (categories):
    - Name
    - Consecutive leading laps
    - Number of World champion titles
    - Number of won races
    - Age at first win
    - Number of fastest laps
    - Number of Podiums
- The deck is loaded from a csv file into a list of dictionaries
- The deck list is shuffled
- The deck is split in half and given to player and computer
- At each turn:
    1. The player is shown his top card with all info
    2. The player chooses the category to be compared
    3. The computer top card is shown.
    4. Compare both cards by chosen category
        - if player wins, add both cards at end of his deck
        - if computer wins, add both cards at end of its deck
        - if draw add each player's card at end of his/its deck
    5. Display result (who won) and remaining cards in each deck
- Game is finished when one player has no cards left
- Display result
- Ask if player wants to play again.