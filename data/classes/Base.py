import pygame
from data.classes.Square import Square
from data.classes.pieces.Rook import Rook
from data.classes.pieces.Bishop import Bishop
from data.classes.pieces.Knight import Knight
from data.classes.pieces.Queen import Queen
from data.classes.pieces.King import King
from data.classes.pieces.Pawn import Pawn
import pprint


baseboard = [
    ['RookW', 'KnightW', 'BishopW', 'QueenW', 'KingW', 'BishopW', 'KnightW', 'RookW'],
    ['PawnW', 'PawnW', 'PawnW', 'PawnW', 'PawnW', 'PawnW', 'PawnW', 'PawnW'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['PawnB', 'PawnB', 'PawnB', 'PawnB', 'PawnB', 'PawnB', 'PawnB', 'PawnB'],
    ['RookB', 'KnightB', 'BishopB', 'QueenB', 'KingB', 'BishopB', 'KnightB', 'RookB']
]


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tile_v = h // 8
        self.tile_h = w // 8
        self.clicked_on = None
        self.curr_turn = 'WH'
        self.i = self.phase2()
        self.setup()

    def phase2(self):
        out = []
        for y in range(8):
            for x in range(8):
                out.append(Square(x, y, self.tile_h, self.tile_v))
        return out

    def setup(self):
        for y, r in enumerate(baseboard):
            for x, p in enumerate(r):
                if p:
                    if p[-1] == 'W':
                        col = 'WH'
                    else:
                        col = 'BL'
                    sq = self.sq_fr_pos([x, y])
                    if 'Rook' in p:
                        sq.piece = Rook([x, y], col, self)
                    elif 'Knight' in p:
                        sq.piece = Knight([x, y], col, self)
                    elif 'Bishop' in p:
                        sq.piece = Bishop([x, y], col, self)
                    elif 'Queen' in p:
                        sq.piece = Queen([x, y], col, self)
                    elif 'King' in p:
                        sq.piece = King([x, y], col, self)
                    else:
                        sq.piece = Pawn([x, y], col, self)

    def sq_fr_pos(self, p):
        for square in self.i:
            if (square.x, square.y) == (p[0], p[1]):
                return square

    def click(self, mx, my):
        x = mx // self.tile_v
        y = my // self.tile_h
        print(x, y)
        print(mx // self.tile_h, my // self.tile_v)
        sq = self.sq_fr_pos([y, x])
        if self.clicked_on is None:
            if sq.piece:
                if sq.piece.color == self.curr_turn:
                    self.clicked_on = sq.piece
        elif self.clicked_on.move(self, sq):
            self.curr_turn = 'WH' if self.curr_turn == 'BL' else 'BL'
        elif sq.piece:
            if sq.piece.color == self.curr_turn:
                self.clicked_on = sq.piece

    def check(self, cl, turn=None):
        out = False
        king = None
        chp = None
        os = None
        ns = None
        nsog = None
        if turn:
            for sq in self.i:
                if sq.pos == turn[0]:
                    chp = sq.piece
                    os = sq
                    os.piece = None
            for sq in self.i:
                if sq.pos == turn[1]:
                    ns = sq
                    nsog = ns.piece
                    ns.piece = chp
        pieces = [a.piece for a in self.i if a.piece]
        if chp:
            if chp.type == 'king':
                king = ns.pos
        if king == None:
            for p in pieces:
                if p.type == 'king' and p.color == cl:
                    king = p.pos
        for p in pieces:
            if p.color != cl:
                for sq in p.attsq(self):
                    if sq.pos == king:
                        out = True
        if turn:
            os.piece = chp
            ns.piece = nsog
        return out

    def checkmate(self, color):
        out = False
        pieces = []
        for g in self.i:
            if g.piece is not None:
                pieces.append(g.piece)
        for b in pieces:
            if b:
                if b.type == 'king' and b.color == color:
                    king = b
        if not king.valid(self):
            out = True
        return out

    def draw(self, display):
        if self.clicked_on is not None:
            self.sq_fr_pos(self.clicked_on.pos).colalt = True
            for a in self.clicked_on.valid(self):
                a.colalt = True
        for b in self.i:
            b.draw(display)