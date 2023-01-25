"""
Assignment 5: Blackjack

This program is a modified version of blackjack in which the probabilities
for drawing each of 13 cards is equal and independent of previous card draws.
"""
from random import choice
from time import sleep
# I used the sleep function to print statements with small delays in order to
# make the output text easier for the user to follow.

deck = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
        '10':10, 'J':10, 'Q':10, 'K':10}
# I prepared a dictionary consisting of the 13 cards and their corresponding
# values in order to easily refer to the card names while still having
# numerical values that can be used for calculating hand totals.

def draw():
    """
    This function draws a card from a standard deck with the same probability
    for each card no matter what the previous draws are, similarly to an
    infinite uno deck.
    """
    return choice(list(deck))

print('\nWelcome to Slackjack, the blackjack simulator where you can hone '
      'your *skills* in a *luck-based* game.\n')
sleep(1)
print('Whether you hit the best hand of your life or you suffer an '
      'unbelievable defeat, you can choose when to walk away.\n')
sleep(1)
print('This is so you can practice cutting your wallet some slack, and '
      'that\'s how this simulator got its name!\n')
sleep(1)

#def main():
# I did not want to use this because linter was complaining about the large
# number of loops and statements I was using within one main function

while True: # This while loop is responsible for the blackjack simulation.
    print(f'{"":-^100}')
    # Every time the while loop is run, I want to visually separate the new
    # round from the previous round for better clarity.

    new_game = input('\nWould you like to start a new game? (y/n): ')

    if new_game.lower().startswith('y'):
        print('\nBest of luck to you. Cards will now be dealt.\n')
        sleep(1)
    elif new_game.lower().startswith('n'):
        print('\nGood job, you are walking away from gambling!\n')
        sleep(1)
        print('Slackjack will now exit.\n')
        sleep(1)
        break
    else:
        print('\nPlease clearly indicate either \'y\' (yes) or \'n\' (no).\n')
        sleep(1)
        continue
        # Since this is the "play again" section of the game, it determines
        # whether or not to restart the entire while loop (AKA the game), so
        # I had to put it as early in the loop as possible.
        # Without doing this, I couldn't check for invalid inputs.

    ace_counter = [0, 0]
    # Aces might have to change value from 11 to 1, so a counter is needed to
    # track the number of aces valued only at 11.
    # Index 0 represents the player. Index 1 represents the dealer.
    # I chose to represent it as a list so that linter would not complain
    # about snake case for a constant value

    player_card1 = draw()
    player_card2 = draw()
    # This generates the first 2 cards for the user/player

    player_open = [player_card1, player_card2]
    for card in player_open:
        if card == 'A':
            ace_counter[0] += 1
    # This counts the number of aces in the player's opening hand

    dealer_card1 = draw()
    dealer_card2 = draw()
    # This generates the first 2 cards for the dealer

    dealer_open = [dealer_card1, dealer_card2]
    for card in dealer_open:
        if card == 'A':
            ace_counter[1] += 1
    # This counts the number of aces in the dealer's opening hand

    player_total = deck[player_card1] + deck[player_card2]
    if ace_counter[0] == 2:
        ace_counter[0] += -1
        player_total += -10
    # Aces have a default value of 11 so if the player gets 2 aces, they have
    # a hand total of 22. To account for this case, this code changes one ace
    # to have a value of 1 instead of 11

    dealer_total = deck[dealer_card1] + deck[dealer_card2]
    if ace_counter[1] == 2:
        ace_counter[1] += -1
        dealer_total += -10
    # This code does the same as the previous section, but for the dealer.

    print(f'You are dealt {player_card1} and {player_card2}. '
          f'Your total is {player_total}.\n')
    sleep(1)
    print(f'The dealer draws {dealer_card1}. The other card is hidden.\n')
    sleep(1)

    while player_total < 21:
        move = input('Would you like to hit or stand? (h/s): ')
        if move.lower().startswith('h'):
            player_hit = draw()
            if player_hit == 'A':
                ace_counter[0] += 1
            # If player draws 11-value ace, the player's ace counter increases
            player_total += deck[player_hit]
            if player_total > 21:
                if ace_counter[0] > 0:
                    ace_counter[0] += -1
                    player_total += -10
            # If the player total exceeds 21 while having an ace of value 11,
            # the ace value is changed to 1 and the player's turn continues.
            print(f'\nYou decide to hit and are dealt {player_hit}. '
                  f'Your total is now {player_total}.\n')
            sleep(1)
        elif move.lower().startswith('s'):
            print('\nYou decide to stand.\n')
            sleep(1)
            break
        else:
            print('\nPlease enter either \'h\' (hit) or \'s\' (stand).\n')
            sleep(1)
            continue
            # The program keeps asking for the user's move until they give a
            # valid input.

    if player_total > 21:
        print('BUST! Your total is over 21.\n')
        sleep(1)
        print('Dealer wins! Good thing there was no real money involved.\n')
        sleep(1)
        continue
        # The player loses if their hand exceeds 21 without any 11 value aces

    print('It is now the dealer\'s turn.\n')
    sleep(1)
    #The dealer's turn begins when the player stands or reaches 21.

    print(f'The dealer has {dealer_card1} and reveals their hidden card: '
          f'{dealer_card2}. Their total is {dealer_total}.\n')
    sleep(1)

    while dealer_total <= 16:
    # The dealer has to keep hitting until they pass 16
        dealer_hit = draw()
        if dealer_hit == 'A':
            ace_counter[1] += 1
        # If dealer draws 11-value ace, the dealers's ace counter increases
        dealer_total += deck[dealer_hit]
        if dealer_total > 21:
            if ace_counter[1] > 0:
                ace_counter[1] += -1
                dealer_total += -10
        # If the dealer total exceeds 21 while having an ace of value 11,
        # the ace value is changed to 1 and the dealer's turn continues.
        print(f'The dealer must hit. They draw {dealer_hit}. '
              f'Their total is now {dealer_total}.\n')
        sleep(1)
    if dealer_total > 21:
        print('BUST! The dealer\'s total is over 21.\n')
        sleep(1)
        print('You win! Your prize is a grand total of: $0.00 and pride.\n')
        sleep(1)
        continue
        # If the dealer's hand exceeds 21, the user/player wins.

    print('The dealer has passed 16 and must stand.\n')
    # If the dealer passes 16 without going bust, their turn ends.
    sleep(1)
    print(f'Your total is {player_total} and the dealer\'s '
          f'total is {dealer_total}.\n')
    sleep(1)
    # The hand totals are summarized for the user's convenience.
    if player_total <= dealer_total:
        print('Dealer wins! Good thing there was no real money involved.\n')
        sleep(1)
        continue
        # If there is a tie, the dealer wins. Otherwise, the hand with the
        # greater total wins.
    print('You win! Your prize is a grand total of: $0.00 and pride.\n')
    sleep(1)
    continue
    # The code only reaches this point if the player total beats the dealer
