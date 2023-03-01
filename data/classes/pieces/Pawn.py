import pygame
from data.classes.BasePiece import Piece


class Pawn(Piece):
    def __init__(self, pos, race, brd):
        super().__init__(pos, race)
        self.img = pygame.image.load('data/images/Pawn' + race + '.png')
        self.img = pygame.transform.scale(self.img, (brd.tile_h - 40, brd.tile_v - 40))
        self.ispawn = True
        self.type = 'pawn'

    def pmvs(self, brd):
        fin = []
        temp = []
        if self.color == 'WH':
            temp.append([0, -1])
            if not self.pchanged:
                temp.append([0, -2])
        else:
            temp.append([0, 1])
            if not self.pchanged:
                temp.append([0, 2])
        for a in temp:
            np = [self.x, self.y + a[1]]
            if 0 <= np[1] < 8:
                fin.append(brd.sq_fr_pos(np))
        return fin

    def mvs(self, brd):
        fin = []
        for a in self.pmvs(brd):
            if a.piece:
                break
            else:
                fin.append(a)
        if self.color == 'WH':
            if self.x + 1 < 8 and self.y - 1 >= 0:
                sq = brd.sq_fr_pos((self.x + 1, self.y - 1))
                if sq.piece:
                    if sq.piece.color != self.color:
                        fin.append(sq)
            if self.x - 1 >= 0 and self.y - 1 >= 0:
                sq = brd.sq_fr_pos((self.x - 1, self.y - 1))
                if sq.piece:
                    if sq.piece.color != self.color:
                        fin.append(sq)
        else:
            if self.y + 1 < 8 and self.x + 1 < 8:
                sq = brd.sq_fr_pos((self.x + 1, self.y + 1))
                if sq.piece:
                    if sq.piece.color != self.color:
                        fin.append(sq)
            if self.x - 1 >= 0 and self.y + 1 < 8:
                sq = brd.sq_fr_pos((self.x - 1, self.y + 1))
                if sq.piece:
                    if sq.piece.color != self.color:
                        fin.append(sq)
        return fin

    def attsq(self, brd):
        return [i for i in self.mvs(brd) if i.x != self.x]