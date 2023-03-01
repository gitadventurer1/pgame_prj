import pygame
from data.classes.BasePiece import Piece


class Knight(Piece):
    def __init__(self, pos, color, brd):
        super().__init__(pos, color)
        self.img = pygame.image.load('data/images/Knight' + str(self.color) + '.png')
        self.img = pygame.transform.scale(self.img, (brd.tile_h - 20, brd.tile_v - 20))
        self.type = 'knight'

    def mvs(self, brd):
        fin = []
        mv = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]
        for a in mv:
            ptemp = (self.x + a[0], self.y + a[1])
            if 0 <= ptemp[0] < 8 and 0 <= ptemp[1] < 8:
                fin.append(brd.sq_fr_pos(ptemp))
        return fin