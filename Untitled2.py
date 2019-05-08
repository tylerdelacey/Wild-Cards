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

print "Welcome to Wild Cards!"
name = raw_input("Give me your name:  ")
print("Hello, " + name)

# Construct a Deck instance, with 52 cards.
deck = pydealer.Deck()

# Shuffle the deck, in place.
deck.shuffle()

# Deal some cards from the deck.
player_cards = deck.deal(2)

dealer_cards = deck.deal(2)
player_sum = 0
dealer_sum = 0
print "Player's Hand"
print player_cards
print "Dealer's Hand"
print dealer_cards
choice = raw_input("Would you like to hit or stay?:  ")
print ("You choose to " + choice )

     #give number after you hit or stay
for card in player_cards:
    print convert_card(card.value)
    player_sum+= convert_card(card.value)

for card in dealer_cards:
    print convert_card(card.value)
    dealer_sum+=convert_card(card.value)

if player_sum <= 21 :
    pass
else:
    print "You Busted!"
# zero is hit
if int(choice) == 0:
    print "You said hit"
    new_card = deck.deal(1)
    for card in new_card:
        player_sum+=convert_card(card.value)
        print new_card
    else:
        print "You stay"



#Compare cards to dealers
compare_cards()

if (player_sum >= dealer_sum and player_sum <= 21):
    print "You win the round!"
else:
    print "You lose the round!"

print "Your total is"
print player_sum

#hit or stand option for player
#you busted!
