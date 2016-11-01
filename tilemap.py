import pygame,sys
from pygame.locals import *

# A list of all tile names. Not actually used for anything (perhaps
# besides sanity checking).
TILENAMES = ('air','concrete')
# A dictionary that connects each tilename to a list of its variant images.
# Variants will be drawn at random to make the grid pattern less obvious.
#(using a fixed seed so the map doesn't flicker)
VARIANTS = {'air':None,'concrete':('0.png','1.png')}

# A map of tiles. Use this for a level.
# A level will be stored as a dictionary of tuples to tilename strings. When
# retreiving a 
class tile_map(object):
    def __init__(self,tile_dict):
        self.tiles = tile_dict
        
    
