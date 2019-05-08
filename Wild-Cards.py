import pydealer
import pygame
from pygame.locals import *
# Construct a Deck instance, with 52 cards.
deck = pydealer.Deck(rebuild=True)
# Shuffle the deck, in place.
deck.shuffle()
# Deal some cards from the deck.
dealt_cards = deck.deal(2)




pygame.init()
screen = pygame.display.set_mode((640, 480))
clock=pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Wild Cards", True, (0, 128, 0))


running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      print event

  # screen.fill((120, 120, 120))
  screen.fill((255, 255, 255))
  screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
  pygame.display.flip()
  clock.tick(60)


pygame.quit()
