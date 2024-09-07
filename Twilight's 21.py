import random
import os

# Function to deal a card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate the score
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

# Function to play the game
def play_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Twilight's 21")
    print("----------------------------")

    player_hand = []
    computer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    game_over = False

    while not game_over:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Twilight's 21")
        print("----------------------------")

        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print("\nYour cards: ", player_hand, ", current score: ", player_score)
        print("Twilight's first card: ", computer_hand[0])

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if should_continue == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Twilight's 21")
    print("----------------------------")

    print("\nYour final hand: ", player_hand, ", final score: ", player_score)
    print("Twilight's final hand: ", computer_hand, ", final score: ", computer_score)

    if player_score > 21:
        return "You went over. Now you don't have a house!"
    elif computer_score > 21:
        return "Twilight went over. You're a billionare!"
    elif player_score == computer_score:
        return "It's a draw!"
    elif player_score == 0:
        return "Blackjack! You are the gambling king!"
    elif computer_score == 0:
        return "Twilight got a Blackjack. You are now one million dollars in debt!"
    elif player_score > computer_score:
        return "You win! The gambling gods have shed their mercy upon you!"
    else:
        return "You lose! Cut the losses while you still can!"

# Main menu
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Twilight's 21")
    print("----------------------------")
    print("[1] Let's Go Gambling")
    print("[2] Exit The Casino")
    choice = input("What would you like to do? ")

    if choice == '1':
        print("\n" + play_game())
        input("Press Enter to continue...")
        main_menu()
    elif choice == '2':
        print("\nYou exit the casino and cut down on your losses... Coward...")
    else:
        print("\nInvalid choice. Please try again.")
        main_menu()

main_menu()