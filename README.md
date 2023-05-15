# F1_Driver_Wars
Requirements for the program
----------------------------

! Important !
Due to personal time constraint I have not finished working on this project. As stated in the description of this task:
"Note: due to potentially needing to wait for the pair-programming sessions, you can work on this project in parallel 
to the main project. In extreme cases, you may even continue and complete this part after you have passed this sprint’s 
corrections."
I will finish this task as soon as I have committed the main project of this sprint.
Sorry! But there are serious objective reasons for this delay.

As a compensation, this program will be a little bit more interesting than the requirements of this task prescribe. (As
you can see in the description below. :)

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