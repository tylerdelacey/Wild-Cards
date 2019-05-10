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
        print "You Busted!"

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
            print new_card
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
                # print new_card
                print ("\nDealer sum is {}".format(dealer_sum))



    #Compare cards to dealers
    # compare_cards()
    if player_sum >= 21:
        print "\nYOU LOSE"
    if (player_sum <= dealer_sum):
        print "\nYOU WIN"
    else:
        print "\nYOU LOSE"



    print "\nTOTAL: "
    print player_sum

    #hit or stand option for player
    #you busted!

    again = raw_input("Do you want to play again?:  ")
    print("\nWelcome Back {}".format(name))
