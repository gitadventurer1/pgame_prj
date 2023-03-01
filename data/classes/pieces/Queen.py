import pygame
from data.classes.BasePiece import Piece


class Queen(Piece):
    def __init__(self, pos, color, brd):
        super().__init__(pos, color)
        self.img = pygame.image.load('data/images/Queen' + str(self.color) + '.png')
        self.img = pygame.transform.scale(self.img, (brd.tile_h - 20, brd.tile_v - 20))
        self.type = 'queen'

    def mvs(self, brd):
        fin = []
        m_upleft = []
        m_upright = []
        m_downleft = []
        m_downright = []
        for a in range(1, 8):
            if self.x - a < 0 or self.y - a < 0:
                break
            else:
                m_upleft.append(brd.sq_fr_pos([self.x - a, self.y - a]))

        for a in range(1, 8):
            if self.x + a > 7 or self.y - a < 0:
                break
            else:
                m_upright.append(brd.sq_fr_pos([self.x + a, self.y - a]))
        for a in range(1, 8):
            if self.x - a < 0 or self.y + a > 7:
                break
            else:
                m_downleft.append(brd.sq_fr_pos([self.x - a, self.y + a]))
        for a in range(1, 8):
            if self.x + a > 7 or self.y + a > 7:
                break
            else:
                m_downright.append(brd.sq_fr_pos([self.x + a, self.y + a]))
        fin += m_upleft
        fin += m_upright
        fin += m_downleft
        fin += m_downright
        m_left = []
        m_right = []
        m_down = []
        m_up = []
        for a in range(1, 8):
            if self.x - a < 0:
                break
            else:
                m_left.append(brd.sq_fr_pos([self.x - a, self.y]))

        for a in range(1, 8):
            if self.x + a > 7:
                break
            else:
                m_right.append(brd.sq_fr_pos([self.x + a, self.y]))
        for a in range(1, 8):
            if self.y + a > 7:
                break
            else:
                m_down.append(brd.sq_fr_pos([self.x, self.y + a]))
        for a in range(1, 8):
            if self.y - a < 0:
                break
            else:
                m_up.append(brd.sq_fr_pos([self.x, self.y - a]))
        fin += m_up
        fin += m_right
        fin += m_down
        fin += m_left
        return fin