import pydealer

def convert_card(player_card):
    #convert the string to an integer
    # [int(s) for s in player_card.split() if s.isdigit()]
    try:
        converted_card = [int(s) for s in player_card.split() if s.isdigit()][0]
    except:
        converted_card= 10
    return converted_card

def compare_cards():
    if player_sum <= 21 :
        pass
    else:
        print "\nYou Busted!"

print "\nWelcome to Wild Cards!"
name = raw_input("Give me your name:  ")
print("\nHello, " + name)
salad_dressing = False
while not salad_dressing:

    # Construct a Deck instance, with 52 cards.
    deck = pydealer.Deck()

    # Shuffle the deck, in place.
    deck.shuffle()

    # Deal some cards from the deck.
    player_cards = deck.deal(2)

    dealer_cards = deck.deal(2)
    player_sum = 0
    dealer_sum = 0
    print "\nPlayer's Hand"
    print player_cards
    print "\nDealer's Hand"
    print dealer_cards
    choice = raw_input("\nWould you like to hit or stay?:  ")
    print ("\nYou choose to " + choice )

         #give number after you hit or stay
    for card in player_cards:
        # print convert_card(card.value)
        player_sum+= convert_card(card.value)

    for card in dealer_cards:
        # print convert_card(card.value)
        dealer_sum+=convert_card(card.value)
    if player_sum <= 21 :
        pass
    else:
        print "\nYOU BUSTED"
    # zero is hit

    if choice == "hit":
        print "\nYOU HIT"
        new_card = deck.deal(1)
        for card in new_card:
            player_sum+=convert_card(card.value)
            print("Player's card: " + str(new_card))
        while dealer_sum < 18:
        # if dealer_sum < 21:
            new_card = deck.deal(1)
            for card in new_card:
                dealer_sum+=convert_card(card.value)
                # print new_card
                print ("\nDealer sum is {}".format(dealer_sum))
    else:
        print "\nYOU STAY"
        while dealer_sum < 18:
        # if dealer_sum < 21:
            new_card = deck.deal(1)
            for card in new_card:
                dealer_sum+=convert_card(card.value)
                print("Dealer's Card: " + str(new_card))
                print("\nDealer sum is {}".format(dealer_sum))


    print "\n Player Sum: "
    print player_sum
    print "\n Dealer Sum: "
    print dealer_sum

    #Compare cards to dealers
    # compare_cards()
    if player_sum > 21:
        print "\nYOU LOSE"
    elif (player_sum >= dealer_sum):
        print "\nYOU WIN"
    elif dealer_sum > 21:
        print "\nYOU WIN"
    elif (dealer_sum > player_sum):
        print "\n YOU LOSE"








    again = raw_input("\nDo you want to play again?:  ")
    print("\nWelcome Back {}".format(name))
