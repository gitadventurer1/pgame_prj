import pygame
from data.classes.BasePiece import Piece


class King(Piece):
    def __init__(self, pos, color, brd):
        super().__init__(pos, color)
        self.img = pygame.image.load('data/images/King' + str(self.color) + '.png')
        self.img = pygame.transform.scale(self.img, (brd.tile_h - 20, brd.tile_v - 20))
        self.type = 'king'

    def mvs(self, brd):
        fin = []
        mv = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        for a in mv:
            ptemp = (self.x + a[0], self.y + a[1])
            if 0 <= ptemp[0] < 8 and 0 <= ptemp[1] < 8:
                fin.append(brd.sq_fr_pos(ptemp))
        return fin

    def rakir(self, brd):
        if not self.pchanged:
            if self.color == 'WH':
                lr = brd.sq_fr_pos([0, 7]).piece
                rr = brd.sq_fr_pos([7, 7]).piece
                if lr:
                    if not lr.pchanged:
                        if [brd.sq_fr_pos([1, 7]).piece, brd.sq_fr_pos([2, 7]).piece, brd.sq_fr_pos([3, 7]).piece] == [None, None, None]:
                            return 'left'
                if rr:
                    if not rr.pchanged:
                        if [brd.sq_fr_pos([5, 7]).piece, brd.sq_fr_pos([6, 7]).piece] == [None, None]:
                            return 'right'
            elif self.color == 'BL':
                lr = brd.sq_fr_pos([0, 0]).piece
                rr = brd.sq_fr_pos([7, 0]).piece
                if lr:
                    if not lr.pchanged:
                        if [brd.sq_fr_pos([1, 0]).piece, brd.sq_fr_pos([2, 0]).piece, brd.sq_fr_pos([3, 0]).piece] == [None, None, None]:
                            return 'left'
                if rr:
                    if not rr.pchanged:
                        if [brd.sq_fr_pos([5, 0]).piece, brd.sq_fr_pos([6, 0]).piece] == [None, None]:
                            return 'right'

    def valid(self, brd):
        out = []
        for a in self.mvs(brd):
            if not brd.check(self.color, turn=[self.pos, a.pos]):
                out.append(a)
        if self.rakir(brd) == 'left':
            out.append(brd.sq_fr_pos([self.x - 2, self.y]))
        if self.rakir(brd) == 'right':
            out.append(brd.sq_fr_pos([self.x + 2, self.y]))
        return out